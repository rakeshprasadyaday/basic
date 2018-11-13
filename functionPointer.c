#include <stdio.h> 
//Program for demonstrating function pointer std::array<T, N> ;
 
void add(int a, int b)
{
    printf("Addition of number is %d \n",a+b);
}

void substraction(int a, int b)
{
    printf("substraction of number is %d \n",a-b);
}

//Driver code
int main()
{
    unsigned int a,b=100,c=47;
    void (*fun_ptr[])(int,int)={add,substraction};
    printf("Enter your choice 1,2 or defa\n");
    scanf("%d",&a);
    
    if(a>1)
        return 0;
    (*fun_ptr[a])(b,c);
    
    return 0;
}
