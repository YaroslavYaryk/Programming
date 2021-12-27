// Вывод фигур в графическом окне. В окне определена строка меню  
// (JMenuBar), в которой определены два меню (JMenu)  – "Цвет и "Вывод". 
// В меню "Цвет" определены четыре пункта меню (JRadioButtonMenuItem): "Черный" 
// (цвет по умолчанию),  "Красный", "Зеленый" и "Синий".  В меню "Вывод" определены 
// три пункта меню (JCheckBoxMenuItem): "Квадрат",  "Круг",  и "Треугольник". В верней 
// панели окна панели (JPanel) окна выводятся в графическом контексте (с помощью методов 
// drawRect(), drawOval() и drawPolygon()) три фигуры: прямоугольник, круг и треугольник. В 
// нижней панели (JPanel) "Управление выводом" задается надпись (JLabel) "Цвет:", раскрывающееся 
// меню  (JComboBox), в котором определены четыре пункта: "Черный" (цвет по умолчанию),  
// "Красный", "Зеленый" и "Синий", надпись (JLabel) "Вывод:" и три переключателя (JCheckBox): 
// "Квадрат",  "Круг",  и "Треугольник". При выборе пункта раскрывающегося меню все  фигуры 
// заполняются заданным цветом. На экран выводятся только те фигуры, переключатели которых включены


import java.awt.*;
import java.awt.geom.Ellipse2D;
import java.awt.event.*;
import javax.swing.*;


/**
 * The class is used to store objects with the property
 * <b>color</b> 
 *
 * @author aDyhanov Yaroslav
 * @version 1.0
 */
class Colorize {
    String color;

    Colorize(String color) {
        this.color = color;
    }

    /**
     * Method for getting color according to instance
     *
     */
    public Color get_color() {
        if (color == "RED") {
            return Color.RED;
        }
        if (color == "GREEN") {
            return Color.GREEN;
        }
        if (color == "BLUE") {
            return Color.BLUE;
        }
        return Color.BLACK;
    }
}


/**
 * The class is used to store objects with the property
 * <b>color</b> <b>rectangle</b> <b>oval</b> <b>polygon</b>
 *
 * @author aDyhanov Yaroslav
 * @version 1.0
 */
class Surface extends JPanel {

    Color color;
    boolean rectangle, oval, polygon;

    /**
     * constructor for initialization objects
     *
     * @param color - color
     * @param rectangle - rectangle
     * @param oval - oval
     * @param polygon - polygon
     */
    public Surface(String color, boolean rectangle, boolean oval, boolean polygon) {
        Colorize color_type = new Colorize(color);
        this.color = color_type.get_color();
        this.rectangle = rectangle;
        this.oval = oval;
        this.polygon = polygon;
    }

    /**
     * method for drawing rectangle
     *
     * @param g - graphic object
     */
    protected void drawRect(Graphics g) {

        Graphics2D g2d = (Graphics2D) g;

        g2d.fillRect(100, 10, 50, 50);
    }

    /**
     * method for drawing oval
     *
     * @param g - graphic object
     */
    protected void drawOval(Graphics g) {

        Graphics2D g2d = (Graphics2D) g;

        g2d.fill(new Ellipse2D.Double(200, 10, 50, 50));
    }

    /**
     * method for drawing polygon
     *
     * @param g - graphic object
     */
    protected void drawPolygon(Graphics g) {

        Graphics2D g2d = (Graphics2D) g;

        g2d.fillPolygon(new int[] { 30, 70, 0 }, new int[] { 0, 70, 70 }, 3);
    }

    @Override
    public void paintComponent(Graphics g) {

        super.paintComponent(g);

        g.setColor(color);
        if (rectangle)
            drawRect(g);
        if (oval)
            drawOval(g);
        if (polygon)
            drawPolygon(g);
    }
}

/**
 * The class is used to store objects with the property
 * <b>color</b> <b>rectangle</b> <b>oval</b> <b>polygon</b> <b>frame</b>
 *
 * @author aDyhanov Yaroslav
 * @version 1.0
 */
class NewWindow {
    JFrame frame = new JFrame();
    String color;
    boolean rectangle, oval, polygon;

    /**
     * constructor for initialization objects
     */
    NewWindow(String color, boolean rectangle, boolean oval, boolean polygon) {
        this.color = color;
        Surface new_surf = new Surface(color, rectangle, oval, polygon);
        frame.setBounds(600, 200, 500, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.add(new_surf);

    }
}

/**
 * The class is used to store objects with the property
 * <b>button</b> <b>black</b> <b>green</b> <b>red</b>
 * <b>blue</b> <b>rect_check</b> <b>oval_check</b> <b>polygon_check</b>
 * @author aDyhanov Yaroslav
 * @version 1.0
 */
public class Lab6_8 extends JFrame {

    private JButton button = new JButton("press");
    private JRadioButtonMenuItem black = new JRadioButtonMenuItem("black", true);
    private JRadioButtonMenuItem red = new JRadioButtonMenuItem("red");
    private JRadioButtonMenuItem green = new JRadioButtonMenuItem("green");
    private JRadioButtonMenuItem blue = new JRadioButtonMenuItem("blue");

    private JCheckBoxMenuItem rect_check = new JCheckBoxMenuItem("rectangle", true);
    private JCheckBoxMenuItem oval_check = new JCheckBoxMenuItem("oval", true);
    private JCheckBoxMenuItem polygon_check = new JCheckBoxMenuItem("polygon", true);

    private JCheckBoxMenuItem rect_check_down = new JCheckBoxMenuItem("rectangle", false);
    private JCheckBoxMenuItem oval_check_down = new JCheckBoxMenuItem("oval", false);
    private JCheckBoxMenuItem polygon_check_down = new JCheckBoxMenuItem("polygon", false);

    static JFrame f;

    // JButton
    static JButton b, b1, b2;

    // Label to display text
    static JLabel l;

    private JMenuBar mb;
    private JMenu color_menu, output_menu;

    public Lab6_8() {
        mb = new JMenuBar();
        color_menu = new JMenu("Color");
        output_menu = new JMenu("Output");
        setTitle("Basic shapes");
        this.setBounds(600, 200, 500, 300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Container container = this.getContentPane();
        container.setLayout(new GridLayout(3, 4, 10, 10));

        container.add(new Surface("BLACK", true, true, true));
        ButtonGroup group = new ButtonGroup();
        group.add(black);
        group.add(red);
        group.add(green);
        group.add(blue);

        color_menu.add(black);
        color_menu.add(red);
        color_menu.add(green);
        color_menu.add(blue);

        output_menu.add(rect_check);
        output_menu.add(oval_check);
        output_menu.add(polygon_check);

        mb.add(color_menu);
        mb.add(output_menu);

        setJMenuBar(mb);
        button.addActionListener(new ButtonEventListener());
        container.add(button);
        String[] values = { "BLACK", "GREEN", "RED", "BLUE" };
        l = new JLabel("Color:");
        JComboBox combobox = new JComboBox(values);
        combobox.setSelectedItem(1);
        combobox.addActionListener(new ComboboxEventListener());
        // Creating a panel to add buttons
        JPanel p = new JPanel();
        // Adding buttons and textfield to panel
        // using add() method
        p.add(l);
        p.add(combobox);
        p.add(rect_check_down);
        p.add(oval_check_down);
        p.add(polygon_check_down);

        container.add(p);
    }

        /**
     * The class is used to act on clicking button
     * @author aDyhanov Yaroslav
     * @version 1.0
     */
    class ButtonEventListener implements ActionListener {

        public void actionPerformed(ActionEvent e) {
            String color = "";
            if (black.isSelected()) {
                color = "BLACK";
            }
            if (red.isSelected()) {
                color = "RED";
            }
            if (green.isSelected()) {
                color = "GREEN";
            }
            if (blue.isSelected()) {
                color = "BLUE";
            }
            boolean rectangle = false;
            boolean oval = false;
            boolean polygon = false;
            if (rect_check.isSelected()) {
                rectangle = true;
            }
            if (oval_check.isSelected()) {
                oval = true;
            }
            if (polygon_check.isSelected()) {
                polygon = true;
            }
            if (e.getSource() == button) {
                NewWindow myNewWindow = new NewWindow(color, rectangle, oval, polygon);
            }
        }
    }

     /**
     * The class is used to act on clicking combobox
     * @author aDyhanov Yaroslav
     * @version 1.0
     */
    class ComboboxEventListener implements ActionListener {

        public void actionPerformed(ActionEvent e) {

            JComboBox combobox = (JComboBox) e.getSource();
            String color = (String) combobox.getSelectedItem();
            System.out.println(color);
            boolean rectangle = false;
            boolean oval = false;
            boolean polygon = false;
            if (rect_check_down.isSelected()) {
                rectangle = true;
            }
            if (oval_check_down.isSelected()) {
                oval = true;
            }
            if (polygon_check_down.isSelected()) {
                polygon = true;
            }
            NewWindow myNewWindow = new NewWindow(color, rectangle, oval, polygon);

        }
    }

     /**
     * Method for starting program and create an app with panels and painting part
     *
     * @param args - that we can give with console usage
     */
    public static void main(String[] args) {

        EventQueue.invokeLater(new Runnable() {

            @Override
            public void run() {
                Lab6_8 ex = new Lab6_8();
                ex.setVisible(true);
            }
        });
    }
}