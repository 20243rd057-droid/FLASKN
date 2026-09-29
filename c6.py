def agregar_lista():
    """
    agregar_lista | Emiliano Gomez | 2025-09-11
    modified: 2025-09-11 | initial version | Emiliano Gomez

    params:
    
    return:
    list
    """
    lista = []

    for i in range(5):
        lista.append(i)

    return lista


def agregar_diccionario():
    """
    agregar_diccionario | Emiliano Gomez | 2025-09-11
    modified: 2025-09-11 | initial version | Emiliano Gomez

    params:

    return:
    dictionary
    """
    diccionario = {}

    for i in range(5):
        diccionario[i] = i * 10

    return diccionario


def imprimir_elementos():
    """
    imprimir_elementos | Emiliano Gomez | 2025-09-11
    modified: 2025-09-11 | initial version | Emiliano Gomez

    params:

    return:
    None
    """
    lista = agregar_lista()
    diccionario = agregar_diccionario()

    print("Elementos de la lista:")
    for elemento in lista:
        print(elemento)

    print("Elementos del diccionario:")
    for clave, valor in diccionario.items():
        print(clave, ":", valor)


print("Lista creada:")
print(agregar_lista())

print("Diccionario creado:")
print(agregar_diccionario())

print("Impresión de elementos:")
imprimir_elementos()