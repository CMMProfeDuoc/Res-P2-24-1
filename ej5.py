"""
Unos científicos han logrado crear un programa que es capaz de leer ADN y convertirlo a letras, pero, el programa a veces falla.
Cada lista de letras tiene las letras ‘A’ ‘T’ ‘C’ o ‘G’, nada más, a veces en mayúsculas, a veces en minúsculas.
Los científicos le indican que los pares del ADN siempre son AT o TA o CG o GC.
Usted debe crear un programa que reciba 2 listas de letras (correspondientes al par de secuencias de ADN) e indique lo siguiente:
Si es una secuencia válida (que no tenga errores)
Y si tiene errores, indique cuantos, luego, debe corregirlos y mostrar la secuencia correcta.
Considere que ambas listas tienen el mismo tamaño.
Considere que la primera lista, siempre esta correcta, debe corregir la segunda lista.
"""

par1 = ['a','A','T','G','c']
par2 = ['T','a','a','c','G']

errores = []

for i in range(len(par1)):
    print(i,par1[i],par2[i])


    if (par1[i].upper() == 'A') and (par2[i].upper() != 'T'):
        errores.append(i)
        continue

    if (par1[i].upper() == 'T') and (par2[i].upper() != 'A'):
        errores.append(i)
        continue

    if (par1[i].upper() == 'C') and (par2[i].upper() != 'G'):
        errores.append(i)
        continue

    if (par1[i].upper() == 'G') and (par2[i].upper() != 'C'):
        errores.append(i)
        continue

if (len(errores) > 0):
    print("HAY ERRORES")
    print("errores en pos:",errores)
else:
    print("NO HAY ERRORES")

if (errores != []):
    for index in errores:
        if (par1[index].upper() == 'A'):
            par2[index] = 'T'

        if (par1[index].upper() == 'T'):
            par2[index] = 'A'

        if (par1[index].upper() == 'G'):
            par2[index] = 'C'

        if (par1[index].upper() == 'C'):
            par2[index] = 'G'
    print("ERRORES CORREJIDOS")
for i in range(len(par1)):
    print(par1[i],par2[i])