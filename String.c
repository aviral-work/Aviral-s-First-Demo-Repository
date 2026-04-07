#include<stdio.h>
#include<conio.h>
int main()
{
    int n;
    char name[n];
    printf("Enter your name: ");
    //len function in C is used to calculate the length of a string. It is defined in the string.h header file. The syntax for using the len function is as follows:
    //len(string);
    scanf("%s",name);
    n=strlen(name);
    printf("Hello, %s!",name);
    printf("\nLength of your name is: %d",n);
    return 0;
}