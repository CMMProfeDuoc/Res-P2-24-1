"""
Suponga que le dan una lista de varios textos, debe calcular el peso de cada texto segun lo siguiente:
Se asigna un valor a cada letra, de la siguiente manera
a = 1, b= 2, c = 3 . . . hasta la z.
Las mayúsculas valen el doble.
Puede considerar que no se ingresaran "ñ" o "Ñ"
Por cada número en el texto, se suma el valor de ese número al ‘peso’.
Hay símbolos que restan valor al ‘peso’.
* = -1 , ~ = -2 , & = -3 , $ = -5, # = -10
El resto de símbolos no afecta nada.
Muestre en pantalla una lista con el peso de cada texto de la lista inicial.
La palabra con más valor.
La palabra con menos valor.
El promedio de valor de las palabras.
"""

lista_letras = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]

lista_strings = [
    'hola','a*','pepito#'
]
lista_valores = []


for palabra in lista_strings:
    valor = 0
    for letra in palabra:
        if (letra.lower() in lista_letras): #EN CASO DE LETRA
            mayus_mult = 1
            if (letra.isupper()): 
                mayus_mult = 2
            valor += lista_letras.index(letra.lower())+1 * mayus_mult

        if (letra.isdigit()): #EN CASO DE NUMERO
            valor += int(letra)

        if (letra == '*'):
            valor -= 1

        if (letra == '~'):
            valor -= 2

        if (letra == '&'):
            valor -= 3
        
        if (letra == '$'):
            valor -= 5

        if (letra == '#'):
            valor -= 10

    lista_valores.append(valor)

for i in range(len(lista_strings)):
    print(lista_strings[i],lista_valores[i],sep=' => ')

indice_min = 0
minimo = 0

indice_max = 0
maximo = 0

suma = 0

for i in range(len(lista_valores)):
    if (i == 0) or (lista_valores[i] < minimo):
        minimo = lista_valores[i]
        indice_min = i

    if (i==0) or (lista_valores[i] > maximo):
        maximo = lista_valores[i]
        indice_max = i

    suma += lista_valores[i]

print("palabra minima:",lista_strings[indice_min])
print("palabra maxima:",lista_strings[indice_max])
print("Prom:",suma/len(lista_strings))