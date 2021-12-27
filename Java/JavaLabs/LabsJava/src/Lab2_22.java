import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Lab2_22 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int numbers = num.nextInt();
        Integer[] a = new Integer[numbers];
        for (int i=0; i<numbers; i++){
            System.out.printf("a[%s] ", i+1);
            a[i] = num.nextInt();
        }
        Map<Integer, Integer> int_store = new HashMap<Integer, Integer>();
        for (int i=0; i<numbers; i++){
            int_store.put(i, a[i]);
        } 
        for (Map.Entry<Integer, Integer> pair : int_store.entrySet()) {
            System.out.println(String.format("|%s - %s|", pair.getKey(),pair.getValue())); 
        }
        Arrays.sort(a, Collections.reverseOrder());
        Integer[] b = new Integer[numbers];
        for (int i=0; i<numbers; i++){
            b[i] = get_key(int_store,a[i]);
            int_store.remove(get_key(int_store,a[i]));
        }
        System.out.printf("The new array is %s\n", Arrays.toString(b));
        num.close();
    }

    public static int get_key(Map<Integer, Integer> obj, int elem){
        for (Map.Entry<Integer, Integer> pair : obj.entrySet()) {
            if (pair.getValue() == elem){
            return pair.getKey();
            }
        }
        return 1;
    }
}
