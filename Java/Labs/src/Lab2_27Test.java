import org.junit.Assert;
import org.junit.Test;

import java.util.HashMap;
import java.util.Map;


public class Lab2_27Test {

    @Test
    public void test_main(){
        int[] a = new int[]{1,2,3,4,5};
        int[] b = new int[]{3,5,6,0,9};
        Map<Integer, int[]> int_store = new HashMap<Integer, int[]>();
        Lab2_27 object = new Lab2_27();
        Map<Integer, int[]> result = object.get_result(int_store, a, b);

        Assert.assertEquals(2, result.size());
    }
}