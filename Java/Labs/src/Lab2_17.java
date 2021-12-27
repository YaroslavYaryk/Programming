// Сформируйте из массива a массив b по следующему алгоритму: 
// элемент массива b равен значению разности между максимальным 
// значением элементов массива a и значением данного элемента массива a.


import java.util.Scanner;
import java.util.Arrays;

public class Lab2_17 {
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
        System.out.printf("The new array is %s\n", Arrays.toString(get_difference_array(storage)) );
        num.close();
    }
    public static int[] get_difference_array(int[] array){
        int[] result_array = Arrays.copyOf(array, array.length);
        int[] new_array = new int[array.length];
        Arrays.sort(result_array);
        int max_elem = result_array[array.length-1];
        System.out.println("Max elem is " + max_elem);
        for (int i = 0; i < array.length; i++){
            new_array[i] = max_elem - array[i];
        } 
        return new_array;
    }
}