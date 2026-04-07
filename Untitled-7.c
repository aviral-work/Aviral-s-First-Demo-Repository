#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    int a[10]={1,2,3,4,5,6,7,8,9,10};
    int i,n1;
    printf("Enter the number to search:");
    scanf("%d",&n1);
    for(i=0;i<10;i++)
    {
        if(a[i]==n1)
        {
            printf("Number found at index %d\n",i);
            break;
        }
    }   
    printf("_________________________________________\n");
    
    int an,t,n,d;
    printf("Enter first term value= \n");
    scanf("%d",&t);
    printf("Enter common difference of series=\n");
    scanf("%d",&d);
    printf("Enter the nth term in series= \n");
    scanf("%d",&n);
    an=(t+(n-1)*d);
    printf("The nth term of series is %d",an);
    return 0;

    
}
