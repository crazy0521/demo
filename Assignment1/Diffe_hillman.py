# --- Diffie-Hellman Key Exchange with User Input ---

def diffie_hellman():
    """
    Performs the Diffie-Hellman key exchange based on user input.
    """
    try:
        print("\n--- Diffie-Hellman Key Exchange ---")
        
        # Get publicly known values from the user
        p_str = input("Enter a large prime number (p): ")
        g_str = input("Enter a primitive root (g) for p: ")
        
        p = int(p_str)
        g = int(g_str)

        print(f"\nPublicly known values:\np = {p}, g = {g}")

        # Get Alice's private key
        a_str = input("Enter Alice's private key (a): ")
        a = int(a_str)
        
        # Calculate Alice's public key
        A = pow(g, a, p)  # A = g^a mod p
        print(f"Alice's private key (a): {a}")
        print(f"Alice's public key (A): {A} (This is sent to Bob)")

        # Get Bob's private key
        b_str = input("\nEnter Bob's private key (b): ")
        b = int(b_str)
        
        # Calculate Bob's public key
        B = pow(g, b, p)  # B = g^b mod p
        print(f"Bob's private key (b): {b}")
        print(f"Bob's public key (B): {B} (This is sent to Alice)")

        # Exchange public keys A and B
        print("\n--- Key Exchange ---")
        print("Alice receives Bob's public key (B) and computes the shared secret.")
        print("Bob receives Alice's public key (A) and computes the shared secret.")
        
        # Compute shared secret keys
        shared_key_alice = pow(B, a, p)  # (B^a) mod p
        shared_key_bob = pow(A, b, p)    # (A^b) mod p

        print(f"\nShared secret (computed by Alice): {shared_key_alice}")
        print(f"Shared secret (computed by Bob):   {shared_key_bob}")

        if shared_key_alice == shared_key_bob:
            print("\n✅ Shared secret established successfully!")
        else:
            print("\n❌ Shared secret mismatch!")

    except ValueError:
        print("\nError: Please enter valid whole numbers for all values.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# =======================
# === MAIN PROGRAM =====
# =======================
if __name__ == "__main__":
    diffie_hellman()