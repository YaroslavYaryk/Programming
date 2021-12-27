// Определить количество равных элементов и 
// их индексы для двух исходных одномерных массивов a и b.


import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Lab2_27 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements in a: ");
        int numbers1 = 0;
        try{
            numbers1 = Integer.parseInt(num.next());
        }catch (NumberFormatException ex) {
            System.out.println("The number is not an integer ");
            System.exit(0);
        }
        int[] a = new int[numbers1];
        for (int i=0; i<numbers1; i++){
            try{
                System.out.printf("storage[%s] ", i+1);
                a[i] = Integer.parseInt(num.next());
            }catch (NumberFormatException ex) {
                System.out.println("The number is not an integer ");
                System.exit(0);
            }
        }
        System.out.print("Enter number of elements in b: ");
        int numbers2 = 0;
        try{
            numbers2 = Integer.parseInt(num.next());
        }catch (NumberFormatException ex) {
            System.out.println("The number is not an integer ");
            System.exit(0);
        }
        int[] b = new int[numbers2];
        for (int i=0; i<numbers2; i++){
            try{
                System.out.printf("storage[%s] ", i+1);
                b[i] = Integer.parseInt(num.next());
            }catch (NumberFormatException ex) {
                System.out.println("The number is not an integer ");
                System.exit(0);
            }
        }

        Map<Integer, int[]> int_store = new HashMap<Integer, int[]>();
        System.out.println("\n|Element - [a, b]|");
        System.out.println("+------------------+");
        get_result(int_store, a, b);
        for (Map.Entry<Integer, int[]> pair : int_store.entrySet()) {
            System.out.println(String.format("|%s - %s|", pair.getKey(), Arrays.toString(pair.getValue())));
        }
        System.out.println("total similarity - " + int_store.size());
        num.close();
    }

    public static Map get_result(Map<Integer, int[]> int_store,int[] a, int[] b) {
        for (int i = 0; i < b.length; i++) {
            if (is_in_array(a, b[i])) {
                int[] temp = new int[]{get_index(a, b[i]), i};
                int_store.put(b[i], temp);
            }
        }
        return  int_store;
    }

    
    public static boolean is_in_array(int[] array, int element){
        for (int i=0; i< array.length; i++){
            if (array[i] == element){
            return true;
            }
        }
        return false;
    }

    public static int get_index(int[] array, int element){
        for (int i=0; i< array.length; i++){
            if (array[i] == element){
            return i;
            }
        }
        return 1;
    }
}
