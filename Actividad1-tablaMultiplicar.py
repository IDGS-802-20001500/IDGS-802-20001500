
x = int(input("Dame un numero: "))

print("-------{}-------".format(x))

for index in range(1, 11):
    print("|{} x {} = {}".format(x, index,(x * index)))

