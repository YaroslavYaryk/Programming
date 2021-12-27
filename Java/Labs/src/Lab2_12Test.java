import org.junit.Assert;
import org.junit.Test;


public class Lab2_12Test {

    @Test
    public void test_main(){
        Lab2_12 object = new Lab2_12();
        int[] array = new int[]{4,3,2,4,5};

        String result = object.get_result(array);

        Assert.assertEquals("Array [4, 3, 2, 4, 5] - isn't sorted\n", result);
    }

}