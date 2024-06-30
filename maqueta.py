class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("Harry Potter", "J.K. Rowling")

def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("Harry Potter", "J.K. Rowling")
biblioteca.mostrar_libros()

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca
        if titulo_libro not in self.libros:
            print(f"El libro '{titulo_libro}' no está disponible en la biblioteca.")
            return
        
        # Verificar si el libro está disponible
        if not self.libros[titulo_libro]['disponible']:
            print(f"El libro '{titulo_libro}' no está disponible para prestar en este momento.")
            return
        
        # Verificar si el usuario está registrado
        if nombre_usuario not in self.usuarios:
            print(f"El usuario '{nombre_usuario}' no está registrado en la biblioteca.")
            return
        
        # Prestar el libro al usuario
        self.libros[titulo_libro]['disponible'] = False
        print(f"El libro '{titulo_libro}' ha sido prestado a '{nombre_usuario}'.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("Harry Potter", "J.K. Rowling")
biblioteca.registrar_usuario("Usuario1")
biblioteca.prestar_libro("Harry Potter", "Usuario1")
biblioteca.mostrar_libros()

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca
        if titulo_libro not in self.libros:
            print(f"El libro '{titulo_libro}' no está disponible en la biblioteca.")
            return
        
        # Verificar si el libro está disponible
        if not self.libros[titulo_libro]['disponible']:
            print(f"El libro '{titulo_libro}' no está disponible para prestar en este momento.")
            return
        
        # Verificar si el usuario está registrado
        if nombre_usuario not in self.usuarios:
            print(f"El usuario '{nombre_usuario}' ha sido registrado en la biblioteca.")
            self.usuarios[nombre_usuario] = []
        else:
            print(f"El usuario '{nombre_usuario}' ya está registrado en la biblioteca.")

    def registrar_usuario(self, nombre_usuario):
        # Verificar si el usuario ya está registrado
        if nombre_usuario not in self.usuarios:
            print(f"El usuario '{nombre_usuario}' ha sido registrado en la biblioteca.")
            self.usuarios[nombre_usuario] = []
        else:
            print(f"El usuario '{nombre_usuario}' ya está registrado en la biblioteca.")


# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.registrar_usuario("Usuario1")


import pickle

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca y si está disponible
        # Lógica de prestamo de libro...

    def registrar_usuario(self, nombre_usuario):
        # Verificar si el usuario ya está registrado
        # Lógica de registro de usuario...

    def guardar_datos(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump((self.libros, self.usuarios), f)
        print("Datos de la biblioteca guardados correctamente.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.agregar_libro("Harry Potter", "J.K. Rowling")
biblioteca.guardar_datos("datos_biblioteca.pkl")


import pickle

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca y si está disponible
        # Lógica de prestamo de libro...

    def registrar_usuario(self, nombre_usuario):
        # Verificar si el usuario ya está registrado
        # Lógica de registro de usuario...

    def guardar_datos(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump((self.libros, self.usuarios), f)
        print("Datos de la biblioteca guardados correctamente.")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.libros, self.usuarios = pickle.load(f)
            print("Datos de la biblioteca cargados correctamente.")
        except FileNotFoundError:
            print("El archivo de datos no existe. Inicializando la biblioteca como vacía.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.cargar_datos("datos_biblioteca.pkl")

  #Implementar la lógica para listar los usuarios
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca y si está disponible
        # Lógica de prestamo de libro...

    def registrar_usuario(self, nombre_usuario):
        # Verificar si el usuario ya está registrado
        # Lógica de registro de usuario...

    def guardar_datos(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump((self.libros, self.usuarios), f)
        print("Datos de la biblioteca guardados correctamente.")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.libros, self.usuarios = pickle.load(f)
            print("Datos de la biblioteca cargados correctamente.")
        except FileNotFoundError:
            print("El archivo de datos no existe. Inicializando la biblioteca como vacía.")

    def listar_usuarios(self):
        print("Usuarios registrados en la biblioteca:")
        for usuario in self.usuarios:
            print(usuario)

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.registrar_usuario("Usuario1")
biblioteca.listar_usuarios()

 # Implementar la lógica para listar los libros de un usuario específico

 class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca y si está disponible
        # Lógica de prestamo de libro...

    def registrar_usuario(self, nombre_usuario):
        # Verificar si el usuario ya está registrado
        # Lógica de registro de usuario...

    def guardar_datos(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump((self.libros, self.usuarios), f)
        print("Datos de la biblioteca guardados correctamente.")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.libros, self.usuarios = pickle.load(f)
            print("Datos de la biblioteca cargados correctamente.")
        except FileNotFoundError:
            print("El archivo de datos no existe. Inicializando la biblioteca como vacía.")

    def listar_usuarios(self):
        print("Usuarios registrados en la biblioteca:")
        for usuario in self.usuarios:
            print(usuario)

    def listar_libros_usuario(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            libros_prestados = self.usuarios[nombre_usuario]
            if libros_prestados:
                print(f"Libros prestados a {nombre_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"{nombre_usuario} no tiene libros prestados en este momento.")
        else:
            print(f"El usuario {nombre_usuario} no está registrado en la biblioteca.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.registrar_usuario("Usuario1")
biblioteca.agregar_libro("Harry Potter", "J.K. Rowling")
biblioteca.prestar_libro("Harry Potter", "Usuario1")
biblioteca.listar_libros_usuario("Usuario1")


# Implementar la lógica para devolver un libro

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        # Verificar si el libro ya existe en la biblioteca
        if titulo in self.libros:
            # Si el libro ya existe, aumentar su cantidad en uno
            self.libros[titulo]['cantidad'] += 1
        else:
            # Si el libro no existe, agregarlo con una cantidad inicial de 1
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}
        print(f"El libro '{titulo}' de {autor} ha sido agregado a la biblioteca.")

    def mostrar_libros(self):
        print("Libros en la biblioteca:")
        for titulo, info in self.libros.items():
            disponible = "Disponible" if info['disponible'] else "No disponible"
            print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad: {info['cantidad']}, Disponibilidad: {disponible}")

    def prestar_libro(self, titulo_libro, nombre_usuario):
        # Verificar si el libro está en la biblioteca y si está disponible
        # Lógica de prestamo de libro...

    def registrar_usuario(self, nombre_usuario):
        # Verificar si el usuario ya está registrado
        # Lógica de registro de usuario...

    def guardar_datos(self, archivo):
        with open(archivo, 'wb') as f:
            pickle.dump((self.libros, self.usuarios), f)
        print("Datos de la biblioteca guardados correctamente.")

    def cargar_datos(self, archivo):
        try:
            with open(archivo, 'rb') as f:
                self.libros, self.usuarios = pickle.load(f)
            print("Datos de la biblioteca cargados correctamente.")
        except FileNotFoundError:
            print("El archivo de datos no existe. Inicializando la biblioteca como vacía.")

    def listar_usuarios(self):
        print("Usuarios registrados en la biblioteca:")
        for usuario in self.usuarios:
            print(usuario)

    def listar_libros_usuario(self, nombre_usuario):
        if nombre_usuario in self.usuarios:
            libros_prestados = self.usuarios[nombre_usuario]
            if libros_prestados:
                print(f"Libros prestados a {nombre_usuario}:")
                for libro in libros_prestados:
                    print(libro)
            else:
                print(f"{nombre_usuario} no tiene libros prestados en este momento.")
        else:
            print(f"El usuario {nombre_usuario} no está registrado en la biblioteca.")

    def devolver_libro(self, titulo_libro, nombre_usuario):
        if nombre_usuario in self.usuarios:
            libros_prestados = self.usuarios[nombre_usuario]
            if titulo_libro in libros_prestados:
                libros_prestados.remove(titulo_libro)
                self.libros[titulo_libro]['disponible'] = True
                print(f"El libro '{titulo_libro}' ha sido devuelto por '{nombre_usuario}'.")
            else:
                print(f"El usuario '{nombre_usuario}' no tiene prestado el libro '{titulo_libro}'.")
        else:
            print(f"El usuario '{nombre_usuario}' no está registrado en la biblioteca.")

# Ejemplo de uso
biblioteca = Biblioteca()
biblioteca.registrar_usuario("Usuario1")
biblioteca.agregar_libro("Harry Potter", "J.K. Rowling")
biblioteca.prestar_libro("Harry Potter", "Usuario1")
biblioteca.devolver_libro("Harry Potter", "Usuario1")
biblioteca.mostrar_libros()
