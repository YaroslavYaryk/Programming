import org.junit.Assert;
import org.junit.Test;
import java.util.*;

public class Lab2_17Test {
    @Test
    public void test_main(){
        Lab2_17 object = new Lab2_17();
        int[] array = new int[]{2,1,3,4,5};

        String result = Arrays.toString(object.get_difference_array(array));

        Assert.assertEquals("[3, 4, 2, 1, 0]",result);
    }
}