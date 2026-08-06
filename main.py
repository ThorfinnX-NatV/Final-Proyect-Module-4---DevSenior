from utils.menu import mostrar_menu
from services.inventario import Inventario
from services.ventas import Ventas

def main():
    #Dependencias de la clase Main
    inventario = Inventario()           #Instanciar
    ventas = Ventas()                   #Clases Inventario y Ventas

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            inventario.registrar_producto()

        elif opcion == "2":
            inventario.listar_producto()

        elif opcion == "3":
            inventario.buscar_producto()

        elif opcion == "4":
            inventario.eliminar_producto()

        elif opcion == "5":
            ventas.registrar_ventas()

        elif opcion == "6":
            ventas.listar_ventas()

        elif opcion == "7":
            ventas.total_vendido()

        elif opcion == "8":
            print("Saliendo del Sistma")
            break 

        else:
            print("La opcion no esta Disponble en el sistema")

main()