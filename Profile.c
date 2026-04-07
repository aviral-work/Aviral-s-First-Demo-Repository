#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
    char name[10];
    printf("How are you? what is your name ");
    scanf("%s",name);
    printf("Your name length is (characters) \n",name);
    int length;
    length=strlen(name);
    printf("%d\n",length);
    printf("Welcome to this program %s\n", name);
    int age;
    printf("What is your age?\n");
    scanf("%d",&age);
    char email[20];
    printf("Enter your email address= \n");
    scanf("%s",email);
    printf("So hi %s, your age is %d and your email address is %s\n",name,age,email);
    printf("Now I would like to ask you some questions about your hobbies\n");
    char hobby[20];
    printf("What is your hobby?\n");
    scanf("%s",hobby);
    char music[20];
    printf("What is your favorite music genre?\n");
    scanf("%s",music);
    printf("_________________________________________\n");
    printf("User Profile:\nName: %s\nAge: %d\nEmail: %s\nHobby: %s\nFavorite Music Genre: %s\n", name, age, email, hobby, music);
    return 0;
}

    