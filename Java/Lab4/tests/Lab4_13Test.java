import org.junit.Assert;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.*;

public class Lab4_13Test {
    private final ByteArrayOutputStream output = new ByteArrayOutputStream();

    @Test
    public void test_main(){

        Lab4_13.Abonent obj1 = new Lab4_13.Abonent("Yaroslav", "Dyhanov", "Yuriyovych", "Volodymyrets");
        Lab4_13.Abonent obj2 = new Lab4_13.Abonent("Yarosla", "Dyhano", "Yuriyovy", "Volodymyre");
        Lab4_13.Abonent obj3= new Lab4_13.Abonent("Yarosl", "Dyhan", "Yuriyov", "Volodymyr");
        Lab4_13.Abonent obj4 = new Lab4_13.Abonent("Yaros", "Dyha", "Yuriyo", "Volodymy");
        Lab4_13.Abonent obj5 = new Lab4_13.Abonent("Yaro", "Dyh", "Yuriyh", "Volodym");
        Map<Integer, Lab4_13.Abonent> phonebook = new HashMap<>();
        phonebook.put(1, obj1);
        phonebook.put(2, obj2);
        phonebook.put(3, obj3);
        phonebook.put(4, obj4);
        phonebook.put(5, obj5);
        // change_abonent(phonebook);
        ArrayList<Lab4_13.Abonent> sorted = new ArrayList<>(phonebook.values());

        PrintStream old = System.out;
        System.setOut(new PrintStream(output));
        Lab4_13.print_sorted(sorted, phonebook);
        Assert.assertEquals(output.toString(), "Yaro Dyh Yuriyh Volodym  Number: 5\n" +
        "Yaros Dyha Yuriyo Volodymy  Number: 4\n" +
        "Yarosl Dyhan Yuriyov Volodymyr  Number: 3\n" +
        "Yarosla Dyhano Yuriyovy Volodymyre  Number: 2\n" +
        "Yaroslav Dyhanov Yuriyovych Volodymyrets  Number: 1\n");
        System.setOut(old);
    }
}