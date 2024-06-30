    """

    Representa un usuario de la biblioteca.

    Attributes:
        nombre (str): El nombre del usuario.
        libros_prestados (list): Una lista de los libros prestados al usuario.

        
    """


class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            return True
        return False

    def __str__(self):
        return f"Usuario: {self.nombre}, Libros prestados: {len(self.libros_prestados)}"