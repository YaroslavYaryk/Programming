// 18.
//Рисование фигуры в графическом окне. В верхней панели (JPanel) "Вывод дуги" в графическом контексте рисуется
// (с помощью метода drawArc()) дуга. В нижней панели (JPanel) "Параметры дуги" задаются следующие компоненты:
// надпись (JLabel)   "Координата X:", текстовое поле   (JTextField), надпись (JLabel)
// "Координата Y:", текстовое поле   (JTextField),  надпись (JLabel)   "Ширина:", текстовое поле   (JTextField),
// надпись (JLabel)   "Высота:", текстовое поле (JTextField), надпись (JLabel)   "Начальный угол:",
// две радиокнопки  "Плюс" и "Минус", вращающийся список  (JSpinner), надпись (JLabel)   "Конечный угол:",
// две радиокнопки  "Плюс" и "Минус", вращающийся список  (JSpinner) и кнопка (JButton) "Вывести дугу".
// При вводе данных для координат и размера (в пикселях), набора данных для углов и при нажатии кнопки "Вывести дугу"
// дуга перерисовывается с заданными параметрами. При вводе данных проверяется, все ли данные введены и являются ли
// данные целыми числами. Значения данных во вращающемся списке – в диапазоне от 0 до 360 с шагом 45.

import javax.swing.*;
import java.awt.*;

/**
 * The class is used to store objects with the property
 * <b>X</b> <b>Y</b> <b>WID</b> <b>HEIG</b> <b>START</b> <b>FINISH</b> <b>spinnerS</b>
 * <b>spinnerE</b> <b>plusS</b> <b>minusS</b> <b>plusE</b> <b>minusE</b>
 *
 * @author aDyhanov Yaroslav
 * @version 1.0
 */
public class Lab6_18 extends JPanel {
    public static Integer X = 0;
    public static Integer Y = 0;
    public static Integer WID = 0;
    public static Integer HEIG = 0;
    public static Integer START = 0;
    public static Integer FINISH = 0;
    public static JSpinner spinnerS, spinnerE;
    public static JRadioButton plusS, minusS, plusE, minusE;

    /**
     * Method for starting program and create an app with panels and painting part
     *
     * @param args - that we can give with console usage
     */
    public static void main(String[] args) {
        JFrame jFrame = add_frame("Lab6_18");
        JPanel output = new Lab6_18.draw_arc();
        output.setBorder(BorderFactory.createTitledBorder("Вивід дуги:"));
        JPanel parameters = add_panel();
        parameters.setBorder(BorderFactory.createTitledBorder("Параметри дуги:"));
        jFrame.add(output);
        jFrame.add(parameters, BorderLayout.SOUTH);
        jFrame.revalidate();
    }
    /**
     * Method for making the app and positioning it on the screen
     *
     * @param title - that set a title of the app
     */
    public static JFrame add_frame(String title) {
        JFrame jFrame = new JFrame();
        jFrame.setTitle(title);
        jFrame.setVisible(true);
        jFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Toolkit toolkit = Toolkit.getDefaultToolkit();
        Dimension dimension = toolkit.getScreenSize();
        jFrame.setBounds(dimension.width / 2 - 750, dimension.height / 2 - 500, 1500, 1000);
        return jFrame;
    }
    /**
     * Method that set a panel with components (with validating)
     *
     * @return parameters
     */
    public static JPanel add_panel() {
        JPanel parameters = new JPanel();
        plusS = new JRadioButton("+");
        minusS = new JRadioButton("-");
        plusE = new JRadioButton("+");
        minusE = new JRadioButton("-");

        JLabel xcoord = new JLabel("Координата X: ");
        parameters.add(xcoord);

        JTextField x = new JTextField("0", 5);
        parameters.add(x);

        JLabel ycoord = new JLabel("Координата Y: ");
        parameters.add(ycoord);

        JTextField y = new JTextField("0", 5);
        parameters.add(y);

        JLabel wid = new JLabel("Ширина: ");
        parameters.add(wid);

        JTextField width = new JTextField("0", 5);
        parameters.add(width);

        JLabel heig = new JLabel("Висота: ");
        parameters.add(heig);

        JTextField height = new JTextField("0", 5);
        parameters.add(height);
        JLabel st_ancle = new JLabel("Початковий кут: ");
        parameters.add(st_ancle);
        ButtonGroup buttonGroupS = new ButtonGroup();
        buttonGroupS.add(plusS);
        buttonGroupS.add(minusS);
        parameters.add(plusS);
        parameters.add(minusS);
        SpinnerNumberModel spinnerNumberModelS = new SpinnerNumberModel(0, 0, 360, 45);
        spinnerS = new JSpinner(spinnerNumberModelS);
        parameters.add(spinnerS);

        JLabel fin_ancle = new JLabel("Кінцевий кут: ");
        parameters.add(fin_ancle);
        ButtonGroup buttonGroupE = new ButtonGroup();
        buttonGroupE.add(plusE);
        buttonGroupE.add(minusE);
        parameters.add(plusE);
        parameters.add(minusE);
        SpinnerNumberModel spinnerNumberModelE = new SpinnerNumberModel(0, 0, 360, 45);
        spinnerE = new JSpinner(spinnerNumberModelE);
        parameters.add(spinnerE);


        JButton submit = new JButton("Вивести  дугу");
        parameters.add(submit);
        submit.addActionListener(e -> {
            String x_ = x.getText();
            String y_ = y.getText();
            String w_ = width.getText();
            String h_ = height.getText();
            String regexp = "^[0-9]+$";
            if (x_.matches(regexp) && y_.matches(regexp) && w_.matches(regexp) && h_.matches(regexp)) {
                X = Integer.parseInt(x.getText());
                Y = Integer.parseInt(y.getText());
                WID = Integer.parseInt(width.getText());
                HEIG = Integer.parseInt(height.getText());
                if (plusS.isSelected()) START = (Integer) spinnerS.getValue();
                else if (minusS.isSelected()) START = (Integer) spinnerS.getValue() * -1;
                if (plusE.isSelected()) FINISH = (Integer) spinnerE.getValue();
                else if (minusE.isSelected()) FINISH = (Integer) spinnerE.getValue() * -1;
            } else {
                JOptionPane.showMessageDialog(parameters, "Неправильні параметри дуги (тількі цілі)");
            }
        });
        return parameters;
    }

    /**
     * The class is used to override the method of JPanel class
     */
    static class draw_arc extends JPanel {
        /**
         * Overriding paintComponent method, that draw rectangle with some parameters
         * @param g object to draw
         */
        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.drawArc(X, Y, WID, HEIG, START, FINISH);
            repaint();
        }
    }
}