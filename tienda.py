import CRUD as conn
from Mantenimiento_productos1 import Productos
from procesoCompra import ProcesoCompra
from mantenimiento_categorias import Categorias
from mantenimiento_clientes import Usuarios  # Importamos la clase Usuarios
from mantenimiento_ventas import Ventas  # Importamos la clase Ventas

db = conn.Database()

class MenuInicio:
    def __init__(self):
        pass

    def mostrar_menu_inicio(self):
        while True:
            print("\t===============================")
            print("Sistema de administración y ventas | Tienda de juguetes")
            print("\t===============================")
            print("[1] Proceso de compra")
            print("[2] Servicios administrativos")
            print("[3] Salir")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    proceso_compra = ProcesoCompra()  
                    proceso_compra.mostrar_menu_proceso_compra()  
                elif option == 2:
                    menu_categorias = MenuCategorias()
                    menu_categorias.mostrar_menu_categorias()
                elif option == 3:
                    print("Has elegido salir, hasta pronto!")
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

class MenuCategorias:
    def __init__(self):
        self.productos = Productos()
        self.categorias = Categorias()  
        self.usuarios = Usuarios()  
        self.ventas = Ventas()  

    def mostrar_menu_categorias(self):
        while True:
            print("\t===============================")
            print("Servicios administrativos | Categorías")
            print("\t===============================")
            print("[1] Mantenimiento de productos")
            print("[2] Mantenimiento de categorías")
            print("[3] Mantenimiento de ventas")
            print("[4] Mantenimiento de usuarios")
            print("[5] Generación de informes")
            print("[6] Volver al menú principal")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    menu_productos = Menu()
                    menu_productos.mostrar_menu()
                elif option == 2:
                    self.mostrar_menu_categorias_mantenimiento()
                elif option == 3:
                    self.mostrar_menu_ventas_mantenimiento()
                elif option == 4:
                    self.mostrar_menu_usuarios_mantenimiento()
                elif option == 6:
                    break
                else:
                    print("Esta funcionalidad aún no está implementada.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    def mostrar_menu_categorias_mantenimiento(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de categorías")
            print("\t===============================")
            print("[1] Agregar Categoría")
            print("[2] Ver Categorías")
            print("[3] Modificar Categoría")
            print("[4] Eliminar Categoría")
            print("[5] Volver al menú anterior")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    self.categorias.agregar_categoria()
                elif option == 2:
                    self.categorias.mostrar_categorias()  
                elif option == 3:
                    self.categorias.modificar_categoria()
                elif option == 4:
                    self.categorias.eliminar_categoria()
                elif option == 5:
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    def mostrar_menu_ventas_mantenimiento(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de ventas")
            print("\t===============================")
            print("[1] Cambiar Estado de Envío")
            print("[2] Buscar Venta")
            print("[3] Ver Detalle de Venta")
            print("[4] Eliminar Venta")
            print("[5] Ver Ventas")
            print("[6] Volver al menú anterior")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))

                if option == 1:
                    self.ventas.cambiar_estado_envio()
                elif option == 2:
                    self.ventas.buscar_venta()
                elif option == 3:
                    self.ventas.ver_detalle_venta()
                elif option == 4:
                    self.ventas.eliminar_venta()
                elif option == 5:
                    self.ventas.ver_ventas()
                elif option == 6:
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    def mostrar_menu_usuarios_mantenimiento(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de usuarios")
            print("\t===============================")
            print("[1] Agregar Usuario")
            print("[2] Buscar Usuario")
            print("[3] Ver Usuarios")
            print("[4] Modificar Usuario")
            print("[5] Eliminar Usuario")
            print("[6] Volver al menú anterior")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    self.usuarios.agregar_usuario()
                elif option == 2:
                    self.usuarios.buscar_usuario()
                elif option == 3:
                    self.usuarios.ver_usuarios()
                elif option == 4:
                    self.usuarios.modificar_usuario()
                elif option == 5:
                    self.usuarios.eliminar_usuario()
                elif option == 6:
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

class Menu:
    def __init__(self):
        self.productos = Productos()

    def mostrar_menu(self):
        while True:
            print("\t===============================")
            print("Tienda de juguetes")
            print("\t===============================")
            print("[1] Agregar Productos")
            print("[2] Ver Productos")
            print("[3] Modificar Productos")
            print("[4] Eliminar Productos")
            print("[5] Salir")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                
                if option == 1:
                    self.productos.agregar_producto()
                elif option == 2:
                    self.productos.mostrar_productos()
                elif option == 3:
                    self.productos.modificar_producto()
                elif option == 4:
                    self.productos.eliminar_producto()
                elif option == 5:
                    print("Has elegido salir, hasta pronto!")
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

if __name__ == "__main__":
    menu_inicio = MenuInicio()
    menu_inicio.mostrar_menu_inicio()
