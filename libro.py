    """
    Representa un libro en la biblioteca.

    Attributes:
        titulo (str): El título del libro.
        autor (str): El autor del libro.
        cantidad (int): La cantidad de copias disponibles del libro.
        disponible (bool): Indica si el libro está disponible para préstamo.
    
    """
class Libro:
    def __init__(self, titulo, autor, cantidad=1):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = True

    def __str__(self):
        return f"{self.titulo} por {self.autor} - Cantidad: {self.cantidad}, {'Disponible' if self.disponible else 'No disponible'}"


