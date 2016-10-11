#include<stdio.h>
main(){
int n,x,y,a,b,c;
int modulo;
int oper;
int res;

printf("escriba la base 1 : ");
scanf("%d",&n);
printf("escriba la base 2: ");
scanf("%d",&x);
printf("esciba la base 3: ");
scanf("%d",&y);
printf("escriba el modulo: ");
scanf("%d",&modulo);
a=n-modulo;
b=x-modulo;
c=y-modulo;
printf("1.sumar\n 2.restar\n 3.multiplicar\n");
scanf("%d",&oper);
 switch(oper){
   case 1:
        res=a+b+c;
     printf("El resultado es: %d\n",res);
  break;

   case 2:
        res=a-b-c;
     printf("Ek resultado es: %d\n",res);
  break;

  case 3:
       res=a*b*c;
    printf("El resultado es: %d\n",res);

 }

}

