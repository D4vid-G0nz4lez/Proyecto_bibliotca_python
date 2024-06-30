from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


def mostrar_menu():
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar Libro")
    print("2. Mostrar Libros")
    print("3. Prestar Libro")
    print("4. Registrar Usuario")
    print("5. Listar Usuarios")
    print("6. Listar Libros de Usuario")
    print("7. Devolver Libro")
    print("8. Guardar Datos")
    print("9. Salir")

def main():
    biblioteca = Biblioteca()
    biblioteca.cargar_datos()  # Intenta cargar datos previos

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblioteca.agregar_libro(titulo, autor)
        elif opcion == "2":
            biblioteca.mostrar_libros()
        elif opcion == "3":
            titulo = input("Ingrese el título del libro a prestar: ")
            usuario = input("Ingrese el nombre del usuario: ")
            biblioteca.prestar_libro(titulo, usuario)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del nuevo usuario: ")
            biblioteca.registrar_usuario(nombre)
        elif opcion == "5":
            biblioteca.listar_usuarios()
        elif opcion == "6":
            usuario = input("Ingrese el nombre del usuario: ")
            biblioteca.listar_libros_usuario(usuario)
        elif opcion == "7":
            titulo = input("Ingrese el título del libro a devolver: ")
            usuario = input("Ingrese el nombre del usuario: ")
            biblioteca.devolver_libro(titulo, usuario)
        elif opcion == "8":
            biblioteca.guardar_datos()
            print("Datos guardados exitosamente.")
        elif opcion == "9":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()