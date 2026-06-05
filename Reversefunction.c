#include<stdio.h>
#include<conio.h>
#include<string.h>
void str_reverse(char x[100])
{
    int i=0;
    while(x[i]!='\0')
    {
        i++;
    }
    for (i=i-1;i>=0;i--)
    {
        printf("%c",x[i]);
    }
}
void main()
{   
    char x[100];
    printf("Enter a string to reverse= \n");
    scanf("%s",&x);
    str_reverse(x);
}