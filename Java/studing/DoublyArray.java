package studing;
import java.util.Scanner;


public class DoublyArray {
    public static void main(String[] args) {
        Scanner num = new Scanner(System.in);
        int[][] array = new int[3][3];
        for (int i=0; i< 3; i++){
            for(int j = 0; j<3; j++){
                System.out.print("array[" + i + "]["+ j + "] = ");
                array[i][j] = num.nextInt();
            }
        }

        for (int i=0; i< 3; i++){
            for(int j = 0; j<3; j++){
                System.out.print(array[i][j] + " ");
            }
            System.out.println();    
        }

        num.close();
    }
}
