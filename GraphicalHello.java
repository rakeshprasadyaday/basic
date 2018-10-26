import javax.swing.*;
 public class GraphicalHello
{
public static void main(String[] args)
{

JFrame frame=new JFrame("Hello, Wo");
JLabel label=new JLabel("Hello ",JLabel.CENTER);
frame.add(label);
frame.setSize(300,300);
frame.setVisible(true);
}
}
