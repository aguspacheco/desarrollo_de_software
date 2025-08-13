#!/usr/bin/env python3

"""
Ejercicio 4. Escriba un programa que permita hacer la conversión de valores de temperatura entre Celsius y Fahrenheit. Se debe solicitar al usuario que ingrese un valor numérico y la escala original. El programa deberá mostrar por pantalla el valor convertido incluyendo la escala final. Ver input(). Construya dos funciones, una para convertir datos a escala Celsius y otra para convertir los datos a escala Fahrenheit. Ejemplo: Ingrese temperatura: 28.5 Ingrese escala: C Resultado: 83.3°F

"""

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def main():
    temp = float(input("Ingresa una temperatura: "))
    escala = input("Ingrese escala (C/F): ").strip().upper()

    if escala == "C":
        convertido = celsius_a_fahrenheit(temp)
        print(f"Resultado: {convertido:1f}°F")
    elif escala == "F":
        convertido = fahrenheit_a_celsius(temp)
        print(f"Resultado: {convertido:.1f}°C")
    else:
        print("Escala incorrecta. Use 'C' para Celsius o 'F' para Fahrenheit")
    
if __name__ == "__main__":
    main()