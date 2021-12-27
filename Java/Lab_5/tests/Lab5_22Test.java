import org.junit.Assert;
import org.junit.Test;

import static org.junit.Assert.*;

public class Lab5_22Test {

    @Test
    public void main() {

        Notebook_Interaface notebook = new Notebook("Yaroslav", "Dyhanov",
                "Yuriyovych", "380684862861", "31 03 2003");

        Date date = new Date("20 01 2021");

        String result = "There are " + notebook.days_to_birthday(date) + " days to birhtday from '" + date.get_date() + "'" ;
        String expected_result = "There are 70 days to birhtday from '20 01 2021'";
        Assert.assertEquals(expected_result, result);
    }
}