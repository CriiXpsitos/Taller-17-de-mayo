#zero 
#a = 4; b = 0
#print(a/b)

# eror index
lista = [1, 2, 3]
try:
    elemento = lista[8]
except IndexError:
    print("Error: El índice está fuera del rango de la lista.")
  
print("\n")

#error type error 

try:
    resultado = "10" + 5
except TypeError:
    print("Error: No se puede concatenar una cadena de texto con un número.")

print("\n")

#error value - error

try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir 'abc' a un entero.") 