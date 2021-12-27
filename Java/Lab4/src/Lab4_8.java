/*
Создайте приложение для просмотра списка очередников и изменения приоритета очередников в очереди. Список  (5 записей)
создается в программе и является объектом класса LinkedList. Запись списка является объектом QueuePerson, содержащим
поля фамилии, имени и отчества очередника (типа String), поле типа AddressValue для адреса очередника и приоритет очередника
(типа int). В свою очередь, поле типа AddressValue содержит три поля типа String: наименование города, наименование улицы и
номер дома, а также поле типа int – номер квартиры (если номер квартиры равен 0, дом, в котором проживает очередник, не имеет
квартир). Записи в очереди сортируются в соответствии с приоритетом, и очередник добавляется последним в очереди приоритета.
 */

import javax.management.BadAttributeValueExpException;
import java.util.*;

public class Lab4_8 {
    public static void main(String[] args) {
        try {
            Map<Integer, Boolean> queue_status = new HashMap<>();

            QueuePerson person1 = new QueuePerson("Dyhanov", "Yaroslav", "Yuriy", new AddressValue("Volodymyrets", "Osvitianska", 5, 0, 1));
            QueuePerson person2 = new QueuePerson("Plisiuk", "Nazar", "Val", new AddressValue("Ovadne", "Molodizhna", 20, 0, 2));
            QueuePerson person3 = new QueuePerson("Subitskiy", "Pavlo", "Rom", new AddressValue("Ovadne", "Molodizhna", 90, 5, 3));
            QueuePerson person4 = new QueuePerson("Karpiuk", "Alina", "Olex", new AddressValue("Lutsk", "Nova", 55, 9, 4));
            QueuePerson person5 = new QueuePerson("Mankut", "Maksim", "Vik", new AddressValue("Lutsk", "Nevidoma", 19, 99, 6));
            LinkedList<QueuePerson> queue = new LinkedList<>();

            queue.add(person1); queue_status.put(person1.address.get_priority(), true);
            queue.add(person2); queue_status.put(person2.address.get_priority(), false);
            queue.add(person3); queue_status.put(person3.address.get_priority(), true);
            queue.add(person4); queue_status.put(person4.address.get_priority(), true);
            queue.add(person5); queue_status.put(person5.address.get_priority(), true);

            boolean isContinue = true;
            int i;
            Scanner in = new Scanner(System.in);

            while (isContinue){
                System.out.println("1 - watch a queue | 2 - add person | 3 - change priority for person | 4 - exit");
                i = in.nextInt();
                switch (i){
                    case 1:
                        for(QueuePerson p : queue)
                            System.out.println(p.get_full_name() + ". Address: " + p.address.get_full_address() + ". Priority: " + p.address.get_priority());
                        break;
                    case 2:
                        QueuePerson p = new QueuePerson();
                        boolean isCorrect = false;
                        while (!isCorrect){
                            System.out.print("Enter a priority: ");
                            int new_priority = in.nextInt();
                            if(queue_status.get(new_priority) != null && queue_status.get(new_priority)){
                                System.out.println("Priority is not fee! Please try again.");
                                continue;
                            }
                            p.address.change_priority(new_priority);
                            queue_status.put(p.address.get_priority(), true);
                            isCorrect = true;
                        }
                        queue.add(p);
                        Collections.sort(queue, Comparator.comparingInt(obj -> obj.address.get_priority()));
                        break;
                    case 3:
                        System.out.print("Enter a full name of person: ");
                        in.nextLine();
                        String full_name = in.nextLine();
                        for(QueuePerson pr : queue){
                            if(pr.get_full_name().equals(full_name)){
                                in.nextLine();
                                System.out.print("Enter a new priority: ");
                                int new_priority = in.nextInt();
                                if(queue_status.get(new_priority) != null && queue_status.get(new_priority)){
                                    System.out.println("Priority is not free! Please try again.");
                                    break;
                                }
                                pr.address.change_priority(new_priority);
                                queue_status.put(pr.address.get_priority(), true);
                                break;
                            }
                        }
                        Collections.sort(queue, Comparator.comparingInt(obj -> obj.address.get_priority()));
                        break;
                    case 4:
                        isContinue = false;
                        break;
                    default:
                        System.out.println("Wrong input");
                }
            }
        }catch (Exception ex) {
            System.out.println(ex);
        }
    }

}


class QueuePerson{
    String surname;
    String name;
    String patronymic;
    AddressValue address;
    public QueuePerson(String surname, String name, String patronymic, AddressValue address) {
        this.surname = surname;
        this.name = name;
        this.patronymic = patronymic;
        this.address = address;
    }
    public QueuePerson(){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a surname: ");
        this.surname = in.nextLine();
        System.out.print("Enter a name: ");
        this.name = in.nextLine();
        System.out.print("Enter a patronymic: ");
        this.patronymic = in.nextLine();
        this.address = new AddressValue();
    }

    public String get_full_name(){
        return this.surname + " " + this.name + " " + this.patronymic;
    }
}

class AddressValue{
    String city;
    String street;
    int house;
    int flat;
    int priority;
    public AddressValue(String city, String street, int house, int flat, int priority){
        this.city = city;
        this.street = street;
        this.house = house;
        this.flat = flat;
        this.priority = priority;
    }
    public AddressValue(){
        Scanner in = new Scanner(System.in);
        System.out.print("Enter a city: ");
        this.city = in.nextLine();
        System.out.print("Enter a street: ");
        this.street = in.nextLine();
        System.out.print("Enter a house: ");
        this.house = in.nextInt();
        System.out.print("Enter a flat: ");
        this.flat = in.nextInt();
        this.priority = 0;
    }
    public int get_priority(){
        return this.priority;
    }
    public String get_full_address(){
        if(this.flat != 0)
            return this.city + " " + this.street + " " + this.house + " " + this.flat;
        return this.city + " " + this.street + " " + this.house;
    }
    public void change_priority(int priority) throws BadAttributeValueExpException{
        if(priority <= 0)
            throw new BadAttributeValueExpException("Priority must be more then 0");
        this.priority = priority;
    }
}
