// Определить, образуют ли значения элементов исходного одномерного массива a:
// строго возрастающую последовательность (ai < ai+1), 
// строго убывающую последовательность (ai > ai+1) или элементы массива
// не упорядочены и вывести для каждого случая соответствующее сообщение.

import java.util.Scanner;
import java.util.Arrays;

public class Lab2_12 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int numbers = 0;
        try{
            numbers = Integer.parseInt(num.next());
        }catch (NumberFormatException ex) {
            System.out.println("The number is not an integer ");
            System.exit(0);
        }
        int[] storage = new int[numbers];
        for (int i=0; i<numbers; i++){
            try{
                System.out.printf("storage[%s] ", i+1);
                storage[i] = Integer.parseInt(num.next());
            }catch (NumberFormatException ex) {
                System.out.println("The number is not an integer ");
                System.exit(0);
            }
        }
        num.close();
        System.out.println(get_result(storage));
    }

    static String get_result(int[] storage) {
            if (is_sorted_up(storage)){
                return String.format("Array %s - sorted up\n" ,Arrays.toString(storage));
            }
            else if (is_sorted_down(storage)){
                return String.format("Array %s - sorted down\n" ,Arrays.toString(storage));
            }
            else{
                return String.format("Array %s - isn't sorted\n" ,Arrays.toString(storage));
            }
        }

    static boolean is_sorted_up(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] > array[i + 1])
            return false;
        }
        return true;
    }

    static boolean is_sorted_down(int[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i] < array[i + 1])
            return false;
        }
        return true;
    }
}