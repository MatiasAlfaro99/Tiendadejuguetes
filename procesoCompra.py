import CRUD as conn
db = conn.Database()

class ProcesoCompra:
    def __init__(self):
        self.carrito = []

    def mostrar_menu_proceso_compra(self):
        while True:
            print("\t===============================")
            print("Proceso de compra")
            print("\t===============================")
            print("[1] Buscar Producto")
            print("[2] Agregar Producto al Carrito")
            print("[3] Ver Carrito")
            print("[4] Completar Transacción")
            print("[5] Volver al menú principal")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))
                if option == 1:
                    self.buscarProducto()
                elif option == 2:
                    idProducto = int(input("Ingrese el ID del producto que desea agregar: "))
                    self.agregarProductoAlCarrito(idProducto)
                elif option == 3:
                    self.verCompra()
                elif option == 4:
                    self.completarTransaccion()
                elif option == 5:
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

    def buscarProducto(self):
        producto = input("Ingrese el nombre del producto que desea buscar: ")
        query = "SELECT * FROM producto WHERE nombreProducto LIKE ?"
        result = db.ejecutar_consulta(query, ('%' + producto + '%',))
        productos_encontrados = result.fetchall()

        if productos_encontrados:
            print("Productos encontrados:")
            for prod in productos_encontrados:
                print(f"ID: {prod[0]}, Nombre: {prod[1]}, Descripción: {prod[2]}, Precio: {prod[4]}, Stock: {prod[3]}")
        else:
            print("No se encontraron productos con ese nombre.")

    def agregarProductoAlCarrito(self, idProducto):
        query = "SELECT * FROM producto WHERE idProducto = ?"
        result = db.ejecutar_consulta(query, (idProducto,))
        producto = result.fetchone()

        if producto:
            self.carrito.append(producto)
            print(f"Producto '{producto[1]}' agregado al carrito.")
        else:
            print(f"No existe un producto con el ID {idProducto}.")

    def verCompra(self):
        if not self.carrito:
            print("El carrito está vacío.")
        else:
            print("Productos en el carrito:")
            for producto in self.carrito:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[4]}, Stock: {producto[3]}")

    def completarTransaccion(self):
        if not self.carrito:
            print("No hay productos en el carrito para completar la compra.")
            return

        try:
            for producto in self.carrito:
                idProducto = producto[0]
                stock_actual = producto[3]

                if stock_actual > 0:
                    nuevo_stock = stock_actual - 1
                    query = "UPDATE producto SET stock = ? WHERE idProducto = ?"
                    db.ejecutar_consulta(query, (nuevo_stock, idProducto))
                    print(f"Producto '{producto[1]}' actualizado: stock reducido a {nuevo_stock}.")
                else:
                    print(f"El producto '{producto[1]}' no tiene stock disponible.")
                    continue

            print("Transacción completada. Gracias por su compra.")
            self.carrito.clear()

        except Exception as e:
            print(f"Error al completar la transacción: {e}")
