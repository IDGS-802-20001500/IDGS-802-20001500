# Nombre de variables

"""
* Tiene que tener nombres significativos
* Relacionados con lo que representa la variable.
* NO debe ser Keywords (palabras reservadas)
"""

numero = "123"
numero2 = "10"
nombre  =  "Mauricio"
email = "mauriciofernandez832@gmail.com"

print(numero + numero2)

# Conversión forzosas entre tipos de datos

print("La suma es: ")
print(int(numero)+int(numero2))

sueldo = "1200.563"

valorDecimal = float(sueldo)
print(valorDecimal)


edad = 123
print(len(str(edad)))