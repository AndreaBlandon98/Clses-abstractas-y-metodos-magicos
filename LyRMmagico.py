from abc import ABC, abstractmethod


class Publicacion(ABC):
    def __init__(self, titulo):
        self.titulo = titulo

    def informacion(self):
        pass

    def resumen(self):
        pass

    def __str__(self):
        return f"Tipo de publicación: Publicación genérica"


class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo)
        self.autor = autor
        self.paginas = paginas

    def informacion(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

    def resumen(self):
        return f"Este libro titulado '{self.titulo}' fue escrito por {self.autor} y tiene {self.paginas} páginas."

    def __str__(self):
        return f"Tipo de publicación: Libro, Título: {self.titulo}"


class Revista(Publicacion):
    def __init__(self, titulo, edicion, mes):
        super().__init__(titulo)
        self.edicion = edicion
        self.mes = mes

    def informacion(self):
        return f"Revista: {self.titulo}, Edición: {self.edicion}, Mes: {self.mes}"

    def resumen(self):
        return f"La revista '{self.titulo}' de la edición {self.edicion} corresponde al mes de {self.mes}."

    def __str__(self):
        return f"Tipo de publicación: Revista, Título: {self.titulo}"


libro = Libro("El señor de los anillos", "J.R.R. Tolkien", 1178)
print(libro)


revista = Revista("National Geographic", "Vol. 500", "Septiembre")
print(revista)


