class Inventario:


    def __init__(self):
        '''Se representa el inventario en una estructura con forma de lista, debido al orden de insercion '''

        self.producto = []

    def registrar_producto (self):
        '''Funcion que permite agregar productos al inventario'''
        print("\n[Inventario]")
        print("Registro del Producto pendiente")

    def listar_producto (self):
        '''Funcion que Lista o muestra ordenadamente el inventario'''
        print("\n[Inventario]")
        print("Listar Inventario pendiente")

    def buscar_producto (self):
        '''Busca un producto en el inventario'''
        print("\n[Inventario]")
        print("Buscar en el Inventario Pendiente")

    def eliminar_producto (self):
        '''Elimina un producto del inventario'''
        print("\n[Inventario]")
        print("Eliminar producto Pendiente")