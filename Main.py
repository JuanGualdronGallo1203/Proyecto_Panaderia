from Menu import menu_principal, menu_productos, menu_pedidos  # Importa los menús desde el archivo Menu.py.
from Productos import *  # Importa todas las funciones relacionadas con productos desde Productos.py.
from Pedidos import *  # Importa todas las funciones relacionadas con pedidos desde Pedidos.py.

def main():
    """
    Función principal que controla el flujo del programa.
    """
    while True:  # Bucle infinito para mantener el programa en ejecución hasta que el usuario decida salir.
        print(menu_principal)  # Muestra el menú principal al usuario.
        opcion = input("Seleccione una opción: ").strip()  # Solicita al usuario que seleccione una opción.

        if opcion == "1":  # Opción 1: Gestionar Productos.
            while True:  # Bucle para el submenú de productos.
                print(menu_productos)  # Muestra el menú de productos.
                opcion_productos = input("Seleccione una opción: ").strip()  # Solicita al usuario que seleccione una opción.

                if opcion_productos == "1":  # Registrar un producto.
                    registrar_producto()
                elif opcion_productos == "2":  # Información de los productos.
                    informacion_productos()
                elif opcion_productos == "3":  # Eliminar un producto.
                    eliminar_producto()
                elif opcion_productos == "4":  # Buscar producto.
                    buscar_producto()
                elif opcion_productos == "5":  # Volver al menú principal.
                    break
                else:  # Opción inválida.
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == "2":  # Opción 2: Gestionar Pedidos.
            while True:  # Bucle para el submenú de pedidos.
                print(menu_pedidos)  # Muestra el menú de pedidos.
                opcion_pedidos = input("Seleccione una opción: ").strip()  # Solicita al usuario que seleccione una opción.

                if opcion_pedidos == "1":  # Realizar un pedido.
                    realizar_pedido()
                elif opcion_pedidos == "2":  # Registro de productos dentro del pedido.
                    mostrar_registros_pedido()
                elif opcion_pedidos == "3":  # Modificar un pedido.
                    modificar_pedido()
                elif opcion_pedidos == "4":  # Eliminar un pedido.
                    eliminar_pedido()
                elif opcion_pedidos == "5":  # Filtrar pedidos.
                    filtrar_pedidos()
                elif opcion_pedidos == "6":  # Volver al menú principal.
                    break
                else:  # Opción inválida.
                    print("Opción inválida. Intente de nuevo.")

        elif opcion == "3":  # Opción 3: Salir del Programa.
            print("Saliendo del programa...")  # Notifica al usuario que está saliendo.
            break  # Sale del bucle principal y termina el programa.

        else:  # Opción inválida en el menú principal.
            print("Opción inválida. Intente de nuevo.")  # Notifica al usuario que ingresó una opción incorrecta.

if __name__ == "__main__":
    main()  # Ejecuta la función principal cuando se inicia el programa.