
/*⚙️ Step 1: Compile the program

Open your Command Prompt or Terminal in the folder where the file is saved and run:

javac DigitalSignature.java


This will generate a compiled file named DigitalSignature.class.

▶️ Step 2: Run the program

Now run the compiled file using:

java DigitalSignature
*/









import java.security.*;
import java.util.Base64;

public class DigitalSignature {
    public static void main(String[] args) throws Exception {
        // Step 1: Generate Key Pair (Public & Private keys)
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(2048);  // 2048-bit key for strong security
        KeyPair pair = keyGen.generateKeyPair();
        PrivateKey privateKey = pair.getPrivate();
        PublicKey publicKey = pair.getPublic();

        // Step 2: Message to be signed
        String message = "This is a confidential message.";
        System.out.println("Original Message: " + message);

        // Step 3: Create Signature using SHA256withRSA
        Signature sign = Signature.getInstance("SHA256withRSA");
        sign.initSign(privateKey);
        sign.update(message.getBytes());
        byte[] signatureBytes = sign.sign();
        String signature = Base64.getEncoder().encodeToString(signatureBytes);
        System.out.println("\nDigital Signature (Base64 Encoded): " + signature);

        // Step 4: Verify the Signature
        Signature verifySign = Signature.getInstance("SHA256withRSA");
        verifySign.initVerify(publicKey);
        verifySign.update(message.getBytes());
        boolean isCorrect = verifySign.verify(signatureBytes);
        System.out.println("\nSignature Verified: " + isCorrect);
    }
}
