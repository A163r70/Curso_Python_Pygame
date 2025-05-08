"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 25 de abril de 2025
Descripción:
Take an array and remove every second element from the array. Always keep the first element and
start removing with the next element.
"""

def remove_every_other(my_list):
    resultado = []
    for indice in range(len(my_list)):
        if indice % 2 == 0:
            resultado.append(my_list[indice])
    return resultado


if __name__ == '__main__':
    print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
    print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(remove_every_other([[1, 2]]), [[1, 2]])
    print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))