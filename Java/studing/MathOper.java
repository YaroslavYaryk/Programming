package studing;
import java.util.Scanner;


public class MathOper {
    public static void main(String[] args) {
        float a, b, c;
        Scanner num = new Scanner(System.in);
        System.out.print("Enter the first one: ");
        a = num.nextInt();
        System.out.print("Enter the second one: ");
        b = num.nextInt();
        System.out.print("Enter the third one: ");
        c = num.nextInt();
        float result_add = a + b + c;
        float result_sub = a - b - c;
        float result_mul = a * b * c;
        float result_div = a / b / c;
        float result = a % b;
        result *=2; 

        System.out.println("the result_add is: " + result_add);
        System.out.println("the result_sub is: " + result_sub);
        System.out.println("the result_mul is: " + result_mul);
        System.out.println("the result_divv is: " + result_div);
        System.out.println("the result is: " + result);



        num.close();
    }
}
