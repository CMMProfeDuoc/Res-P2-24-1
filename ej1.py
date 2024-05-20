"""
Considere que usted tiene una lista de strings (pueden contener números y símbolos).
Cree un algoritmo que permita al usuario ingresar una serie de caracteres (hasta 5 caracteres) y muestre todas las palabras que tengan al menos uno de los caracteres ingresados. 
Luego, el programa pide otro carácter y reemplaza todos los caracteres ingresados, por el nuevo carácter ingresado.
"""

lista_strings = [
    'hola','completo','cafe'
]

print("lista:")
print(lista_strings)

lista_filtrada = []
filtro = input("filtro: ")[:5]
print("FILTRO:",filtro)
for elemento in lista_strings:
    for f in filtro:
        if (f in elemento):
            lista_filtrada.append(elemento)
            break
print("Lista filtrada:")
print(lista_filtrada)

lista_reemplazo = []
reemplazo = input("Ingrese caracter para reemplazar: ")[:1]
for elemento in lista_filtrada:
    texto = ''
    for letra in elemento:
        if (letra in filtro):
            texto += reemplazo
        else:
            texto += letra
    lista_reemplazo.append(texto)
print("reemplazo:")
print(lista_reemplazo)
