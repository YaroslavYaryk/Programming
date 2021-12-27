// Определить абсолютное значение наименьшей разности между двумя любыми значениями
// элементов исходного одномерного массива a. 

import java.util.Scanner;
import java.util.Arrays;

public class Lab2_7 {
    public static void main(String[] args) throws Exception {
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
        System.out.printf("The lowwest absolute difference is %s\n", get_result(storage) );
        num.close();
    }

    public static int get_result(int[] storage){
        Arrays.sort(storage);
        int[] result = get_difference_array(storage);
        Arrays.sort(result);
        return result[0];
    }

    public static int[] get_difference_array(int[] array){
        int[] result_array = new int[array.length-1];
        for (int i = array.length-1; i > 0; i--){
            result_array[array.length-i-1] = array[i] - array[i-1];
        }
        return result_array;
    }
}



