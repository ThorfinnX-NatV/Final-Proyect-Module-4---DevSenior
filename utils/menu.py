def mostrar_menu():
    print("\n")
    print(("=" * 50))
    print("         SISTEMA DE MANTENIMIENTO DEV-STORE")
    print("                 SEAS BIENVENIDO")
    print(("=" * 50))
    print("1. Registrar Producto")
    print("2. Listar los Productos")
    print("3. Buscar un Producto")
    print("4. Eliminar un Producto")                                ##Unica Responsabilidad
    print("5. Registrer una Venta")
    print("6. Mostrar Ventas")
    print("7. Mostrar Total Vendido")
    print("8. Salir del Sistema")

    opcion = input("\nSeleccione una opcion del sistema:")
    return opcion 

mostrar_menu()