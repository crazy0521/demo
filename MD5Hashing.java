/*⚙️ How to Run

Save the file as MD5Hashing.java

Open Command Prompt or VS Code terminal in the same folder

Compile the code:

javac MD5Hashing.java


Run the program:

java MD5Hashing */




// MD5Hashing.java
import java.security.MessageDigest;
import java.util.Scanner;

public class MD5Hashing {
    public static void main(String[] args) {
        try {
            // Taking input from user
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter text to generate MD5 hash: ");
            String input = sc.nextLine();

            // Step 1: Create MessageDigest instance for MD5
            MessageDigest md = MessageDigest.getInstance("MD5");

            // Step 2: Add input bytes to digest
            md.update(input.getBytes());

            // Step 3: Get the hash's bytes
            byte[] digest = md.digest();

            // Step 4: Convert byte array into hexadecimal format
            StringBuilder hexString = new StringBuilder();
            for (byte b : digest) {
                hexString.append(String.format("%02x", b));
            }

            // Step 5: Display the MD5 hash
            System.out.println("MD5 Hash: " + hexString.toString());

            sc.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
