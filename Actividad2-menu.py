import os

class Menu:
    num1  = 0
    num2  = 0
    res = 0

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
    
    def suma(self):
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))
        print("----------------")
        print(" ")

    def resta(self):
        self.res = self.num1 - self.num2
        print("La resta es: {}".format(self.res))
        print("----------------")
        print(" ")

    def multi(self):
        self.res = self.num1 * self.num2
        print("La multiplicación es: {}".format(self.res))
        print("----------------")
        print(" ")
        
    def div(self):
        self.res = self.num1 / self.num2
        print("La división es: {}".format(self.res))
        print("----------------")
        print(" ")


def main():
    a = int(input("Inserte un numero: "))
    b = int(input("Inserte un numero: "))
    obj = Menu(a, b)
    x = 0
    while x < 5:
        print("-------- Menú -------")
        print("| 1. Suma")
        print("| 2. Resta")
        print("| 3. Multiplicación")
        print("| 4. División")
        print("| 5. Salir")
        print("---------------------")
        print(" ")
        x = int(input("Opción: "))
        print(" ")
        print("----------------")
        
        if x == 1:
            obj.suma()
        elif x == 2:
            
            obj.resta()
        elif x == 3:
            
            obj.multi()
        elif x == 4:
            
            obj.div()
        else:
            print("Adiós")
            print(" ")
            #os.system("cls")
            


if __name__ == "__main__":
    main()



    



