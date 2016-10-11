#include<stdio.h>
main(){
int a=0,b=0,c=0,d=0,e=0;
int suma;
float promedio;
int ndatos=5;
printf("Escriba el primer numero: ");
scanf("%d",&a);
printf("Escriba el segundo numero");
scanf("%d",&b);
printf("Escriba el tercer numero");
scanf("%d",&c);
printf("Escriba el cuarto numero");
scanf("%d",&d);
printf("Escriba el quinto numero");
scanf("%d",&e);
//scanf("5d",&e);
suma=a+b+c+d+e;
printf("La sumatoria es: %d\n",suma);
promedio=suma/ndatos;
printf("El promedio es: %f\n",promedio);
}
