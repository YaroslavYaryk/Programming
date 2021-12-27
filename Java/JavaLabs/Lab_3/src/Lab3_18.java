// Анализ типов аргументов, задаваемых при запуске программы.
//  Если аргумент является числом с плавающей точкой (шаблон: 
// состоит из мантиссы – одна или несколько цифр, возможно со 
// знаком "+" или "-", которая может содержать десятичную точку 
// в начале, середине или конце, а также порядка – целого числа 
// со знаком "+" или "-" или без знака, разделителем между мантиссой 
// и порядком служит символ "e" или символ "E"), то  тип аргумента "Float", 
// иначе "String". Программа выводит количество заданных аргументов и, для каждого аргумента, его тип и значение. 

import java.util.regex.Pattern;

public class Lab3_18 {
    public static void main(String[] args) {
        String[] input = args;
        System.out.println("length: " + args.length);
        for (int i=0; i<args.length; i++){
            if (check_if_float(input[i])){
                float result = Float.parseFloat(args[i]);
                System.out.println(result + " - float" );
            }    
            else{
                String result = args[i];
                System.out.println(result + " - string" );
            }
        }    
    }

    public static boolean check_if_float(String str){

        String regex1 = "[+-]";
        StringBuffer str_buff = new StringBuffer(str);
        
        if (! Pattern.matches(regex1, String.valueOf(str.charAt(0))))
            str_buff.insert(0, '+');

        String regex = "[+-][0-9]+[.][1-9]+";
        String regex2 = "[+-][0-9]+[.][1-9]+[Ee][-+ 0-9][0-9]+";

        if (Pattern.matches(regex, str_buff) || (Pattern.matches(regex2, str_buff)))
            return true;
        
        return false;
    }
}
