"""
Un pescador necesita su ayuda para saber cuando la venta que lograra con la captura recien hecha.
El pescador anota en una lista el tipo de pescado y el peso de la siguiente forma:
'tipo_pescado peso_kg'
ej: ['jurel 1', 'salmon 5', … ]
El pescador debe saber en cuanto puede vender la captura del dia según lo siguiente:
El kilo de salmon cuesta $6000
Si un salmon pesa más de 5 kilos, vale el doble.

El kilo de jurel cuesta $4000
Si un jurel pesa menos de 3 kilos, no se puede vender.

El kilo de reineta cuesta $5000

El kilo de lenguado cuesta $3000

Si hay algun delfin la pesca se vuelve invalida!

Cualquier otro pescado no se cuenta.
Muestre en pantalla en cuanto se puede hacer la venta, si es que es posible.
Cuantos pescados de cada uno se vendieron.
Cuantos kilos de cada pescado se vendieron.
Considere que un pescado no puede pesar más de 9 kilos y siempre tendrá un peso positivo y entero.
Considere que cada elemento en la lista estará bien escrito.
"""

pesca_dia = [
    'jurel 6', 'atun 3', 'salmon 1','delfin 0'
]

#indices:
#0-salmon 1-jurel 2-reineta 3-lenguado
cont_pescados = [0,0,0,0]
kilos_pescados = [0,0,0,0]
nom_pescados = ['salmon','jurel','reineta','lenguado']

total_venta = 0
hay_delfin = False
for pescado in pesca_dia:
    peso = int(pescado[-1])

    if ('salmon' in pescado):
        if (peso > 5):
            total_venta += peso * 6000 * 2
        else:
            total_venta += peso * 6000
        kilos_pescados[0] += peso
        cont_pescados[0] += 1

    if ('jurel' in pescado):
        if (peso > 3):
            total_venta += peso * 4000
        kilos_pescados[1] += peso
        cont_pescados[1] += 1

    if ('reineta' in pescado):
        total_venta += peso * 5000
        kilos_pescados[2] += peso
        cont_pescados[2] += 1

    if ('lenguado' in pescado):
        total_venta += peso * 3000
        kilos_pescados[3] += peso
        cont_pescados[3] += 1

    if ('delfin' in pescado):
        hay_delfin = True
        total_venta = 0
        break

if (hay_delfin):
    print("DELFIN, VENTA ANULADA >:C ")
else:
    print("La venta es:",total_venta)

    print('NOM  | cant | kilos')
    for i in range(len(nom_pescados)):
        print(nom_pescados[i],cont_pescados[i],kilos_pescados[i])
