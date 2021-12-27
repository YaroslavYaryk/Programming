import java.util.Scanner;
import java.util.Arrays;


public class Lab2_7 {
    public static void main(String[] args) throws Exception {
        Scanner num = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int numbers = num.nextInt();
        int storage[] = new int[numbers];
        for (int i=0; i<numbers; i++){
            System.out.printf("storage[%s]", i+1);
            storage[i] = num.nextInt();
        }        
        get_result(storage);
        num.close();
    }

    public static void get_result(int[] storage){
        Arrays.sort(storage);
        int[] result = get_difference_array(storage);
        Arrays.sort(result);
        System.out.printf("The lowwest absolute difference is %s\n", result[0] );
    }

    public static int[] get_difference_array(int[] array){
        int result_array[] = new int[array.length-1];
        for (int i = array.length-1; i > 0; i--){
            result_array[array.length-i-1] = array[i] - array[i-1];
        } 
        return result_array;
    }
}



// public class Lab_2_27_test {

//     @Test
//     public void test_main(){
//         Lab2_7 object = new ThingAdder();
//         int one = 1;
//         int two = 2;
        
//         int result = thingAdder.addThings(one, two);

//         Assert.assertEquals(3, result);
//     }
// }
