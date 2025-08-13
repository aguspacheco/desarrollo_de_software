#!/usr/bin/env python3

"""
Ejercicio 5. Escriba un programa que permita crear una lista de 5 películas. El programa debe solicitar uno por uno los nombres de las películas junto con su año de estreno. Al finalizar la carga de datos, se deberá mostrar por pantalla una lista con los nombres de las películas ordenadas por nombre y un diccionario donde las claves sean los años de estreno y los valores sean las películas estrenadas ese año. Ejemplo: ... Ingrese nombre de pelicula: Batman inicia Ingrese año de estreno: 2008 Resultado: [“300”, “Avatar”, “Batman Inicia”, “Iron Man”, “Tropic Thunder”] {2005: “Batman Inicia”, 2006: “300”, 2008: “Tropic Thunder”, “Iron Man”}

"""
def main():
    peliculas = []
    peliculas_por_anio = {}

    for i in range(5):
        nombre = input(f"Ingrese nombre de la pelicula {i+1}: ").strip().title()
        anio = int(input(f"Ingrese año de estreno de '{nombre}':"))

        peliculas.append(nombre)

        if anio in peliculas_por_anio:
            peliculas_por_anio[anio].append(nombre)
        else:
            peliculas_por_anio[anio] = [nombre]
    print("\nLista ordenada de peliculas:")
    print(sorted(peliculas))

    print("\nPeliculas por año:")
    for anio, nombres in peliculas_por_anio.items():
        if len(nombres) == 1:
            print(f"{anio}: {', '.join(nombres)}")

if __name__ == "__main__":
    main()