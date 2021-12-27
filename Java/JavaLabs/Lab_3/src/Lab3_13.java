// Создайте программу, которая осуществляет шифрование / расшифровка методом простой замены. 
// В нем каждый символ незашифрованного текста из исходного алфавита заменяется другим из алфавита, 
// символы в каком представлены в соответствии с ключом шифрования.

import java.util.*;

public class Lab3_13 {
    public static void main(String[] args) {

        String alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZABCDEFGHIJKLMNOPQRSTUVWZYZ";
        Scanner myObj = new Scanner(System.in);
        System.out.print("Enter string: ");
        String input_string = myObj.nextLine();
        System.out.print("Enter key(int): ");
        int key = 0;
        int choice=1;
        try{
            key = Integer.parseInt(myObj.next());

            System.out.print("Shifr(1) Deshifr(2): ");
            choice = Integer.parseInt(myObj.next());
        }catch (NumberFormatException ex) {
            System.out.println("The number is not an integer ");
            System.exit(0);
        }
        if (choice == 1)
            System.out.printf("Shifered string - %s\n", get_shifred_string(input_string, key, alphabet));
        else if (choice == 2)
            System.out.printf("Deshifered string - %s\n", get_deshifred_string(input_string, key, alphabet));  
        else
            System.out.printf("No choice\n");  
        myObj.close();
    }

    public static String get_shifred_string(String str,int key ,String alphabet){
        
        String result = "";
        for (int i=0; i<str.length(); i++){
            result += (alphabet.charAt(alphabet.indexOf(str.charAt(i)) + key));
        }
        return result;
    }
    public static String get_deshifred_string(String str,int key ,String alphabet){
        
        String result = "";
        for (int i=0; i<str.length(); i++){

            result += (alphabet.charAt(alphabet.lastIndexOf(str.charAt(i)) - key));
        }
        return result;
    }
}
