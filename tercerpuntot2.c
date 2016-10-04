x#include<stdio.h>
int main(){
int opcion,a,b,c,d,e,f;
while (opcion!=6){
printf("1.sumar\n2.restar\n3.multiplicar\n4.dividir\n5.potencia\n6.salir");
scanf("%d",&opcion);
printf("Ingrese un numero: \n");
scanf("%d",&a);
printf("Ingrese otro numero: \n");
scanf("%d",&b);
switch(opcion){
   case 1:
     c=a+b;
     printf("El resultado de la suma es: %d\n",c);
   break;
   case 2:
     c=a-b;
     printf("El resultado de la resta es: %d\n",c);
   break;
   case 3:
     c=a*b;
     printf("El resultado de la mutiplicacion es: %d\n",c");
   break;
   case 4:
     c=a/b
     printf("El resultado de la division es: %d\n",c);
   break;
   case 5:
     c=1;
     d=a;
     e=1;
     for(f=c;f<=b;f++){
          e=d*e;
       }
     printf("El resultado de la potencia es: %d\n",e);
   break;
   case 6:
     printf("6.salir");
   break;
  }
 }
}
