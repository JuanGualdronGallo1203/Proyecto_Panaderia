from data_funciones_json import cargar_datos, guardar_datos, generar_codigo, ARCHIVO_PEDIDOS, ARCHIVO_PRODUCTOS, datetime
from Productos import advertencia_stock_bajo

def advertencia_stock_bajo(producto):
    """
    Muestra una advertencia si el stock de un producto es menor o igual a 5.
    """
    if producto.get('cantidad_stock', 0) <= 5:  # Verifica si el stock del producto es bajo (<= 5).
        print(f"ADVERTENCIA: El producto '{producto.get('nombre', 'Desconocido')}' tiene un stock bajo ({producto['cantidad_stock']}). Necesita volver a comprar.")

def realizar_pedido():
    """
    Permite al usuario realizar un pedido y guarda los detalles en el archivo pedidos.json.
    """
    # Cargar datos existentes de productos y pedidos.
    pedidos = cargar_datos(ARCHIVO_PEDIDOS)  # Carga los datos de pedidos desde el archivo JSON.
    productos = cargar_datos(ARCHIVO_PRODUCTOS)  # Carga los datos de productos desde el archivo JSON.

    # Solicitar el código del pedido.
    while True:
        codigo_pedido = input("Ingrese el código del pedido: ").strip()  # Pide al usuario que ingrese un código de pedido.
        if not codigo_pedido:  # Valida que el código no esté vacío.
            print("El código del pedido no puede estar vacío. Intente de nuevo.")
            continue
        if codigo_pedido in pedidos:  # Valida que el código no esté duplicado.
            print(f"El código '{codigo_pedido}' ya está en uso. Por favor, ingrese otro código.")
            continue
        break  # Si el código es válido, sale del bucle.

    # Solicitar el código del cliente.
    codigo_cliente = input("Ingrese el código del cliente: ")  # Pide al usuario que ingrese el código del cliente.

    # Obtener la fecha y hora actual.
    fecha_pedido = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Genera la fecha y hora actual en formato legible.

    # Lista para almacenar los detalles del pedido.
    detalles_pedido = []  # Inicializa una lista vacía para almacenar los detalles del pedido.

    # Pedir productos hasta que el usuario ingrese 'fin'.
    numero_linea = 1  # Contador para numerar las líneas del pedido.
    while True:
        codigo_producto = input("Ingrese el código del producto (o 'fin' para terminar): ").strip()  # Pide el código del producto.
        if codigo_producto.lower() == "fin":  # Si el usuario ingresa 'fin', termina el ingreso de productos.
            break

        # Validar si el producto existe.
        if codigo_producto not in productos:  # Verifica si el producto existe en el archivo JSON.
            print(f"No se encontró el producto con código '{codigo_producto}'.")
            continue

        # Pedir cantidad del producto.
        while True:
            try:
                cantidad = int(input("Ingresá la cantidad del producto: "))  # Pide la cantidad del producto.
                break
            except ValueError:  # Maneja errores si el usuario no ingresa un número entero.
                print("Por favor, ingresá bien un número entero.")
                continue

        # Validar disponibilidad de stock.
        if cantidad > productos[codigo_producto]["cantidad_stock"]:  # Verifica si hay suficiente stock disponible.
            print(f"No hay suficiente stock disponible para el producto '{productos[codigo_producto]['nombre']}'.")
            continue

        # Obtener precio unitario del producto.
        precio_unitario = productos[codigo_producto]["precio_venta"]  # Obtiene el precio de venta del producto.

        # Agregar el detalle al pedido.
        detalles_pedido.append({
            "codigo_producto": codigo_producto,  # Código del producto.
            "cantidad": cantidad,  # Cantidad solicitada.
            "precio_unitario": precio_unitario,  # Precio unitario del producto.
            "numero_linea": numero_linea  # Número de línea dentro del pedido.
        })

        # Actualizar el stock del producto.
        productos[codigo_producto]["cantidad_stock"] -= cantidad  # Reduce el stock del producto según la cantidad pedida.

        # Mostrar advertencia si el stock es bajo.
        advertencia_stock_bajo(productos[codigo_producto])  # Llama a la función para verificar si el stock es bajo.

        # Incrementar el contador de línea.
        numero_linea += 1  # Incrementa el contador de línea para el siguiente producto.

    # Agregar el pedido al diccionario de pedidos.
    pedidos[codigo_pedido] = {
        "codigo_cliente": codigo_cliente,  # Código del cliente asociado al pedido.
        "fecha_pedido": fecha_pedido,  # Fecha y hora del pedido.
        "detalles_pedido": detalles_pedido  # Detalles del pedido (productos, cantidades, precios).
    }

    # Guardar cambios en los archivos JSON.
    guardar_datos(pedidos, ARCHIVO_PEDIDOS)  # Guarda los datos actualizados de pedidos en el archivo JSON.
    guardar_datos(productos, ARCHIVO_PRODUCTOS)  # Guarda los datos actualizados de productos en el archivo JSON.

    print(f"Pedido {codigo_pedido} realizado correctamente.")  # Notifica al usuario que el pedido fue registrado.

def mostrar_registros_pedido():
    """
    Muestra los detalles de un pedido específico.
    """
    pedidos = cargar_datos(ARCHIVO_PEDIDOS)  # Carga los datos de pedidos desde el archivo JSON.

    if not pedidos:  # Verifica si no hay pedidos registrados.
        print("No hay pedidos registrados.")
        return

    while True:
        codigo_pedido = input("Ingrese el código del pedido que desea ver: ").strip()  # Pide el código del pedido.
        if codigo_pedido in pedidos:  # Verifica si el pedido existe.
            pedido = pedidos[codigo_pedido]  # Obtiene los detalles del pedido.
            print(f"\nDetalles del Pedido {codigo_pedido}:")
            print(f"Código del Cliente: {pedido['codigo_cliente']}")
            print(f"Fecha del Pedido: {pedido['fecha_pedido']}")
            print("Productos:")
            for detalle in pedido["detalles_pedido"]:  # Itera sobre los detalles del pedido.
                print(f"  - Producto: {detalle['codigo_producto']}, Cantidad: {detalle['cantidad']}, Precio Unitario: {detalle['precio_unitario']}")
            break
        else:  # Si el pedido no existe, muestra un mensaje de error.
            print(f"No se encontró ningún pedido con el código '{codigo_pedido}'. Intente de nuevo.")

def modificar_pedido():
    """
    Permite modificar un pedido existente.
    """
    pedidos = cargar_datos(ARCHIVO_PEDIDOS)  # Carga los datos de pedidos desde el archivo JSON.

    if not pedidos:  # Verifica si no hay pedidos registrados.
        print("No hay pedidos registrados.")
        return

    while True:
        codigo_pedido = input("Ingrese el código del pedido que desea modificar: ").strip()  # Pide el código del pedido.
        if codigo_pedido in pedidos:  # Verifica si el pedido existe.
            pedido = pedidos[codigo_pedido]  # Obtiene los detalles del pedido.
            print(f"\nDetalles actuales del Pedido {codigo_pedido}:")
            print(f"Código del Cliente: {pedido['codigo_cliente']}")
            print(f"Fecha del Pedido: {pedido['fecha_pedido']}")
            print("Productos:")
            for detalle in pedido["detalles_pedido"]:  # Muestra los detalles actuales del pedido.
                print(f"  - Producto: {detalle['codigo_producto']}, Cantidad: {detalle['cantidad']}, Precio Unitario: {detalle['precio_unitario']}")

            # Permitir al usuario modificar los detalles del pedido.
            opcion_modificar = input("¿Desea modificar los productos del pedido? (s/n): ").strip().lower()
            if opcion_modificar == "s":
                nuevos_detalles = []  # Lista para almacenar los nuevos detalles del pedido.
                while True:
                    codigo_producto = input("Ingrese el código del producto a modificar (o 'fin' para terminar): ").strip()
                    if codigo_producto.lower() == "fin":
                        break

                    # Buscar el producto en el pedido.
                    encontrado = False
                    for detalle in pedido["detalles_pedido"]:
                        if detalle["codigo_producto"] == codigo_producto:
                            encontrado = True
                            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                            detalle["cantidad"] = nueva_cantidad
                            nuevos_detalles.append(detalle)
                            print(f"Producto '{codigo_producto}' modificado correctamente.")
                            break

                    if not encontrado:
                        print(f"No se encontró el producto '{codigo_producto}' en el pedido.")

                # Actualizar los detalles del pedido.
                pedido["detalles_pedido"] = nuevos_detalles

            # Guardar los cambios en el archivo JSON.
            guardar_datos(pedidos, ARCHIVO_PEDIDOS)
            print(f"Pedido {codigo_pedido} modificado correctamente.")
            break
        else:
            print(f"No se encontró ningún pedido con el código '{codigo_pedido}'. Intente de nuevo.")

def eliminar_pedido():
    """
    Elimina un pedido existente.
    """
    pedidos = cargar_datos(ARCHIVO_PEDIDOS)  # Carga los datos de pedidos desde el archivo JSON.

    if not pedidos:  # Verifica si no hay pedidos registrados.
        print("No hay pedidos registrados.")
        return

    while True:
        codigo_pedido = input("Ingrese el código del pedido que desea eliminar: ").strip()  # Pide el código del pedido.
        if codigo_pedido in pedidos:  # Verifica si el pedido existe.
            del pedidos[codigo_pedido]  # Elimina el pedido del diccionario.
            guardar_datos(pedidos, ARCHIVO_PEDIDOS)  # Guarda los cambios en el archivo JSON.
            print(f"Pedido {codigo_pedido} eliminado correctamente.")
            break
        else:
            print(f"No se encontró ningún pedido con el código '{codigo_pedido}'. Intente de nuevo.")


def filtrar_pedidos():
    """
    Filtra los pedidos por el código del pedido y muestra la información hasta el precio unitario.
    """
    pedidos = cargar_datos(ARCHIVO_PEDIDOS)

    if not pedidos:
        print("No hay pedidos registrados.")
        return

    # Solicitar al usuario el código del pedido
    codigo_pedido = input("Ingrese el código del pedido a buscar: ")

    # Verificar si el pedido existe
    if codigo_pedido in pedidos:
        pedido = pedidos[codigo_pedido]
        print(f"\nDetalles del pedido '{codigo_pedido}':")
        
        # Mostrar información general del pedido
        print(f"Código del Cliente: {pedido.get('codigo_cliente', 'No disponible')}")
        print(f"Fecha del Pedido: {pedido.get('fecha_pedido', 'No disponible')}")
        print("\nProductos:")

        # Obtener la lista de productos (o una lista vacía si no existe)
        productos = pedido.get("productos", [])

        # Depuración: Imprimir la lista de productos para verificar su contenido
        print("Debug: Lista de productos cargada:", productos)

        # Verificar si hay productos
        if isinstance(productos, list) and productos:
            for producto in productos:
                print(f"- Código Producto: {producto.get('codigo_producto', 'No disponible')}")
                print(f"  Nombre Producto: {producto.get('nombre_producto', 'No disponible')}")
                print(f"  Cantidad: {producto.get('cantidad', 'No disponible')}")
                print(f"  Precio Unitario: {producto.get('precio_unitario', 'No disponible')}")
                print("-" * 40)
        else:
            print("Este pedido no tiene productos asociados o la clave 'productos' no es una lista válida.")
    else:
        print(f"No se encontró ningún pedido con el código '{codigo_pedido}'.")

def gestionar_pedidos(menu_pedidos):
    """Menú para gestionar pedidos."""
    while True:
        try:
            print(menu_pedidos)
            opc_pedido = int(input("Ingrese la opcion que desea: "))
            if opc_pedido == 1:
                realizar_pedido()
            elif opc_pedido == 2:
                mostrar_registros_pedido()
            elif opc_pedido == 3:
                modificar_pedido()
            elif opc_pedido == 4:
                eliminar_pedido()
            elif opc_pedido == 5:
                filtrar_pedidos()
            elif opc_pedido == 6:
                break  # Volver al menú principal
            else:
                print("ESA OPCION NO ES VALIDA, POR FAVOR INTENTE DE NUEVO!!!!")
        except ValueError:
            print("Por favor ingrese un número válido.")