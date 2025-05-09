"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Write a function that takes an array of numbers and returns the sum of the numbers.
The numbers can be negative or non-integer. If the array does not contain any numbers
then you should return 0.
"""

def sum_array(a):
    if len(a) == 0:
        return 0
    else:
        return sum(a)

if __name__ == '__main__':
    print(sum_array([]))
    print(sum_array([1, 2, 3]))
    print(sum_array([1.1, 2.2, 3.3]))
    print(sum_array([4, 5, 6]))
    print(sum_array(range(101)))