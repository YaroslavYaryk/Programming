// Создайте приложение для просмотра списка элементов и
// изменения значений элементов списка.  Список
// (5 элементов типа Integer) создается в программе и является объектом класса  ArrayList.


import java.util.ArrayList;
import java.util.Scanner;

public class Lab4_22 {
    public static void main(String[] args) {
        ArrayList<Integer> array = new ArrayList<>();
        array.add(1);
        array.add(2);
        array.add(3);
        array.add(2);
        array.add(5);

        System.out.println("Here is array - [ " + GetStringArray(array) + "]");
        Scanner scan = new Scanner(System.in);

        int elem = 0;
        int value = 0;
        try{
            System.out.print("which elem you wanna change: ");
            elem = Integer.parseInt(scan.next());
            System.out.print("new element: ");
            value = Integer.parseInt(scan.next());
        }catch (NumberFormatException ex) {
            System.out.println("The number is not an integer ");
            System.exit(0);
        }

        if (count_spec_element(array, elem) != 1){
            System.out.println("\nThere is " + count_spec_element(array, elem) + " equal elems in array" );
            System.out.println("Which of them you wanna change" );
            int num = 0;
            try{
                num = Integer.parseInt(scan.next());

            }catch (NumberFormatException ex) {
                System.out.println("The number is not an integer ");
                System.exit(0);
            }
            array.set(get_index_by_element(array, elem, num), value);
        }
        else{
            array.set(get_index_by_element(array, elem, 1), value);
        }

        // System.out.println(get_index_by_element(array, 4));
        System.out.println("Here is new array - [ " + GetStringArray(array) + "]");
        scan.close();
    }

    public static String GetStringArray(ArrayList<Integer> arr)
    {

        String str = "";

        // ArrayList to Array Conversion
        for (int j = 0; j < arr.size(); j++) {

            // Assign each value to String array
            str  += arr.get(j) + ", ";
        }

        return str;
    }

    public static Integer get_index_by_element(ArrayList<Integer> arr, int elem, int count){

        int inner_count = 1;
        for (int i = 0; i < arr.size(); i++) {

            if (arr.get(i) == elem){
                if (inner_count == count){
                    return i;
                }
                inner_count+=1;
            }
        }

        return 0;
    }

    public static int count_spec_element(ArrayList<Integer> arr, int elem){

        int count = 0;
        for (int i = 0; i < arr.size(); i++) {

            if (arr.get(i) == elem){
                count +=1;
            }
        }

        return count;
    }
}
