public class BufferOverflowDemo {
    public static void main(String[] args) {

        String source = "too long";
        char[] dest = new char[5];
        int trigger = 5;

        if (trigger == 5) {

            // Simulating unsafe copy
            for (int i = 0; i < source.length(); i++) {
                dest[i] = source.charAt(i);
            }
        }

        System.out.println("Done");
    }
}
