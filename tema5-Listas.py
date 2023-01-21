"""
Listas

* Una lista es una secuencia de elementos.
* Cunado se asigna a una variable, permite agrupar varios elementos en un solo lugar
* se crean con los [] o con los keywords lsit.
"""

lista1 = ["Mauricio", 33, 9.5, True, "Fernández", 20, 8]

print(lista1)

print(lista1[:])

print(lista1[2])

print(lista1[-1])

print(lista1[0:3])

print(lista1[3:])

lista1.append("Ramos")
print(lista1)

lista1.insert(2, "Israel")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(8)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ["tres", "cuatro"]

lista3 = lista1 + lista2

print(lista3)

print(lista2*4)
lista4 = [2, 1, 3, 4, 7, 6, 5]
print(lista4.sort())

del lista4[0]
print(lista4)


