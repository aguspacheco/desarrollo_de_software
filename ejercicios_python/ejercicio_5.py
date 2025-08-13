#!/usr/bin/env python3

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