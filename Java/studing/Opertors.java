package studing;
import java.util.Scanner;
import java.util.Random;


public class Opertors {
    public static void main(String[] args) {
        Random rand = new Random();
        int rand_int = rand.nextInt(100);
        Scanner num = new Scanner(System.in);
        int digit;
        do {
            System.out.print("Enter a digit:  ");
            digit = num.nextInt();

            if (digit == rand_int)
                System.out.println("You won, Great job");
            else if (digit > rand_int)
                System.out.println("bigger");
            else
                System.out.println("lowwer"); 
                      
        }while(digit != rand_int);
        num.close();
    }
}
