import java.io.*;

class GFG {
	public static void main (String[] args) {
	//start s[] time and finish time f[] are declared here
	int s[]={1,3,0,5,8,5};
	int f[]={2,4,6,7,9,9};
	int n=s.length;
	printActivityProblem(s,f,n);
	
	
	}
	public static void printActivityProblem(int s[], int f[],int n)
	{
	   int i=0;
	   System.out.print(i+" ");
	   for(int j=1;j<n;j++)
	   {
	       if(s[j]>=f[i])
	       {
	           System.out.print(j+" ");
	           i=j;
	       }
	   }
	    
	}
	
}
