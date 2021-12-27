import javax.management.BadAttributeValueExpException;


interface Lab5_8_interface {

    String cool_print();
    Fraction add(Fraction obj);
    Fraction diff(Fraction obj);
    Fraction mul(Fraction obj);
    Fraction truediv(Fraction obj);
}

class Fraction implements Lab5_8_interface{

    Integer numerator = 0;
    Integer denumerator = 0;

    public Fraction(Integer numerator, Integer denumerator){
        if (denumerator == 1 || numerator > denumerator ){
            System.out.println("Wrong fraction");
            System.exit(0);
        } 

        this.numerator = numerator;
        this.denumerator = denumerator;
    }
    
    @Override
    public String cool_print() {

        String result = numerator.toString() + "/" + denumerator.toString();

        return result;
    }

    private int[] get_arifmetic_result(Fraction obj, String sign){
        int numerator = 0;
        if (sign == "add"){
            numerator = this.numerator*obj.denumerator + this.denumerator*obj.numerator;
        }
        else if (sign == "diff"){
            numerator = this.numerator*obj.denumerator - this.denumerator*obj.numerator;
        }
        int denumerator = this.denumerator*obj.denumerator;
        int j = Math.min(numerator, denumerator);
        for(int i = 2; i<= j ;i ++){
            while(numerator%i ==0&&denumerator%i ==0){
                numerator /= i;denumerator /= i;
            }
        }
        int[] result = new int[] {numerator, denumerator};
        return result;
    }

    @Override
    public Fraction add(Fraction obj){
        int[] result = get_arifmetic_result(obj, "add"); 
        return new Fraction(result[0], result[1]);
    }

    

    @Override
    public Fraction diff(Fraction obj){
        int[] result = get_arifmetic_result(obj, "diff"); 
        return new Fraction(result[0], result[1]);
    }

    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    
    public static int[] reduce_fraction(int a, int b) {
        int gcd = gcd(a, b);
        int[] result = new int[] {(a / gcd), (b / gcd)};
        return result;
    }


    @Override
    public Fraction mul(Fraction obj) {
        int numerator = this.numerator * obj.numerator;
        int denumerator = this.denumerator * obj.denumerator;
        int[] result = reduce_fraction(numerator, denumerator);
        return new Fraction(result[0], result[1]);
    }

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
        Lab5_8_interface element1 = new Fraction(1, 3);
        Lab5_8_interface element3;
        Fraction element2 = new Fraction(4, 5);
        element3 = element1.truediv(element2);
        System.out.println(element3.cool_print());
    }
}