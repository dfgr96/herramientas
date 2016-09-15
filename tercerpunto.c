#include<stdio.h>
int main(){
int c;
char b;
char a;
printf("Ingrese una letra: ");
scanf("%c%*c",&a);
printf("Ingrese otra letra: ");
scanf("%c",&b);
if(a>b){
 for(c=b;c<=a;c++){
   printf("%c",c);
   }
 }
else{
 for(c=a;c<=b;c++){
  printf("%c",c);
   }
 }
}
