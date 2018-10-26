
package myPackage;
import java.io.*;

public class MyClass
{
//getNames takes an argument s as string and
//print output of the input string s;
  public void getNames(String s)
  {
    System.out.println(s);
  }
//Function for adding two number
//Having argument a and b as an integer
  public void addOfNumber(int a, int b)
  {
   int c;
   c=a+b;
   System.out.println(c);
 }

 //Module for Disk space available
 //in root directory
 public static void spaceOnDisk()
    {
        File file = new File("/");

        double size = file.getFreeSpace() / (1024.0 * 1024 * 1024);
        System.out.println(size);
    }
}
