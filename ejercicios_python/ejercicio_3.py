#!/usr/bin/env python3

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