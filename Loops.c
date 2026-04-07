#include<stdio.h>
#include<conio.h>
int main()
{
    int i,n,ni;
    printf("Enter number for multiplication table= \n");
    scanf("%d",&n);
    for(i=1;i<=10;i++)
    {
        ni=n*i;

        printf("%d x %d = %d\n",n,i,ni);
    }
}