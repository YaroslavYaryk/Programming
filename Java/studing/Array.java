package studing;

public class Array {
    public static void main(String[] args) {
        int[] array = new int[10]; //initialization without adding element
        int[] array2 = new int[] {1,2,3,4,3}; //initialization with adding 5 elements

        for (int i=0; i<5; i++)
            System.out.println(array2[i]);

        for (int i = 0; i < 10; i++){
            array[i] = i;
        }

        for (int i = 0; i < 10; i++){
            System.out.print(array[i]);
        }
        System.out.println();

    }
}
