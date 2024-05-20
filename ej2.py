"""
Cree un programa que reciba un string de una operación matemática y lo resuelva.
Considere que la operación solo usara dos términos enteros, positivos y de un solo digito.
El programa funciona hasta que el usuario ingrese 'salir'. Al principio de cada ciclo debe mostrar las operaciones previamente realizadas.
Operaciones aceptadas: + - / *
"""

historial = []
while (True):
    for h in historial:
        print(h)
    print()

    operacion = input("Ingrese operacion matematica: ")
    if (operacion.lower() == 'salir'):
        break
    
    lista_op = []


    for o in operacion:
        if (o != ' '):
            lista_op.append(o)
    simbolo = lista_op[1]
    a = int(lista_op[0])
    b = int(lista_op[2])
    res = 0

    if (simbolo == '+'):
        res = a+b

    if (simbolo == '-'):
        res = a-b

    if (simbolo == '*'):
        res = a*b

    if (simbolo == '/'):
        if (b == 0):
            print("no se puede dividir por 0. TONOTO")
            res = ' tonoto '
        else:
            res = a/b

        
    historial.append(operacion + '=' + str(res))
