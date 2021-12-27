import java.util.ArrayList;

import org.junit.Assert;
import org.junit.Test;

public class Lab4_22Test {

    @Test
    public void test_main(){
        ArrayList<Integer> array = new ArrayList<>();
        array.add(1);
        array.add(2);
        array.add(3);
        array.add(2);
        array.add(5);

        int result = Lab4_22.get_index_by_element(array, 3, 1);

        Assert.assertEquals(2, result);
    }
}

