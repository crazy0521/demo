# 🔎 How to Run
# first take a image and name it as input.py

# Save the code as crypto_watermark.py.

# Install Pillow if you haven’t:

# pip install pillow


# Embed a watermark:

# python crypto_watermark.py embed --in input.png --out watermarked.png --text "MyName 2025" --key "mysecret"


# (Use a reasonably sized image like 800×600 PNG/JPG.)

# Extract and verify:

# python crypto_watermark.py extract --in watermarked.png --key "mysecret"

from PIL import Image
import hmac, hashlib
import math
import sys

SEPARATOR = "||:||"  # must be unique in watermark

def _to_bit_list(data_bytes):
    bits = []
    for b in data_bytes:
        for i in range(7, -1, -1):
            bits.append((b >> i) & 1)
    return bits

def _bits_to_bytes(bits):
    byts = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(bits):
                byte = (byte << 1) | bits[i + j]
            else:
                byte = (byte << 1)
        byts.append(byte)
    return bytes(byts)

def _hmac_sha256(key: bytes, message: bytes) -> bytes:
    return hmac.new(key, message, hashlib.sha256).digest()

def embed_watermark(input_image_path: str, watermark_text: str, key: str, output_image_path: str):
    """
    Embed watermark_text (string) into input_image_path and save as output_image_path.
    key (string) used to compute HMAC protecting watermark.
    """
    img = Image.open(input_image_path)
    img = img.convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())

    # build payload: watermark + separator + hmac
    watermark_bytes = watermark_text.encode('utf-8')
    key_bytes = key.encode('utf-8')
    tag = _hmac_sha256(key_bytes, watermark_bytes)
    payload = watermark_bytes + SEPARATOR.encode('utf-8') + tag

    payload_bits = _to_bit_list(payload)

    # capacity: 3 bits per pixel (LSB of R,G,B)
    capacity_bits = width * height * 3
    if len(payload_bits) > capacity_bits:
        raise ValueError(f"Payload too large for image. Need {len(payload_bits)} bits, capacity {capacity_bits} bits.")

    # embed bits
    new_pixels = []
    bit_idx = 0
    for (r, g, b) in pixels:
        r_new = r
        g_new = g
        b_new = b
        if bit_idx < len(payload_bits):
            r_new = (r & ~1) | payload_bits[bit_idx]
            bit_idx += 1
        if bit_idx < len(payload_bits):
            g_new = (g & ~1) | payload_bits[bit_idx]
            bit_idx += 1
        if bit_idx < len(payload_bits):
            b_new = (b & ~1) | payload_bits[bit_idx]
            bit_idx += 1
        new_pixels.append((r_new, g_new, b_new))

    # If any pixels left (no more payload bits), just copy remaining pixels unchanged
    if bit_idx < capacity_bits:
        # copy the remainder of original pixels if not already processed
        # (we already processed all pixels in loop above, but if payload was smaller,
        # new_pixels length equals pixels length anyway)
        pass

    # create new image and save
    out_img = Image.new('RGB', (width, height))
    out_img.putdata(new_pixels)
    out_img.save(output_image_path)
    print(f"Watermark embedded and saved to {output_image_path}.")
    print(f"Embedded watermark length: {len(watermark_bytes)} bytes, HMAC length: {len(tag)} bytes.")

def extract_watermark(image_path: str, key: str) -> (str, bool):
    """
    Extract watermark and verify HMAC with key.
    Returns (watermark_text, is_valid)
    """
    img = Image.open(image_path)
    img = img.convert('RGB')
    width, height = img.size
    pixels = list(img.getdata())

    bits = []
    # read LSBs in same order we wrote: R,G,B per pixel
    for (r, g, b) in pixels:
        bits.append(r & 1)
        bits.append(g & 1)
        bits.append(b & 1)

    # convert bits to bytes progressively and look for separator
    all_bytes = _bits_to_bytes(bits)
    # as we don't know exact watermark length, we try to find separator bytes
    sep_bytes = SEPARATOR.encode('utf-8')
    idx = all_bytes.find(sep_bytes)
    if idx == -1:
        raise ValueError("Separator not found — no watermark or different embedding scheme.")

    watermark_bytes = all_bytes[:idx]
    tag_bytes = all_bytes[idx + len(sep_bytes): idx + len(sep_bytes) + hashlib.sha256().digest_size]

    # verify HMAC
    key_bytes = key.encode('utf-8')
    expected_tag = _hmac_sha256(key_bytes, watermark_bytes)
    is_valid = hmac.compare_digest(expected_tag, tag_bytes)

    try:
        watermark_text = watermark_bytes.decode('utf-8')
    except UnicodeDecodeError:
        watermark_text = watermark_bytes.decode('latin-1', errors='replace')

    return watermark_text, is_valid

# -------------------------
# Example usage (CLI)
# -------------------------
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Embed or extract cryptographic watermark in an image.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_embed = sub.add_parser("embed", help="Embed watermark")
    p_embed.add_argument("--in", dest="input", required=True, help="Input image path (PNG/JPG).")
    p_embed.add_argument("--out", dest="output", required=True, help="Output image path.")
    p_embed.add_argument("--text", dest="text", required=True, help="Watermark text to embed.")
    p_embed.add_argument("--key", dest="key", required=True, help="Secret key for HMAC.")

    p_extract = sub.add_parser("extract", help="Extract watermark")
    p_extract.add_argument("--in", dest="input", required=True, help="Watermarked image path.")
    p_extract.add_argument("--key", dest="key", required=True, help="Secret key for HMAC verification.")

    args = parser.parse_args()

    if args.cmd == "embed":
        embed_watermark(args.input, args.text, args.key, args.output)
    elif args.cmd == "extract":
        wm, ok = extract_watermark(args.input, args.key)
        print("Extracted watermark text:", wm)
        print("HMAC verification:", ok)
