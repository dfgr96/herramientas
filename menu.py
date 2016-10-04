print(" 1.suma\n 2.resta\n 3.multiplicacion\n 4.division\n")
operacion=int(input("Escriba la opcion: "))
if(operacion == 1):
	valor=int(input("ingrese un numero: "))
	valor2=int(input("ingrerse otro numero: "))
	resultado =valor+valor2
	print("el resultado de la suma es: "+str(resultado))
elif(operacion ==2):
	valor=int(input("ingrese el numero: "))
	valor2=int(input("ingrese otro numero: "))
	resultado=valor-valor2
	print("el resultado de la resta: "+str(resultado))
elif(operacion == 3):
	valor=int(input("ingrese el numero: "))
	valor2=int(input("ingrese el otro numero: "))
	resultado=valor*valor2
	print("el resultado de la multiplicacion es: "+str(resultado))
elif(operacion == 4):
	valor=int(input("ingrese un numero: "))
	valor2=int(input("ingrese otro numero: "))
	resultado=valor/valor2
	print("el resultado de la division es: "+str(resultado))
