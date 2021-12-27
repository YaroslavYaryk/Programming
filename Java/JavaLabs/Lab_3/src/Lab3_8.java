// Создайте программу, которая принимает произвольный текстовую строку, 
// а возвращает другой, в котором символы располагаются в обратном порядке.

import java.util.*;


public class Lab3_8 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.print("Enter string: ");

        String input_string = myObj.nextLine();  // Read user input
        
        System.out.printf("Reversed string - %s\n", get_reverse_string(input_string));
        myObj.close();
    }

    public static String get_reverse_string(String str){

        StringBuffer str_buff = new StringBuffer(str);

        str_buff.reverse();

        return str_buff.toString();
    }
}
