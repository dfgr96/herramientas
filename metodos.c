#include<stdio.h>
int suma(int a, int b);
int resta(int a, int b);
int multiplicacion(int a, int b);
int potencia(int a, int b);

int main(){

 int n1, n2, oper, result;

 while(1){

   printf("1. suma\n 2. resta\n 3. multiplicacion\n 4. potencia\n 5. salir\n");
   scanf("%d",%oper);

    switch (oper){

      case 1:
             printf("Escriba un numero: ");
             scanf("%d",&n1);
             printf("Escriba otro numero: ");
             scanf("%d",&n2);
             result=suma(n1, n2);
             printf("El resultado de la suma es: %d",result);
      break;

      case 2:
             printf("Escriba un numero: ");
             scanf("%d",&n1);
             printf("Escriba otro numero: ");
             scanf("%d",&n2);
             result=resta(n1, n2);
             printf("El resultado de la resta es: %d",result);
      break;

      case 3:
             printf("Escriba un numero: ");
             scanf("%d",&n1);
             printf("Escriba otro numero: ");
             scanf("%d",&n2);
             result=multiplicacion(n1, n2);
             printf("El resultado de la multiplicacion  es: %d",result);
       break;

       case 4:
             printf("Escriba un numero: ");
             scanf("%d",&n1);
             printf("Escriba el exponente de la operacion anterior: ");
             scanf("%d",&n2);
             result=potencia(n1, n2);
             printf("El resultado de la potencia es: %d",result);
       break;

       case 5:
             printf("Ha salido del sistema.\n");
             return 0;
      break;
    }
 }
}

    int suma(int n1, int n2){
            return n1+n2;
    }

    int resta(int n1, int n2){
             return n1-n2;
    }

    int multiplicacion(int n1, int n2){
             int a=0;
             for(int i=0;i<n2;i++){
                a=a+n1;
             }
      return a;
    }

    int potencia(int n1, int n2){
            int a=n1;
            int b=0;
            for(int i=0;i<n2;i++){
            a=a+b;
            b=0;
             for(int f=1;f<n1;f++){
             b=b+a;
             }
            }
       return a;
    }
