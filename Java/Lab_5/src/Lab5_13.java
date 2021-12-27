// Создать класс Квадрат. Поля - сторона. Функции-члены вычисляют площадь, 
// периметр, устанавливает поля и возвращают значения. Функции-члены установки 
// полей класса должны проверять корректность задаваемых параметров. 


/** Interface for Square class
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
interface Lab5_13_interface {

    int get_square();
    int get_perimeter();
    void set_side(int side);
    int get_side();

}


/** class for saving Square
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
class Square implements Lab5_13_interface{
    /** property - side */
    int side;

    /** set parameters
     * @param side - side)
     */
    @Override
    public void set_side(int side) {
        if (side <= 0){
            System.out.println("Wrong side");
            System.exit(0);
        }
        this.side = side;
    }

    /** Function for getting side  {@link Square#side}
     * @return value of side
     */
    @Override
    public int get_side() {
        return this.side;
    }

    /** Function for getting perimeter according to side
     * @return perimeter according to side
     */
    @Override
    public int get_perimeter() {
        return 4 * this.side;
    }

    /** Function for getting square according to side
     * @return square according to side
     */
    @Override
    public int get_square() {
        return this.side * this.side;
    }

    @Override
    public String toString() {
        return "Square( " + side + " )";
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
