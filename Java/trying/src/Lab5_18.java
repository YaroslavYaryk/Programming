
interface Lab5_18_interface {

    String get_goods();
    String get_producer();
    int get_quantity();
    String get_date_made();
    int get_shelf_life();
    String get_shipment();
    String get_shipment_number();
    String get_producer_number();
    double get_price_for_one_unit();

}

class Storage implements Lab5_18_interface{
    
    String goods;
    String producer;
    int quantity;
    String date_made;
    int shelf_life; 
    String shipment;
    String shipment_number;
    String producer_number;
    double price_for_one_unit;

    public Storage(String goods,
        String producer, int quantity,String date_made,
        int shelf_life, String shipment, String shipment_number,
        String producer_number, double price_for_one_unit){
            this.goods = goods;
            this.producer = producer;
            this.quantity = quantity;
            this.date_made = date_made;
            this.shelf_life = shelf_life;
            this.shipment = shipment;
            this.shipment_number = shipment_number;
            this.producer_number = producer_number;
            this.price_for_one_unit = price_for_one_unit;
        } 

    @Override
    public String get_goods() {
        return this.goods;
    }

    @Override
    public String get_producer() {
        return this.producer;
    }

    @Override
    public int get_quantity() {
        return this.quantity;
    }
    
    @Override
    public String get_date_made() {
        return this.date_made;
    }

    @Override
    public int get_shelf_life() {
        return this.shelf_life;
    }

    @Override
    public String get_shipment() {
        return this.shipment;
    }

    @Override
    public String get_shipment_number() {
        return this.shipment_number;
    }

    @Override
    public String get_producer_number() {
        return this.producer_number;
    }

    @Override
    public double get_price_for_one_unit() {
        return this.price_for_one_unit;
    }
}


public class Lab5_18 {
    public static void main(String[] args) {
        Lab5_18_interface element = new Storage(
            "Phone", "Xiaomi", 1, "31/03/2021", 3, "AimpCorporation", 
            "0683265896", "0965412365", 195);

        System.out.println("Goods: " + element.get_goods());
        System.out.println("Producer: " + element.get_producer());    
        System.out.println("Quantity: " + element.get_quantity());    
        System.out.println("Date made: " + element.get_date_made());    
        System.out.println("Shelf life: " + element.get_shelf_life());    


    }    
}
