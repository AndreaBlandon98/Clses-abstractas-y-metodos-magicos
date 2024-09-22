class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} por {self.autor}"

    def __repr__(self):
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"


libro1 = Libro("Asi hablo Zaratustra", "Friedrich Nietzscche", 560)
libro2 = Libro("La muerte de platon", "Marcos Chicot", 944)

print(libro1)
print(libro2)

print(repr(libro1))
print(repr(libro2))