//for converting integer to string, we will use
Scanner sc=new Scanner(System.in);

int n=sc.nextInt();
String s=new Integer(n).toString();

//now for conforming whether it is converted or not
if(n==Integer.parseInt(s))
