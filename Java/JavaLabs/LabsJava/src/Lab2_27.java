import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Lab2_27 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements in a: ");
        int numbers1 = num.nextInt();
        int a[] = new int[numbers1];
        for (int i=0; i<numbers1; i++){
            System.out.printf("a[%s] ", i+1);
            a[i] = num.nextInt();
        }
        System.out.print("Enter number of elements in b: ");
        int numbers2 = num.nextInt();
        int b[] = new int[numbers2];
        for (int i=0; i<numbers2; i++){
            System.out.printf("b[%s] ", i+1);
            b[i] = num.nextInt();
        }

        Map<Integer, int[]> int_store = new HashMap<Integer, int[]>();
        for (int i=0; i<numbers2; i++){
            if (is_in_array(a, b[i])){
            int temp[] = new int[] { get_index(a, b[i]) ,i};
            int_store.put(b[i], temp);
            } 
        } 
        System.out.println("\n|Element - [a, b]|");
        System.out.println("+------------------+");
        for (Map.Entry<Integer, int[]> pair : int_store.entrySet()) {
            System.out.println(String.format("|%s - %s|", pair.getKey(), Arrays.toString(pair.getValue()))); 
        }
        System.out.println("total similarity - " + int_store.size());
        num.close();
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
