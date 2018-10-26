import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
	public static void main (String[] args)
	 {
	 //code
	 //test case declaration
	 int test;
	 Scanner sc=new Scanner(System.in);
	 test=sc.nextInt();
	 //while for test case execution 
	 while(test-->0)
	 {
	     String name=sc.next();
	     char ch=name.charAt(0);
	     //Checking the case of char
	     if(ch.isUpperCase()==true)
	     {
	         System.out.println(name.toUpperCase());
	         
	     }
	     //else case for char is lower case
	     else
	     {
	         System.out.println(name.toLowerCase());
	         
	     }
	     
	 }
	 }
}
