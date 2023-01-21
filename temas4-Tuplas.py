"""
TUPLAS no son inmutables
"""

tupla=("uno", "dos", "tres")

print(tupla)

tuplasVariosDatos=(12, True, 23.6, "Roberto", 12+2j)

print(tuplasVariosDatos)

tuplasConTuplas =(12,(1, 2, 3, 4, 5),(6,7 ,89),(12, 44, 2.3, 56))
print(tuplasConTuplas)

print(tuplasConTuplas[3])
print(tuplasConTuplas[-2])
print(tuplasConTuplas[0:2])

a,b,c=tupla

print(a)
print(b)
print(c)

tuplaNueva = tupla+tuplasVariosDatos
print(tuplaNueva)