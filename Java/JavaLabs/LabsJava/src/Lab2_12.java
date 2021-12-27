import java.util.Scanner;
import java.util.Arrays;

public class Lab2_12 {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int numbers = num.nextInt();
        int storage[] = new int[numbers];
        for (int i=0; i<numbers; i++){
            System.out.printf("storage[%s] ", i+1);
            storage[i] = num.nextInt();
        } 
        if (is_sorted_up(storage)){
            System.out.printf("Array %s - sorted up\n" ,Arrays.toString(storage));
        }
        else if (is_sorted_down(storage)){
            System.out.printf("Array %s - sorted down\n" ,Arrays.toString(storage));
        }
        else{
            System.out.printf("Array %s - isn't sorted\n" ,Arrays.toString(storage));
        }
        num.close();
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