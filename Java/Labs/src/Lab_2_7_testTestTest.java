import org.junit.Assert;
import org.junit.Test;


public class Lab_2_7_testTestTest {
    @Test
    public void test_main(){
        Lab2_7 object = new Lab2_7();
        int[] array = new int[]{2,5,4,6,3};

        int result = object.get_result(array);

        Assert.assertEquals(1, result);
    }
}