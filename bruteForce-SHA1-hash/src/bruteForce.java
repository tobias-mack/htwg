//all possibilities for 3 letters
// -> implementation for longer passwords with recursive calls @Generator.java
public class bruteForce {
    public static void main(String[] args) {
        String inputString = "abc";
        char [] finalString = inputString.toCharArray();
        for (int o = 0; o < inputString.length(); o++) {
            finalString[0] = inputString.charAt(o);
            for (int i = 0; i < inputString.length(); i++) {
                finalString[1] = inputString.charAt(i);
                for (int j = 0; j < inputString.length(); j++) {
                    finalString[2]  = inputString.charAt(j);
                    System.out.println(finalString);
                }

            }
        }
    }
}
