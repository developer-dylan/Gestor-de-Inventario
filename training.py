# Sección de datos y contador de IDs
inventario = {}        # Diccionario que almacenará los productos
id_actual = 1        # ID que se incrementa con cada nuevo producto
deleted_products = [] # Lista para almacenar productos eliminados

# Buscar ID por nombre
def obtener_id_por_nombre(nombre): 
    for id, datos in inventario.items():
        if datos["nombre"] == nombre:
            return id
    return None

# Añadir producto con ID único
def añadir_producto(nombre, precio, cantidad):
    global id_actual
    if any(producto["nombre"] == nombre for producto in inventario.values()):
        print(" El producto ya existe.")
    else:
        inventario[id_actual] = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        print(f" Producto '{nombre}' añadido con ID {id_actual}.")
        id_actual += 1

# Consultar producto por nombre
def consultar_producto(nombre):
    id_producto = obtener_id_por_nombre(nombre)
    if id_producto:
        datos = inventario[id_producto]
        print(f"ID: {id_producto} | {datos['nombre']} → Precio: ${datos['precio']:>10,.0f} | Cantidad: {datos['cantidad']:>10,.0f}")
    else:
        print(" Producto no encontrado.")

# Actualizar precio de un producto
def actualizar_precio(nombre, nuevo_precio):
    id_producto = obtener_id_por_nombre(nombre)
    if id_producto:
        inventario[id_producto]["precio"] = nuevo_precio
        print(" Precio actualizado.")
    else:
        print(" Producto no encontrado.")

# Eliminar producto por nombre
def eliminar_producto(nombre):
    global id_actual
    id_producto = obtener_id_por_nombre(nombre)
    if id_producto:
        # Guardar el producto eliminado en la lista
        deleted_products.append({
            "id": id_producto,
            "nombre": inventario[id_producto]["nombre"],
            "precio": inventario[id_producto]["precio"],
            "cantidad": inventario[id_producto]["cantidad"]
        })
        # Eliminar el producto
        del inventario[id_producto]
        print(f" Producto '{nombre}' eliminado.")
    else:
        print(" Producto no encontrado.")

def lista_prod_eliminados():
    if not deleted_products:
        print ("No hay productos eliminados.")
    else:
        print("Productos eliminados:")
        print ("\n")
        for producto in deleted_products:
            print(f"ID: {producto['id']} | {producto['nombre']} | Precio: ${producto['precio']:>10,.0f} | Cantidad: {producto['cantidad']:>10,.0f}")

# Calcular valor total usando lambda
def calcular_valor_total():
    total = sum(map(lambda p: p["precio"] * p["cantidad"], inventario.values()))
    print(f" Valor total del inventario: ${total:>10,.0f}")

# Validar número ingresado
def pedir_precio(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor < 0:
                print("Ingresa un número positivo.")
            else:
                return valor
        except ValueError:
            print("Ingresa un número válido.")

# Menú principal del programa
def mostrar_menu():
    while True:
        print("\n------ MENÚ DE INVENTARIO ------")
        print ("\n")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total")
        print("6. Mostrar todos los productos")
        print("0. Salir")
        print ("\n")

        opcion = input("Selecciona una opción (1-6 ó 0 PARA SALIR): ")
        print ("\n")

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip().upper()
            precio =pedir_precio("Precio del producto: ")
            cantidad =pedir_precio("Cantidad disponible: ")
            print ("\n")
            añadir_producto(nombre, precio, cantidad)

        elif opcion == "2":
            if not inventario:
                print("No hay productos en el inventario.")
                mostrar_menu()
            else:
                inventario
            nombre = input("Nombre del producto a consultar: ").strip().upper()
            consultar_producto(nombre)

        elif opcion == "3":
            if not inventario:
                print("No hay productos en el inventario.")
                mostrar_menu()
            else:
                nombre = input("Nombre del producto a actualizar: ").strip().upper()
                nuevo_precio =pedir_precio("Nuevo precio: ")
                actualizar_precio(nombre, nuevo_precio)

        elif opcion == "4":
            if not inventario:
                print("No hay productos en el inventario.")
                mostrar_menu()
            else:
                nombre = input("Nombre del producto a eliminar: ").strip().upper()
                eliminar_producto(nombre)

        elif opcion == "5":
            calcular_valor_total()

        elif opcion == "6":
            if not inventario: 
                print("No hay productos en el inventario.")
                mostrar_menu()
            else: 
                inventario
                print("\nInventario completo:")
                for id, datos in inventario.items():
                    print(f"ID: {id} | {datos['nombre'].title()} | Precio: ${datos['precio']:>10,.0f} | Cantidad: {datos['cantidad']:>10,.0f}")

                ver_eliminados = input("\n¿Deseas ver también los productos eliminados? (S/N): ").strip().upper()
                print ("\n")
                if ver_eliminados == "S":
                    lista_prod_eliminados()
                else: 
                    ver_eliminados == "N"
                    mostrar_menu()

        elif opcion == "0":
            print("Programa finalizado. ¡Hasta luego!")
            ingresar_al_programa =  input("\n¿Deseas ingresar al programa? (S/N): ").strip().upper()
            print ("\n")
            if ingresar_al_programa == "S":
                mostrar_menu()
            else:
                ingresar_al_programa == "N"
                print("Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

mostrar_menu()
