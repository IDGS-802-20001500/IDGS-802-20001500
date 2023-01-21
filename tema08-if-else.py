print("Suma de numeros")

num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))

if num1 > num2:
    print("El {} es mayor que el {}".format(num1,num2))
else:
    print("El {} es mayor que el {}".format(num2,num1))

print("---------------------Pedir una edad-----------------------")
edad=int(input("Ingrese edad: "))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres menor de edad")