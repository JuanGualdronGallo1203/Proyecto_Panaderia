from data_funciones_json import cargar_datos, guardar_datos, ARCHIVO_PRODUCTOS

def advertencia_stock_bajo(producto):
    """
    Muestra una advertencia si el stock de un producto es menor o igual a 5.
    """
    if producto.get("cantidad_stock", 0) <= 5:
        print(f"ADVERTENCIA: El producto '{producto.get('nombre', 'Desconocido')}' tiene un stock bajo ({producto['cantidad_stock']}). Necesita volver a comprar.")

def registrar_producto():
    """
    Registra un nuevo producto con los campos en el orden especificado.
    """
    productos = cargar_datos(ARCHIVO_PRODUCTOS)

    # Solicitar el código del producto
    codigo_producto = input("Ingrese el código del producto: ")
    if codigo_producto in productos:
        print(f"El producto con código '{codigo_producto}' ya existe.")
        return

    # Solicitar los demás datos del producto en el orden especificado
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")  # Nuevo campo
    nombre_proveedor = input("Ingrese el nombre del proveedor: ")  # Nuevo campo
    while True:
        try:
            cantidad_stock = int(input("Ingrese la cantidad en stock: "))
            break
        except ValueError:
            print("Por favor, lea bien e ingrese un numero")
            continue 

    while True:
        try:
            precio_venta = float(input("Ingrese el precio de proveedor: "))  # Nuevo campo
            break
        except ValueError:
            print("Por favor, lea bien e ingrese un numero")
            continue 

    while True:
        try:
            precio_proveedor = float(input("Ingrese el precio de venta: "))
            break
        except ValueError:
            print("Por favor, lea bien e ingrese un numero")
            continue 
    

    # Crear el diccionario del producto en el orden especificado
    productos[codigo_producto] = {
        "nombre": nombre,
        "descripcion": descripcion,
        "nombre_proveedor": nombre_proveedor,
        "cantidad_stock": cantidad_stock,
        "precio_venta": precio_venta,
        "precio_proveedor": precio_proveedor
    }

    # Guardar los datos en el archivo JSON
    guardar_datos(productos, ARCHIVO_PRODUCTOS)
    print(f"Producto '{nombre}' registrado correctamente.")

def informacion_productos():
    """
    Muestra la información de todos los productos en el orden especificado.
    """
    productos = cargar_datos(ARCHIVO_PRODUCTOS)

    if not productos:
        print("No hay productos registrados.")
        return

    print("Lista de productos:")
    for codigo, producto in productos.items():
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Proveedor: {producto['nombre_proveedor']}")
        print(f"Stock: {producto['cantidad_stock']}")
        print(f"Precio de Venta: {producto['precio_venta']}")
        print(f"Precio de Proveedor: {producto['precio_proveedor']}")
        print("-" * 40)

def eliminar_producto():
    """Elimina un producto existente."""
    productos = cargar_datos(ARCHIVO_PRODUCTOS)
    
    codigo_producto = input("Ingrese el código del producto a eliminar: ")
    if codigo_producto not in productos:
        print(f"No se encontró el producto con código '{codigo_producto}'.")
        return
    
    del productos[codigo_producto]
    guardar_datos(productos, ARCHIVO_PRODUCTOS)
    print(f"Producto '{codigo_producto}' eliminado correctamente.")

def buscar_producto():
    """
    Busca un producto por código, nombre o descripción y muestra sus detalles.
    """
    productos = cargar_datos(ARCHIVO_PRODUCTOS)

    if not productos:
        print("No hay productos registrados.")
        return

    # Preguntar al usuario qué criterio desea usar para buscar
    print("Seleccione el criterio de búsqueda:")
    print("1. Código del producto")
    print("2. Nombre del producto")
    print("3. Descripción del producto")
    try:
        opcion_busqueda = int(input("Ingrese el número de la opción deseada: "))
    except ValueError:
        print("Por favor ingrese un número válido.")
        return

    # Inicializar variables para la búsqueda
    encontrado = False

    if opcion_busqueda == 1:  # Búsqueda por código
        codigo_producto = input("Ingrese el código del producto a buscar: ")
        if codigo_producto in productos:
            producto = productos[codigo_producto]
            encontrado = True
        else:
            print(f"No se encontró ningún producto con el código '{codigo_producto}'.")
    
    elif opcion_busqueda == 2:  # Búsqueda por nombre
        nombre_producto = input("Ingrese el nombre del producto a buscar: ").lower()
        for codigo, producto in productos.items():
            if producto["nombre"].lower() == nombre_producto:
                encontrado = True
                print(f"Información del producto '{codigo}':")
                print(f"Nombre: {producto['nombre']}")
                print(f"Descripción: {producto['descripcion']}")
                print(f"Proveedor: {producto['nombre_proveedor']}")
                print(f"Stock: {producto['cantidad_stock']}")
                print(f"Precio de Venta: {producto['precio_venta']}")
                print(f"Precio de Proveedor: {producto['precio_proveedor']}")
                print("-" * 40)
        if not encontrado:
            print(f"No se encontró ningún producto con el nombre '{nombre_producto}'.")

    elif opcion_busqueda == 3:  # Búsqueda por descripción
        descripcion_producto = input("Ingrese la descripción del producto a buscar: ").lower()
        for codigo, producto in productos.items():
            if descripcion_producto in producto["descripcion"].lower():
                encontrado = True
                print(f"Información del producto '{codigo}':")
                print(f"Nombre: {producto['nombre']}")
                print(f"Descripción: {producto['descripcion']}")
                print(f"Proveedor: {producto['nombre_proveedor']}")
                print(f"Stock: {producto['cantidad_stock']}")
                print(f"Precio de Venta: {producto['precio_venta']}")
                print(f"Precio de Proveedor: {producto['precio_proveedor']}")
                print("-" * 40)
        if not encontrado:
            print(f"No se encontró ningún producto con la descripción '{descripcion_producto}'.")

    else:
        print("Opción no válida. Por favor, intente de nuevo.")

    # Si se encontró un producto por código, mostrar sus detalles
    if opcion_busqueda == 1 and encontrado:
        print(f"Información del producto '{codigo_producto}':")
        print(f"Nombre: {producto['nombre']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Proveedor: {producto['nombre_proveedor']}")
        print(f"Stock: {producto['cantidad_stock']}")
        print(f"Precio de Venta: {producto['precio_venta']}")
        print(f"Precio de Proveedor: {producto['precio_proveedor']}")

def gestionar_productos(menu_productos):
    """Menú para gestionar productos."""
    while True:
        try:
            print(menu_productos)
            opc_producto = int(input("Ingrese la opcion que desea: "))
            if opc_producto == 1:
                registrar_producto()
            elif opc_producto == 2:
                informacion_productos()
            elif opc_producto == 3:
                eliminar_producto()
            elif opc_producto == 4:
                buscar_producto()
            elif opc_producto == 5:
                break  # Volver al menú principal
            else:
                print("ESA OPCION NO ES VALIDA, POR FAVOR INTENTE DE NUEVO!!!!")
        except ValueError:
            print("Por favor ingrese un número válido.")
