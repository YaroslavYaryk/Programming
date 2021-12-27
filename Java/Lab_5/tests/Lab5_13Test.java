import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class Lab5_13Test {

    @Test
    public void main() {

        Lab5_13_interface element1 = new Square();
        element1.set_side(5);

        Assert.assertEquals(5, element1.get_side());
        Assert.assertEquals(25, element1.get_square());
        Assert.assertEquals(20, element1.get_perimeter());
    }
}