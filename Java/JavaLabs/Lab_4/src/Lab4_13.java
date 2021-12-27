// Создайте приложение для изменения  абонента телефонной сети. 
// Список абонентов (5 записей) создается в программе и является 
// объектом класса HashMap. Ключом записи является номер телефона 
// (типа Integer), а значением – объект Abonent, содержащий четыре 
// значения типа String:  фамилию, имя, отчество и адрес. Предусмотреть 
// возможность сортировки по фамилии с помощью ArrayList.



import java.util.*;

public class Lab4_13 {
    static class Abonent implements Comparable<Abonent>{
        String name;
        String surname;
        String patronymic;
        String address;
        public Abonent(String name, String surname, String patronymic, String address){
            this.name = name;
            this.surname = surname;
            this.patronymic = patronymic;
            this.address = address;
        }

        @Override
        public int compareTo(Abonent o){
            return this.surname.compareTo(o.surname);
        }
        public String toString(){
            return String.join(" ", name, surname, patronymic, address);
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

    public static void print_sorted(List<Abonent> inp, Map <Integer, Abonent> phonebook){
        Collections.sort(inp);
        for(Abonent s: inp){
            System.out.print(s + "  ");
            System.out.printf("Number: %d\n", getKeyByValue(phonebook, s));
        }
    }

    public static void change_abonent(Map <Integer, Abonent> phonebook){
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter phone number whose owner you want to change:");
        int num = scan.nextInt();
        if(phonebook.containsKey(num)){
            Abonent obj = phonebook.get(num);
            scan.nextLine();
            System.out.println("Enter new name:");
            obj.name = scan.nextLine();
            System.out.println("Enter new surname:");
            obj.surname = scan.nextLine();
            System.out.println("Enter new patronymic:");
            obj.patronymic = scan.nextLine();
            System.out.println("Enter new address:");
            obj.address = scan.nextLine();
        }
        else{System.out.println("Number not in phonebook!");}

        scan.close();
    }

    public static void main(String[] args){
        Abonent obj1 = new Abonent("Yaroslav", "Dyhanov", "Yuriyovych", "Volodymyrets");
        Abonent obj2 = new Abonent("Yarosla", "Dyhano", "Yuriyovy", "Volodymyre");
        Abonent obj3= new Abonent("Yarosl", "Dyhan", "Yuriyov", "Volodymyr");
        Abonent obj4 = new Abonent("Yaros", "Dyha", "Yuriyo", "Volodymy");
        Abonent obj5 = new Abonent("Yaro", "Dyh", "Yuriyh", "Volodym");
        Map<Integer, Abonent> phonebook = new HashMap<>();
        phonebook.put(1, obj1);
        phonebook.put(2, obj2);
        phonebook.put(3, obj3);
        phonebook.put(4, obj4);
        phonebook.put(5, obj5);
        // change_abonent(phonebook);
        ArrayList<Abonent> sorted = new ArrayList<>(phonebook.values());
        System.out.println("Sorted:");
        print_sorted(sorted, phonebook);
    }
}
