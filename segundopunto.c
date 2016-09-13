#include<stdio.h>
int main(){
 int a=0,i=0,par=0,impar=0,positivo=0,negativo=0;

     for(i=0;i<10;i++)
      {
        printf("ingrese un número: ");
        scanf("%d",&a);

                if(a>0)
                  {
                      positivo=positivo+1;

                    if(a%2==0)
                     {
                       par=par+1;
                      }
                    else{
                        impar=impar+1;
                      }
		}
                else{
                        negativo=negativo+1;

                       if(a%2==0)
                        {
                          par=par+1;
                        }
			else{
                          impar=impar+1;
                            }
                     }
    }
printf("la cantidad de números positivos es: %d\n",positivo);
printf("la cantidad de números negativos es: %d\n",negativo);
printf("la cantidad de números pares es: %d\n",par);
printf("la cantidad de números impares es: %d\n",impar);
}
