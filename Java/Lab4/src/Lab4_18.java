// Создайте приложение для просмотра списка книг в
// библиотечном каталоге и изменения цены книги.
// Список книг (5 записей) создается в программе и
// является объектом класса HashMap. Ключом записи
// является индекс ISBN книги (типа Integer), а
// значением – объект Book, содержащий наименование
// книги, ФИО автора, издательство (все записи типа
// String), год издания (типа int) и цену книги
// (типа float). Предусмотреть возможность сортировки
// книг по издательству или цене, используя ArrayList.


import java.util.*;

public class Lab4_18 {

    static class Book{
        String name;
        String author_name;
        String author_surname;
        String author_patronymic;
        String publishing;
        int year;
        float price;

        public Book(String name, String author_name, String author_surname,
                    String author_patronymic, String publishing ,int year, float price){
            this.name = name;
            this.author_name = author_name;
            this.author_surname = author_surname;
            this.author_patronymic = author_patronymic;
            this.publishing = publishing;
            this.year = year;
            this.price = price;
        }

    }

    static class PriceComparator implements Comparator<Book>{
        @Override
        public int compare(Book obj1, Book obj2){
            return Float.compare(obj1.price, obj2.price);
        }
    }

    static class PublishingComparator implements Comparator<Book>{
        @Override
        public int compare(Book obj1, Book obj2){
            return obj1.publishing.compareTo(obj2.publishing);
        }
    }


    public static <T, E> T getKeyByValue(Map<T, E> map, E value) {
        for (Map.Entry<T, E> entry : map.entrySet()) {
            if (Objects.equals(value, entry.getValue())) {
                return entry.getKey();
            }
        }
        return null;
    }

    public static void print_sorted(List<Book> inp, Map <Integer, Book> phonebook){
        for(Book s: inp){
            System.out.print(s.author_name + " " + s.author_surname + " " + s.price + "  ");
            System.out.printf("Number: %d\n", getKeyByValue(phonebook, s));
        }
    }

    public static void change_book_price(Map <Integer, Book> book_store){
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter book number that price you want to change:");
        int num = scan.nextInt();
        if(book_store.containsKey(num)){
            Book obj = book_store.get(num);
            scan.nextLine();
            System.out.println("Enter new price:");
            obj.price = scan.nextFloat();

        }
        else{System.out.println("Number not in book_store!");}

        scan.close();
    }
    public static void main(String[] args){
        Book obj1 = new Book("Book1", "Yaroslav", "Dyhanov", "Yuriyovych", "Volodymyrets", 2020, 5.55f);
        Book obj2 = new Book("Book2", "Yarosla", "Dyhano", "Yuriyovyc", "Volodymyret", 1020, 2.55f);
        Book obj3= new Book("Book3", "Yarosl", "Dyhan", "Yuriyovy", "Volodymyre", 2021, 5.1f);
        Book obj4 = new Book("Book4", "Yaros", "Dyha", "Yuriyov", "Volodymyr", 202, 1.55f);
        Book obj5 = new Book("Book5", "Yaro", "Dyh", "Yuriyo", "Volodymy", 2220, 4.55f);
        Map<Integer, Book> book_store = new HashMap<>();
        book_store.put(1, obj1);
        book_store.put(2, obj2);
        book_store.put(3, obj3);
        book_store.put(4, obj4);
        book_store.put(5, obj5);
        // change_book_price(book_store);
        ArrayList<Book> sorted = new ArrayList<>(book_store.values());
        sorted.sort(new PriceComparator());
        System.out.println("Sorted by name:");
        print_sorted(sorted, book_store);
        sorted.sort(new PublishingComparator());
        System.out.println("Sorted by surname:");
        print_sorted(sorted, book_store);

    }
}
