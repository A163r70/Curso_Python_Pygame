"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 25 de abril de 2025
Descripción:
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    print(even_or_odd(2))
    print(even_or_odd(1))
    print(even_or_odd(-1))
    print(even_or_odd(0))