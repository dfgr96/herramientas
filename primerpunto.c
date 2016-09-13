#include <stdio.h>
int main (){
int a;
int b;
printf("inserte un número: ");
scanf("%d",&a);
printf("inserte un número: ");
scanf("%d",&b);
if(a<b)
  {
    printf("el número mayor es: %d\n",b);
  }
if(a>b)
  {
    printf("el número mayor es:%d\n",a);
  }

}
