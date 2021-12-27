
interface Lab5_13_interface {

    int get_square();
    int get_perimeter();
    void set_side(int side);
    int get_side();

}

class Square implements Lab5_13_interface{
    int side;

    @Override
    public void set_side(int side) {
        if (side <= 0){
            System.out.println("Wrong side");
            System.exit(0);
        }
        this.side = side;
    }

    @Override
    public int get_side() {
        return this.side;
    }

    @Override
    public int get_perimeter() {
        return 4 * this.side;
    }
    @Override
    public int get_square() {
        return this.side * this.side;
    }

}


public class Lab5_13 {
    public static void main(String[] args) {
        Lab5_13_interface element1 = new Square();
        element1.set_side(5);
        System.out.println("Side is: " + element1.get_side());
        System.out.println("Square is: " + element1.get_square());
        System.out.println("Perimeter is: " + element1.get_perimeter());

    }    
}
