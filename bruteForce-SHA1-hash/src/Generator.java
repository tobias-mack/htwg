import java.security.NoSuchAlgorithmException;

//put in SHA1 hash, set min and max length and brute force the pw
public class Generator {

    private char[] charset;
    String hashToCrack = "d3074410225100d565315762b4530e4d53cd3939";

    private int min; //var added for min char length
    private int max; //var added for max char length

    public Generator() {
        charset = "abcdefghijklmnopqrstuvwxyzA0123456789BCDEFGHJKLMNOPQRSTUVWXYZ".toCharArray();
        //charset = "abc".toCharArray();
        min = 5; // min length of password
        max = 6; // max length of password -1
    }

    public void generate(String str, int pos, int length,final long startTime) throws NoSuchAlgorithmException {
        if (length == 0) {      //if string has reached length of password
            String hash = HashTextTest.sha1(str);       // generate hash of password
            if (hash.equals(hashToCrack)){              //check if generated hash == hashToCrack
                System.out.println("the hash: " + hashToCrack + "\nthe password: "+ str);
                final long endTime = System.currentTimeMillis();
                System.out.println("Total execution time: " + (endTime - startTime) +"ms");
                System.exit(0);
            }
            //System.out.println(str);      //prints each possible string
        } else {

            //This if statement resets the char position back to the very first character in the character set ('a'), which makes this a complete solution to an all combinations bruteforce!
            if (pos != 0) {
                pos = 0;
            }

            for (int i = pos; i < charset.length; i++) {
                generate(str + charset[i], i, length - 1,startTime);
            }
        }
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Generator bruteforce = new Generator();
        final long startTime = System.currentTimeMillis();
        for (int length = bruteforce.min; length < bruteforce.max; length++) {
            bruteforce.generate("", 0, length,startTime);
        }
    }

}
