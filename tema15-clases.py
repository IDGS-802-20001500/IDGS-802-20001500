import os



class OperasBas:
    #declaración de propiedades

    num1 = 0
    num2 = 0
    res = 0

    # declaración de constructor
    
    def __init__(self, a, b):
        self.num1=a
        self.num2=b
    


    # declaración de metodos de clase

    def sum(self):
        #num1 = 12
        #num2 = 10
        self.res = self.num1 + self.num2
        print("La suma es: {}".format(self.res))


def main():
    obj = OperasBas(3, 4)
    obj.sum()

if __name__ == "__main__":
    main()



    



