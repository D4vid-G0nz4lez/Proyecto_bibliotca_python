  """
    Representa una biblioteca con funcionalidades de gestión de libros y usuarios.

    Attributes:
        libros (dict): Un diccionario que almacena los libros de la biblioteca.
        usuarios (dict): Un diccionario que almacena los usuarios de la biblioteca.
    """
import pickle
from libro import Libro
from usuario import Usuario
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor)
        print(f"Libro '{titulo}' agregado/actualizado.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            print(libro)

    def prestar_libro(self, titulo, nombre_usuario):
        if titulo not in self.libros or not self.libros[titulo].disponible:
            print("Libro no disponible.")
            return
        if nombre_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        libro = self.libros[titulo]
        usuario = self.usuarios[nombre_usuario]
        libro.cantidad -= 1
        if libro.cantidad == 0:
            libro.disponible = False
        usuario.prestar_libro(libro)
        print(f"Libro '{titulo}' prestado a {nombre_usuario}.")

    def registrar_usuario(self, nombre):
        if nombre not in self.usuarios:
            self.usuarios[nombre] = Usuario(nombre)
            print(f"Usuario '{nombre}' registrado.")
        else:
            print("Usuario ya existe.")

    def listar_usuarios(self):
        for usuario in self.usuarios.values():
            print(usuario)

    def listar_libros_usuario(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            usuario = self.usuarios[nombre_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {nombre_usuario}:")
                for libro in usuario.libros_prestados:
                    print(libro.titulo)
            else:
                print(f"{nombre_usuario} no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")

    def devolver_libro(self, titulo, nombre_usuario):
        if nombre_usuario not in self.usuarios or titulo not in self.libros:
            print("Usuario o libro no encontrado.")
            return
        usuario = self.usuarios[nombre_usuario]
        libro = self.libros[titulo]
        if usuario.devolver_libro(libro):
            libro.cantidad += 1
            libro.disponible = True
            print(f"Libro '{titulo}' devuelto por {nombre_usuario}.")
        else:
            print(f"{nombre_usuario} no tenía prestado el libro '{titulo}'.")

    def guardar_datos(self):
        with open('datos_biblioteca.pkl', 'wb') as f:
            pickle.dump((self.libros, self.usuarios), f)

    def cargar_datos(self):
        try:
            with open('datos_biblioteca.pkl', 'rb') as f:
                self.libros, self.usuarios = pickle.load(f)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontraron datos previos. Iniciando con biblioteca vacía.")