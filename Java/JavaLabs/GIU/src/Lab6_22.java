/*22.	Изменение надписи в графическом окне.
    В центре верхней панели (JPanel) "Вывод надписи" в графическом контексте
    выводится (с помощью метода drawString()) произвольная надпись.
    В нижней панели (JPanel) "Параметры надписи" задаются следующие компоненты:
    надпись (JLabel) "Текст:", текстовое поле   (JTextField), надпись (JLabel)  "Цвет:",
    четыре радиокнопки (JRadioButton) со значениями: "Черный" (цвет по умолчанию),
    "Красный", "Зеленый" и "Синий", вращающийся список (JLabel) "Размер:",
    три радиокнопки (JRadioButton) со значениями: "10pt",  "12pt" (размер по умолчанию)
    и "14pt", надпись (JLabel) "Координата X:", текстовое поле   (JTextField),
    надпись (JLabel) "Координата Y:", текстовое поле   (JTextField),
    а также кнопка (JButton) "Вывести строку". Первоначально в текстовых полях
    "Координата X:" и "Координата Y:" устанавливаются координаты начала базовой линии надписи
    (текстовые поля заданы как нередактируемые). При вводе данных надпись меняет текст,
    цвет и/или размер. При щелчке мышью в области верхней панели в текстовых полях выводятся
    координаты точки щелчка и надпись перерисовывается в этой точке.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;


/**
 * The class is used to store objects with the property
 * <b>topPanel</b> <b>botPanel</b> <b>labelText</b> <b>labelColor</b> <b>labelSize</b> <b>labelX</b> <b>labelY</b>
 * <b>textField</b> <b>xField</b> <b>yField</b> <b>color</b> <b>font</b>
 * <b>button</b> <b>x</b> <b>y</b> <b>color</b> <b>font</b>
 * @author aDyhanov Yaroslav
 * @version 1.0
 */
public class Lab6_22 extends JFrame {
    JPanel topPanel, botPanel;
    JLabel labelText = new JLabel("Текст:");
    JLabel labelColor = new JLabel("Цвет:");
    JLabel labelSize = new JLabel("Размер:");
    JLabel labelX = new JLabel("Координата Х:");
    JLabel labelY = new JLabel("Координата Y:");
    JTextField textField, xField, yField;
    JRadioButton black, red, green, blue, pt10, pt12, pt14;
    Color color;
    Font font;
    JButton button = new JButton("Вивестри напис");
    int x = 100, y = 100;

    /**
     * constructor for creating all fields
     */
    public Lab6_22 () {
        super("Lab6_22");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1600, 500);
        setVisible(true);

        textField = new JTextField("Введіть текст",10);
        xField = new JTextField(Integer.toString(x),3);
        yField = new JTextField(Integer.toString(y),3);
        black = new JRadioButton("Чорний", true);
        red = new JRadioButton("Червоний");
        green = new JRadioButton("Зелений");
        blue = new JRadioButton("Синій");
        ButtonGroup buttonGroup = new ButtonGroup();
        buttonGroup.add(black);
        buttonGroup.add(red);
        buttonGroup.add(green);
        buttonGroup.add(blue);
        pt10 = new JRadioButton("10pt");
        pt12 = new JRadioButton("12pt", true);
        pt14 = new JRadioButton("14pt");
        ButtonGroup buttonGroup1 = new ButtonGroup();
        buttonGroup1.add(pt10);
        buttonGroup1.add(pt12);
        buttonGroup1.add(pt14);
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (black.isSelected()) color = Color.BLACK;
                else if (red.isSelected()) color = Color.RED;
                else if (green.isSelected()) color = Color.GREEN;
                else if (blue.isSelected()) color = Color.BLUE;
                if (pt10.isSelected()) font = new Font("", Font.PLAIN, 10);
                else if (pt12.isSelected()) font = new Font("", Font.PLAIN, 12);
                else if (pt14.isSelected()) font = new Font("", Font.PLAIN, 14);
                repaint();
            }
        });

        /**
         * Method for action clicking on mouse
         *
         * @param e - event
         */
        addMouseListener(new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent e) {
                x = e.getX();
                y = e.getY();
                xField.setText(Integer.toString(x));
                yField.setText(Integer.toString(y));
               // repaint();
            }
            @Override
            public void mousePressed(MouseEvent e) { }
            @Override
            public void mouseReleased(MouseEvent e) { }
            @Override
            public void mouseEntered(MouseEvent e) { }
            @Override
            public void mouseExited(MouseEvent e) { }
        });

        topPanel = new GraphicPanel();
        topPanel.setBorder(BorderFactory.createTitledBorder("Вивід напису"));
        botPanel = new JPanel();
        botPanel.setBorder(BorderFactory.createTitledBorder("Параметри напису"));
        botPanel.add(labelText);
        botPanel.add(textField);
        botPanel.add(labelColor);
        botPanel.add(black);
        botPanel.add(red);
        botPanel.add(green);
        botPanel.add(blue);
        botPanel.add(labelSize);
        botPanel.add(pt10);
        botPanel.add(pt12);
        botPanel.add(pt14);
        botPanel.add(labelX);
        botPanel.add(xField);
        botPanel.add(labelY);
        botPanel.add(yField);
        botPanel.add(button);
        this.add(topPanel);
        this.add(botPanel, BorderLayout.SOUTH);
        revalidate();
    }

    class GraphicPanel extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.setColor(color);
            g.setFont(font);
            g.drawString(textField.getText(), x, y);
        }
    }

    public static void main(String[] args) { new Lab6_22();}
}