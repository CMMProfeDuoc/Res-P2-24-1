"""
Un grupo de científicos le pasa una lista con secuencias de ADN.
Cada secuencia es un texto que tiene las letras A T C G
Las letras siempre deben ir en pares que son AT o TA o CG o GC, todas separadas por un -
Usted debe crear un programa que lea esta lista de cadenas de ADN e indique cuál de estas cadenas es una secuencia válida y cuál no.
Considere que la secuencia solo contendrá letras y el -, estará bien escrita.
"""

adn = [
    'AT-CG-GG-TA-TA-TT',
    'AA-AT-CG-GC-GC-TA-AT',
    'AT-TA-GC',
    'AA-AA-GC'
]

resultados = []

for cadena in adn:
    lista_adn = []
    estado = 'BUENO'
    for letra in cadena:
        if (letra != '-'):
            lista_adn.append(letra)
    
    while (lista_adn != []):
        primero = lista_adn.pop(0)
        segundo = lista_adn.pop(0)

        if (primero == 'A') and (segundo != 'T'):
            estado = 'MALO'
            break

        if (primero == 'T') and (segundo != 'A'):
            estado = 'MALO'
            break

        if (primero == 'C') and (segundo != 'G'):
            estado = 'MALO'
            break

        if (primero == 'G') and (segundo != 'C'):
            estado = 'MALO'
            break
    
    resultados.append(estado)

for i in range(len(adn)):
    print(adn[i],'=>',resultados[i])