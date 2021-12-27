// Анализ типов аргументов, задаваемых при 
// запуске программы. Если аргумент имеет вид 
// "имя=значение", то он является ключевым параметром 
// (тип "Keyed"), если аргумент имеет вид "-значение" 
// или "/значение", то он является опцией (тип "Optional") 
// и если имеет вид "значение", то является непосредственным 
// параметром (тип "Immediate"). Шаблон для значения: одна или 
// несколько цифр и букв (включая буквы кириллицы). Программа
// выводит количество заданных аргументов и, для каждого аргумента, 
// его тип и значение (для ключевых параметров дополнительно выводится имя параметра)

import java.util.regex.Matcher;
import java.util.regex.Pattern;



public class Lab3_22 {

    public static void main(String[] args) {
        System.out.println("length: " + args.length);
        for (int i=0; i<args.length; i++){
            if (check_is_keyed(args[i])){
                System.out.println(args[i].split("=")[1] + "  -  Keyed  (name) = " + args[i].split("=")[0] );
            }
            else if (check_is_optional(args[i])){
                System.out.println(args[i] + "  -  Optional" );
            }
            else if (check_is_immediate(args[i])){
                System.out.println(args[i] + "  -  Immediate" );
            }
            else{
                System.out.println(args[i] + "  -  Unknown" );
            }
        } 

    }

    public static boolean check_is_keyed(String str){

        String regex = "[a-zA-Z]+=[a-zA-Z0-9а-яА-Я]+";
        Pattern p = Pattern.compile(regex, Pattern.UNICODE_CHARACTER_CLASS);

        Matcher m = p.matcher(str);
        if (m.matches()){
            return true;
        }
        return false;        
    }

    public static boolean check_is_optional(String str){

        String regex = "[-/][a-zA-Z0-9а-яА-Я]+";
        Pattern p = Pattern.compile(regex, Pattern.UNICODE_CHARACTER_CLASS);

        Matcher m = p.matcher(str);
        if (m.matches()){
            return true;
        }
        return false;
    }

    public static boolean check_is_immediate(String str){

        String regex = "[a-zA-Z0-9а-яА-Я]+";
        Pattern p = Pattern.compile(regex, Pattern.UNICODE_CHARACTER_CLASS);

        Matcher m = p.matcher(str);
        if (m.matches()){
            return true;
        }
        return false;
    }
}

