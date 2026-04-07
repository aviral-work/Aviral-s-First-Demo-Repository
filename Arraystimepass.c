#include<stdio.h>
#include<conio.h>
void main()
{
    int l;
    printf("Enter length of array= ");
    scanf("%d",&l);
    int a[l];
    int i;
    printf("Enter numbers in array= ");
    for(i=0;i<l;i++)
    {
        scanf("%d\n",&a[i]);
    }
    printf("Numbers in array are= ");
    for(i=0;i<l;i++)
    {
        printf("%d\n",a[i]);
    }


}