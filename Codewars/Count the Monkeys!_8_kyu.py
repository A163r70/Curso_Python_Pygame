"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 25 de abril de 2025
Descripción:
You take your son to the forest to see the monkeys. You know that there are a certain number there (n),
but your son is too young to just appreciate the full number, he has to start counting them from 1.

As a good parent, you will sit and count with him. Given the number (n), populate an array with all numbers
up to and including that number, but excluding zero.
"""

def monkey_count(n):
    monkeys = []
    for i in range(1, n+1):
        monkeys.append(i)
    return monkeys


if __name__ == '__main__':
    print(monkey_count(10))