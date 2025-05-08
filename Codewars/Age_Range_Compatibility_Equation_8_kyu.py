"""
Nombre: Jesús Alberto Ramírez Salinas
Fecha: 29 de abril de 2025
Descripción:
Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so if the age <= 14, use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age

You should floor all your answers so that an integer is given instead of a float (which doesn't represent age).
Return your answer in the form "[min]-[max]"
"""

def dating_range(age):
    if age <= 14:
        min = int(age - (0.10 * age))
        max = int(age + (0.10 * age))
    else:
        min = int((age/2)+7)
        max = int(2*(age-7))
    min_max = str(min)
    min_max += str('-')
    min_max += str(max)
    return min_max

if __name__ == '__main__':
    print(dating_range(17))
    print(dating_range(40))
    print(dating_range(15))
    print(dating_range(35))
    print(dating_range(10))
    print(dating_range(53))
    print(dating_range(19))
    print(dating_range(12))
    print(dating_range(7))
    print(dating_range(13))