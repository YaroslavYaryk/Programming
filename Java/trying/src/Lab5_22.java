import java.text.ParseException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;


interface Notebook_Interaface{
    
    String get_name();
    String get_surname();
    String get_patronimic();
    String get_phone_number();
    String get_birth_date();
    int days_to_birthday(Date obj);
}

class Notebook implements Notebook_Interaface{

    String name;
    String surname;
    String patronimic;
    String phone_number;
    String birth_date;
    
    public Notebook(String name, String surname, String patronimic,
        String phone_number, String birth_date){
            this.name = name;
            this.surname = surname;
            this.patronimic = patronimic;
            this.phone_number = phone_number;
            this.birth_date = birth_date;
        }

    @Override
    public String get_name() {
        return this.name;
    }    

    @Override
    public String get_surname() {
        return this.surname;
    }

    @Override
    public String get_patronimic() {
        return this.patronimic;
    }

    @Override
    public String get_phone_number() {
        return this.phone_number;
    }

    @Override
    public String get_birth_date() {
        return this.birth_date;
    }


    
    @Override
    public int days_to_birthday(Date obj){
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd MM yyyy");

        LocalDate today = LocalDate.parse(obj.get_date(), dtf);;
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

interface Date_Interaface{
    
    public String get_date();
}

class Date implements Date_Interaface{

    String date;

    public Date(String date){
        this.date = date;
    }

    public String get_date(){
        return this.date;
    }
}


public class Lab5_22 {
    
    public static void main(String[] args) throws ParseException {
        Notebook_Interaface notebook = new Notebook("Yaroslav", "Dyhanov", 
            "Yuriyovych", "380684862861", "31 03 2003");

        Date date = new Date("20 01 2021");
        
        System.out.println("There are " + notebook.days_to_birthday(date) + " days to birhtday from '" + date.get_date() + "'" );
    }
}
