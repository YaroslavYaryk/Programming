import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class Lab5_18Test {

    @Test
    public void main() {

        Lab5_18_interface element = new Storage(
                "Phone", "Xiaomi", 1, "31/03/2021", 3, "AimpCorporation",
                "0683265896", "0965412365", 195);


        Assert.assertEquals("Phone", element.get_goods());
        Assert.assertEquals("Xiaomi", element.get_producer());
        Assert.assertEquals(1, element.get_quantity());
        Assert.assertEquals("31/03/2021", element.get_date_made());
        Assert.assertEquals(3, element.get_shelf_life());

    }
}