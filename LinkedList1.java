class LinkedList1{

Node head;
static class Node{
int data;
Node next;
Node(int d){data=d; next=null;}//constructor


}

public void PrintList()
{
Node n=head;
while(n!=null)
{
System.out.print(n.data + " ");
n=n.next;
}

}

public static void main(String[] args)
{
LinkedList1 llist=new LinkedList1();

llist.head=new Node(1);
Node second=new Node(2);
Node third=new Node(3);

llist.head.next=second;
second.next=third;
llist.PrintList();
}
}
