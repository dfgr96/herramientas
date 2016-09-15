#include<stdio.h>
int main(){
int a;
printf("Ingrese un número: ");
scanf("%d",&a);
while(a<0){
  if(a>0){
   printf("El número es mayor a 0. ");
    }
  else{
    printf("Ingrese otro número: ");
    scanf("%d",&a);
     }
 }
}
