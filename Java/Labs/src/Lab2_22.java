// Сформировать массив b, элементами которого являются 
// значения индексов элементов исходного одномерного 
// массива a в порядке убывания значений элементов.


import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;

public class Lab2_22 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int numbers = 0;
        try {
            numbers = Integer.parseInt(num.next());
        } catch (NumberFormatException ex) {
            System.out.println("The number is not an integer ");
            System.exit(0);
        }
        Integer[] a = new Integer[numbers];
        for (int i = 0; i < numbers; i++) {
            try {
                System.out.printf("storage[%s] ", i + 1);
                a[i] = Integer.parseInt(num.next());
            } catch (NumberFormatException ex) {
                System.out.println("The number is not an integer ");
                System.exit(0);
            }
        }
        Map<Integer, Integer> int_store = new HashMap<Integer, Integer>();
        for (int i = 0; i < numbers; i++) {
            int_store.put(i, a[i]);
        }
        for (Map.Entry<Integer, Integer> pair : int_store.entrySet()) {
            System.out.println(String.format("|%s - %s|", pair.getKey(), pair.getValue()));
        }
        System.out.printf("The new array is %s\n", Arrays.toString(get_result(int_store, a)));
        num.close();
    }

    public static Integer[] get_result(Map<Integer, Integer> int_store, Integer[] a){
        Arrays.sort(a, Collections.reverseOrder());
        Integer[] b = new Integer[a.length];
        for (int i=0; i<a.length; i++){
            b[i] = get_key(int_store,a[i]);
            int_store.remove(get_key(int_store,a[i]));
        }
        return b;
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
