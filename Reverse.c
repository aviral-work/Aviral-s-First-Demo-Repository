#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
    int i=0;
    char word[100];
    printf("Enter word to reverse ");
    scanf("%s",word);
    while(word[i]!='\0')
    {
        printf("%c",word[i]);
        i++;
        //Aviral 012345
    }
    for(i=i-1;i>=0;i--)
    {
        printf("%c",word[i]);
    }
    return 0;
}