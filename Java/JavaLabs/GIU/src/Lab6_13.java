// Ввод текста в графическое окно приложения. В верхней панели (JPanel) окна 
// "Характеристики шрифта" определены следующие компоненты: надпись (JLabel) 
// "Цвет:", раскрывающееся меню  (JComboBox), в котором четыре пункта: "Черный" 
// (цвет по умолчанию),  "Красный", "Зеленый" и "Синий",  надпись (JLabel) "Размер:" 
// и три радиокнопки (JRadioButton)  с надписями: "12pt" (размер по умолчанию),  "14pt" и "16pt". 
// В нижней текстовой панели (JTextPane) "Ввод текста" окна приложения вводится текст, набираемый на клавиатуре. 
// При выборе одного из пунктов меню текст в панели выводится соответствующим цветом и/или соответствующего размера.


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;


/**
 * The class is used to store objects with the property
 * <b>textPane1</b> <b>panel1</b> <b>label1</b> <b>label2</b>
 * <b>comboBox1</b> <b>a12ptRadioButton</b> <b>a14ptRadioButton</b> <b>a16ptRadioButton</b> <b>color</b>
 *
 * @author Нфкщідфм Внрфтщм
 * @version 1.0
 */
public class Lab6_13 extends JFrame implements ActionListener {
    private JTextPane textPane1;
    private JPanel panel1;
    private JLabel label1;
    private JLabel label2;
    private JComboBox comboBox1 ;
    private JRadioButton a12ptRadioButton;
    private JRadioButton a14ptRadioButton;
    private JRadioButton a16ptRadioButton;
    protected String[] color = new String[]{"Чорний", "Червоний", "Зелений", "Синій"};
    protected Font font;
    protected Color style =  Color.BLACK;
    String style1 = "Arial";

    /**
     * constructor for creating all fields
     */
    public Lab6_13(){
        super("Text Editor");
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        textPane1 = new JTextPane();
        panel1 = new JPanel();
        label1 = new JLabel();
        label2 = new JLabel();
        comboBox1 = new JComboBox();
        a12ptRadioButton = new JRadioButton();
        a14ptRadioButton = new JRadioButton();
        a16ptRadioButton = new JRadioButton();
        font = new Font(style1, Font.PLAIN, 12);

        panel1.setBorder(BorderFactory.createTitledBorder("Характеристики шрифта"));
        label1.setText("Цвет:");
        panel1.add(label1);
        comboBox1.setModel(new DefaultComboBoxModel(color));
        comboBox1.setSelectedIndex(0);
        panel1.add(comboBox1);

        label2.setText("Размер:");
        panel1.add(label2);
        a12ptRadioButton.setText("12pt");
        panel1.add(a12ptRadioButton);
        a14ptRadioButton.setText("14pt");
        panel1.add(a14ptRadioButton);
        a16ptRadioButton.setText("16pt");
        panel1.add(a16ptRadioButton);

        textPane1.setFont(font);
        textPane1.setBorder(BorderFactory.createTitledBorder("Ввід тексту"));

        add(textPane1);
        add(panel1,BorderLayout.NORTH);
        pack();
        setSize(600, 600);

        a12ptRadioButton.addActionListener(e -> {
            textPane1.setFont(new Font(style1, Font.PLAIN, 12));
            a14ptRadioButton.setSelected(false);
            a16ptRadioButton.setSelected(false);
        });

        a14ptRadioButton.addActionListener(e -> {
            textPane1.setFont(new Font(style1, Font.PLAIN, 14));
            a12ptRadioButton.setSelected(false);
            a16ptRadioButton.setSelected(false);
        });

        a16ptRadioButton.addActionListener(e -> {
            textPane1.setFont(new Font(style1, Font.PLAIN, 16));
            a14ptRadioButton.setSelected(false);
            a12ptRadioButton.setSelected(false);
        });

        comboBox1.setActionCommand("color");
        comboBox1.addActionListener(this);

        this.setVisible(true);
    }

    /**
     * Method for action clicking on combobox
     *
     * @param e - event
     */
    public void actionPerformed(ActionEvent e) {
        String command = e.getActionCommand();
        if(command.equals("color")) {
            String st = Objects.requireNonNull(comboBox1.getSelectedItem()).toString();
            if (st.equals("Чорний"))
                style = Color.BLACK;
            if (st.equals("Червоний"))
                style = Color.RED;
            if (st.equals("Зелений"))
                style = Color.GREEN;
            if (st.equals("Синій"))
                style = Color.BLUE;            
            textPane1.setForeground(style);
        }
    }

    /**
     * Method for starting program and create an app with panels
     *
     * @param args - that we can give with console usage
     */
    public static void main(String[] args) {
        new Lab6_13();
    }
}