#include<stdio.h>
#include<conio.h>
int main()
{
    int n;
    printf("Enter number to calculate factorial= ");
    scanf("%d\n", &n);
    printf("The nno. you entered is= %d", n);
    if (n==1)
    {
        return 1;
    }
    else
    {
        while (n>1)
        {
            n = n-1;
        }
        printf("The factorial of %d is %d", n);
    }
    getch();
    return 0;
}
