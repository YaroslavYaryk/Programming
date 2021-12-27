import org.junit.Assert;
import org.junit.Test;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Lab2_22Test {
    @Test
    public void test_main(){
        Integer[] array = new Integer[]{2,4,5,1,3};
        Map<Integer, Integer> int_store = new HashMap<Integer, Integer>();
        for (int i=0; i< array.length; i++){
            int_store.put(i, array[i]);
        }
        Lab2_22 object = new Lab2_22();
        String result = Arrays.toString(object.get_result(int_store, array));

        Assert.assertEquals("[2, 1, 4, 0, 3]", result);
    }
}