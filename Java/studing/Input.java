package studing;
import java.util.Scanner;


public class Input {
    public static void main(String[] args) {
        System.out.println("enter smth, pls");
        Scanner a = new Scanner(System.in);
        System.out.println(a.nextLine()); //show string
        // System.out.println(a.nextInt()); //show int
        // System.out.println(a.nextDouble()); // show double
        // System.out.println(a.nextFloat()); // show float
        Scanner b = new Scanner(System.in);
        System.out.println("you've entered" + b.nextDouble());
        a.close();
        b.close();
    }
}
