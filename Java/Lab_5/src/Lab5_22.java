// Создать класс «Дата» и класс - «Записная книжка», включающий ФИО, телефон, 
// дату рождения и функцию вычисления количества дней до дня рождения.


import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

/** Interface for Notebook class
 * @author Dyhanov Yaroslav
 * @version 1.0
 */

interface Notebook_Interaface{

    String get_name();
    String get_surname();
    String get_patronimic();
    String get_phone_number();
    String get_birth_date();
    int days_to_birthday(Date obj);
}

/** class  for saving Notebook
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
class Notebook implements Notebook_Interaface{
    /** property - name */
    String name;
    /** property - surname */
    String surname;
    /** property - patronimic */
    String patronimic;
    /** property - phone_number */
    String phone_number;
    /** property - birth_date */
    String birth_date;

    /** Create new Notebook object with this values
     * @param name - name
     * @param surname - surname
     * @param patronimic - patronimic
     * @param phone_number - birth_date
     */
    public Notebook(String name, String surname, String patronimic,
                    String phone_number, String birth_date){
        this.name = name;
        this.surname = surname;
        this.patronimic = patronimic;
        this.phone_number = phone_number;
        this.birth_date = birth_date;
    }

    @Override
    public String toString() {
        return "Notebook( " + name + ", " + surname + ", " + patronimic + " )";
    }

    /** function for getting  name {@link Notebook#name}
     * @return goods name
     */
    @Override
    public String get_name() {
        return this.name;
    }

    /** function for getting  surname {@link Notebook#surname}
     * @return goods surname
     */
    @Override
    public String get_surname() {
        return this.surname;
    }

    /** function for getting patronimic {@link Notebook#patronimic}
     * @return goods patronimic
     */
    @Override
    public String get_patronimic() {
        return this.patronimic;
    }

    /** function for getting phone_number {@link Notebook#phone_number}
     * @return goods phone_number
     */
    @Override
    public String get_phone_number() {
        return this.phone_number;
    }

    /** function for getting birth_date {@link Notebook#birth_date}
     * @return goods name
     */
    @Override
    public String get_birth_date() {
        return this.birth_date;
    }

    /** Returns days to birthday
     * @param obj - date object
     @return days to birthday according to date
     */
    @Override
    public int days_to_birthday(Date obj){
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd MM yyyy");

        LocalDate today = LocalDate.parse(obj.get_date(), dtf);
//      String today2 = (dtf.format(LocalDateTime.now()));
//      LocalDate today = LocalDate.parse(today2, dtf);
        LocalDate birthday = LocalDate.parse(this.birth_date, dtf);

        LocalDate nextBDay = birthday.withYear(today.getYear());

        //If your birthday has occurred this year already, add 1 to the year.
        if (nextBDay.isBefore(today) || nextBDay.isEqual(today)) {
            nextBDay = nextBDay.plusYears(1);
        }

        long daysBetween = ChronoUnit.DAYS.between(today, nextBDay);
        return Math.toIntExact(daysBetween);
    }
}

/** Interface for Date class
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
interface Date_Interaface{
    String get_date();
}

/** class for saving Date
 * @author Dyhanov Yaroslav
 * @version 1.0
 */
class Date implements Date_Interaface{
    /** property - date */
    String date;

    /** Create new Date object with this values
     * @param date - date
     */
    public Date(String date){
        this.date = date;
    }

    @Override
    public String toString() {
        return String.format("Date( " + date + " )");
    }

    /** function for getting date {@link Date#date}
     * @return date
     */
    @Override
    public String get_date(){
        return this.date;
    }
}


public class Lab5_22 {

    public static void main(String[] args) {
        Notebook_Interaface notebook = new Notebook("Yaroslav", "Dyhanov",
                "Yuriyovych", "380684862861", "31 03 2003");

        Date date = new Date("20 01 2021");

        System.out.println("There are " + notebook.days_to_birthday(date) + " days to birhtday from '" + date.get_date() + "'" );
    }
}
