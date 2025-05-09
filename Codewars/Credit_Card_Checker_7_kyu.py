"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Write a function that checks whether a credit card number is correct or not, using the Luhn algorithm.
"""

def valid_card(card):
    total = 0
    lista = list(card)
    for i in reversed(lista):
        total += i * i+1
        if total > 9:
            total -= 9
    return total

if __name__ == '__main__':
    print(valid_card("5457 6238 9823 4311"))