a=int(input("Escriba la primera base: "))
b=int(input("Rscriba la segunda base: "))
c=int(input("Escriba la tercera base: "))
mod=int(input("Escriba el modulo: "))

res1=int(a%mod)
res2=int(b%mod)
res3=int(c%mod)

print(" 1.suma\n 2.resta\n 3.multiplicacion\n")
operacion=int(input("Escriba la opcion: "))
if(operacion == 1):
	resultado =int(res1+res2+res3)
	print("el resultado de la suma es: "+str(resultado))
elif(operacion ==2):
	resultado=int(res1-res2-res3)
	print("el resultado de la resta: "+str(resultado))
elif(operacion == 3):
	resultado=int(res1*res2*res3)
	print("el resultado de la multiplicacion es: "+str(resultado))
