// Построить программу для работы с классом Правильная дробь, 
// который должен включать соответствующие поля: числитель, знаменатель. 
// Программа должна обеспечивать простейшие функции: сложение, вычитание, 
// умножение, деление, вывод дроби в удобной форме. 

import java.lang.*;
import javax.management.BadAttributeValueExpException;
import java.util.Objects;
/** Interface for Square class
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
interface Lab5_8_interface {

    String cool_print();
    Fraction add(Fraction obj);
    Fraction diff(Fraction obj);
    Fraction mul(Fraction obj);
    Fraction truediv(Fraction obj);
}

/** Class for saving Square
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
class Fraction implements Lab5_8_interface{
    /** property - numerator */
    Integer numerator = 1;

    /** property - denumerator */
    Integer denumerator = 1;

    /** Create new object with this values
     * @param numerator - numerator
     * @param denumerator - denominator
     */
    public Fraction(Integer numerator, Integer denumerator){
        if (denumerator == 0  ){
            System.out.println("Wrong fraction");
            System.exit(0);
        }

        this.numerator = numerator;
        this.denumerator = denumerator;
    }

    @Override
    public String toString() {
        return numerator + "/" + denumerator;
    }

    /** Returns parameters
     @return nice form of elements
     */
    @Override
    public String cool_print() {

        return numerator.toString() + "/" + denumerator.toString();
    }

    /** Returns parameters
     * @param obj - Fraction obj
     * @param sign - sign(+/-)
     @return numerator and denumerator
     */
    private int[] get_arifmetic_result(Fraction obj, String sign){
        int numerator = 0;
        if (Objects.equals(sign, "add")){
            numerator = this.numerator*obj.denumerator + this.denumerator*obj.numerator;
        }
        else if (Objects.equals(sign, "diff")){
            numerator = this.numerator*obj.denumerator - this.denumerator*obj.numerator;
        }
        int denumerator = this.denumerator*obj.denumerator;
        int j = Math.min(numerator, denumerator);
        for(int i = 2; i<= j ;i ++){
            while(numerator%i ==0&&denumerator%i ==0){
                numerator /= i;denumerator /= i;
            }
        }
        return new int[] {numerator, denumerator};
    }

    /** Returns Fraction object of added Fractions
     * @param obj - Fraction obj
    see also {@link Fraction#Fraction(Integer, Integer)}.
     */
    @Override
    public Fraction add(Fraction obj){
        int[] result = get_arifmetic_result(obj, "add");
        return new Fraction(result[0], result[1]);
    }


    /** Returns Fraction object of difference Fractions
     * @param obj - Fraction obj
    see also {@link Fraction#Fraction(Integer, Integer)}.
     */
    @Override
    public Fraction diff(Fraction obj){
        int[] result = get_arifmetic_result(obj, "diff");
        return new Fraction(result[0], result[1]);
    }

    /** Returns greater common divisor
     * @param a - first element
     * @param b - second element
     @return greater common divisor
     */
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    /** Returns redused two elements
     * @param a - first element
     * @param b - second element
     @return array aof two reduced integers
     */
    public static int[] reduce_fraction(int a, int b) {
        int gcd = gcd(a, b);
        return new int[] {(a / gcd), (b / gcd)};
    }

    /** Returns Fraction object of multiply Fractions
     * @param obj - Fraction obj
    see also {@link Fraction#Fraction(Integer, Integer)}.
     */
    @Override
    public Fraction mul(Fraction obj) {
        int numerator = this.numerator * obj.numerator;
        int denumerator = this.denumerator * obj.denumerator;
        int[] result = reduce_fraction(numerator, denumerator);
        return new Fraction(result[0], result[1]);
    }

    /** Returns Fraction object of truedivisions Fractions
     * @param obj - Fraction obj
    see also {@link Fraction#Fraction(Integer, Integer)}.
     */
    @Override
    public Fraction truediv(Fraction obj) {
        int numerator = this.numerator * obj.denumerator;
        int denumerator = this.denumerator * obj.numerator;
        int[] result = reduce_fraction(numerator, denumerator);
        return new Fraction(result[0], result[1]);
    }

}


public class Lab5_8 {
    public static void main(String[] args) throws BadAttributeValueExpException {
        Lab5_8_interface element1 = new Fraction(1, 2);
        Fraction element2 = new Fraction(3, 4);
        Fraction element3 = element1.add(element2);
        System.out.println(element3.cool_print());

    }

}