#include<stdio.h>
main(){
int x;
float pi=3.14159;
int diametro;
int circ;
float  area;
printf("Escriba el radio de su circulo: ");
scanf("%d",&x);
diametro=x+x;
printf("El diametro es: %d\n",diametro);
circ=pi*diametro;
printf("La circunferencia de su circulo es: %d\n",circ);
area=pi*x*x;
printf("El area de su circulo es: %.2fn",area);
}


