import java.util.*;
import java.lang.*;
import java.io.*;
class palindrome
 {
	public static void main (String[] args) throws java.lang.Exception
	 {
	 //code
	 //while test case
	 Scanner sc=new Scanner(System.in);
	 int test=sc.nextInt();
	 sc.nextLine();
	 while(test-->0)
	 {
	     String s=sc.next();
	     String reverse=new StringBuffer(s).reverse().toString();
	     if(s.equals(reverse))
	     {
	         System.out.println("Yes");
	     }
	     else
	     {
	         System.out.println("No");
	     }
	 }
	 }
}
