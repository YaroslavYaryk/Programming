import org.junit.Assert;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import static org.junit.Assert.*;

public class Lab4_18Test {
    private final ByteArrayOutputStream output = new ByteArrayOutputStream();

    @Test
    public void test_main(){

        Lab4_18.Book obj1 = new Lab4_18.Book("Book1", "Yaroslav", "Dyhanov", "Yuriyovych", "Volodymyrets", 2020, 5.55f);
        Lab4_18.Book obj2 = new Lab4_18.Book("Book2", "Yarosla", "Dyhano", "Yuriyovyc", "Volodymyret", 1020, 2.55f);
        Lab4_18.Book obj3= new Lab4_18.Book("Book3", "Yarosl", "Dyhan", "Yuriyovy", "Volodymyre", 2021, 5.1f);
        Lab4_18.Book obj4 = new Lab4_18.Book("Book4", "Yaros", "Dyha", "Yuriyov", "Volodymyr", 202, 1.55f);
        Lab4_18.Book obj5 = new Lab4_18.Book("Book5", "Yaro", "Dyh", "Yuriyo", "Volodymy", 2220, 4.55f);
        Map<Integer, Lab4_18.Book> book_store = new HashMap<>();
        book_store.put(1, obj1);
        book_store.put(2, obj2);
        book_store.put(3, obj3);
        book_store.put(4, obj4);
        book_store.put(5, obj5);
        // change_book_price(book_store);
        ArrayList<Lab4_18.Book> sorted = new ArrayList<>(book_store.values());
        sorted.sort(new Lab4_18.PriceComparator());

        PrintStream old = System.out;
        System.setOut(new PrintStream(output));
        Lab4_18.print_sorted(sorted, book_store);
        Assert.assertEquals(output.toString(), "Yaros Dyha 1.55  Number: 4\n" +
        "Yarosla Dyhano 2.55  Number: 2\n" +
        "Yaro Dyh 4.55  Number: 5\n" +
        "Yarosl Dyhan 5.1  Number: 3\n" +
        "Yaroslav Dyhanov 5.55  Number: 1\n");
        System.setOut(old);
    }
}