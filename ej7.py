"""
Un restaurante ha registrado sus productos en dos listas, una contiene los nombres de los productos y otra contiene los precios de los productos.
Han creado también un sistema para que el usuario seleccione productos usando solo números, los que se guardan en una lista, pero, falta el sistema de cobro.
Usted sabe que hay solo hay 8 platos en el menú (numerados del 0 al 7) y que la gente solo ingresa números enteros en la lista de selección. Lamentablemente, la gente a veces escribe números que no son parte del menú, pero, el programa debe seguir funcionando, recuerde eso.
DEBE CONSIDERAR QUE EL DUEÑO DEL RESTORANT PODRIA QUERER AGREGAR MÁS ITEMS A LA LISTA
Cree un programa que muestre las listas de productos y precios.
Luego permita al usuario ingresar un numero para seleccionar un producto.
El usuario podrá ingresar productos hasta que ingrese un numero negativo.
Cuando el usuario termina de seleccionar elementos aparece en pantalla el costo total de su pedido.
El usuario luego podra ingresar un porcentaje de propina (por defecto 10%), y el programa mostrara el precio final de todo, incluyendo propina.
"""

nom_platos = ['bebida', 'jugo', 'completo', 'churrasco', 'chacarero','pizza','postre','te']
precios_platos = [1000, 1200, 1500, 2000, 2200, 4000, 1300,500]

pedido = []

while (True):
    for i,plato in enumerate(nom_platos):
        print(i,'. ',plato,'  $',precios_platos[i],sep='')

    sel = int(input(">> "))
    if (sel < 0):
        break
    if (sel not in range(len(nom_platos))):
        print("tonto")
        continue
    
    pedido.append(sel)
    print("guardado ->",nom_platos[sel])

#termina de pedir cosas

cuenta_total = 0 
print("Pedido: ")
for num in pedido:
    print(nom_platos[num],precios_platos[num],sep=' => $')
    cuenta_total += precios_platos[num]
print('-'*10)
print('Cuenta: $',cuenta_total)

propina = int(input("ingrese propina: "))
if (propina not in range(101)):
    propina = 10

cuenta_total *= 1 + (propina/100)

print('Su cuenta es: $',int(cuenta_total))


