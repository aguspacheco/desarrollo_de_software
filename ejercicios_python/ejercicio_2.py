#!/usr/bin/env python3
"""
Ejercicio 2: Modifique el programa anterior para que muestre “¡Hola <arg 1>!”. Donde arg 1 proviene de la lista de argumentos al ejecutar el programa. Por ejemplo, al ejecutar: python ejercicio_2.py firulais. El programa mostrará “¡Hola Firulais!”. Utilice métodos de string para “capitalizar” el argumento recibido por parámetros.
"""
import sys

def main():
    if len(sys.argv) < 2:
        print("Por favor ingresa un nombre como argumento")
        print("Ejemplo: python ejercicio_2.py pepito")
        return
    
    nombre = sys.argv[1].capitalize()
    print(f"Hola {nombre}!")

if __name__ == "__main__":
    main()