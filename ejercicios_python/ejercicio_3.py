#!/usr/bin/env python3
"""
Ejercicio 3. Escriba un programa con las funciones necesarias para realizar las operaciones de: suma, resta, multiplicación y división. El programa deberá llevar a cabo todas las operaciones al recibir dos parámetros numéricos durante la ejecución del mismo. Ver input(). Ejemplo: Operación suma Ingrese operador 1: 1 Ingrese operador 2: 2 Resultado: 3

"""


def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    if b == 0:
        return "Error no se puede dividir por cero"
    return a/b

def main():
    num1 = float(input("Ingresa un numero 1: "))
    num2 = float(input("Ingresa un numero 2: "))

    print("\nResultados:")
    print(f"Suma: {sumar(num1, num2)}")
    print(f"Resta: {restar(num1, num2)}")
    print(f"Multiplicación: {multiplicar(num1, num2)}")
    print(f"División: {dividir(num1, num2)}")

if __name__ == "__main__":
    main()