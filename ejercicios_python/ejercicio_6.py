#!/usr/bin/env python3
"""
Ejercicio 6. Cree un programa con las siguientes características:
a. Crea una clase llamada “Libro” con los siguientes atributos:
i. titulo
ii. autor
iii. año
iv. genero
b. Utiliza la el método __init__ para inicializar los atributos
c. Agrega un método llamado obtener_info() que devuelva una
cadena con algún formato para los detalles del libro (titulo, autor,
año, género).
d. Agrega un método es_clasico() que devuelva True si el libro se
publicó hace más de 50 años (basado en el año actual) y False en
caso contrario.
e. Crear objetos:
i. Instanciar al menos dos libros con diferentes atributos.
ii. Llama al método obtener_info() de cada libro para mostrar sus
detalles.
iii. Llama al método es_clasico() de cada libro e imprimir si cada
libro es un clásico.

6. Para determinar el año actual pueden solicitarlo al comenzar el
programa o bien obtenerlo utilizando el módulo datetime.

Ejemplo:
from datetime import date
hoy = date.today()
print(f“Año actual: {hoy.year}”) # muestra: 2024
"""

from datetime import date

class Libro:
    def __init__(self, titulo, autor, anio, genero):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero

    def obtener_info(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Año: {self.anio} | Género: {self.genero}"

    def es_clasico(self):
        anio_actual = date.today().year
        return (anio_actual - self.anio) > 50

def main():
    # Instanciar libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Novela")
    libro2 = Libro("El Código Da Vinci", "Dan Brown", 2003, "Thriller")

    # Mostrar info de cada libro
    print(libro1.obtener_info())
    print("¿Es clásico?", "Sí" if libro1.es_clasico() else "No")

    print(libro2.obtener_info())
    print("¿Es clásico?", "Sí" if libro2.es_clasico() else "No")

if __name__ == "__main__":
    main()
