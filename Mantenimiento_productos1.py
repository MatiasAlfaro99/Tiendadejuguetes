import CRUD as conn
db = conn.Database()

class Productos:
    def __init__(self):
        pass

    def mostrar_categorias(self):
        print("""
        Categorías disponibles:
        1 - Vehículos de Juguete
        2 - Muñecas y Figuras de Acción
        3 - Juegos educativos
        4 - Electrónica para Niños
        5 - Deportes y Aire Libre
        6 - Peluches y Cojines
        7 - Juegos de Mesa
        8 - Instrumentos Musicales
        9 - Drones y Tecnología
        10 - Material Didáctico
        """)

    def agregar_producto(self):
        nombreProducto = str(input("Ingrese el nombre del producto: "))
        descripcionProducto = str(input("Ingrese la descripcion del Producto o deje en blanco: "))

        try:
            stock = int(input("Ingrese el stock del producto: "))
            precio = int(input("Ingrese el precio del producto: "))
            self.mostrar_categorias()
            idCategoria = int(input("Ingrese el ID de la categoría del producto: "))
        except ValueError:
            print("El stock, precio y categoría deben ser números enteros.")
            return

        if len(nombreProducto) > 0 and stock > 0 and precio > 0 and idCategoria > 0 and idCategoria < 11:
            try:
                resultado_categoria = db.ejecutar_consulta("SELECT * FROM categoria WHERE idCategoria = ?", (idCategoria,))
                if not resultado_categoria.fetchone():
                    print(f"Error: El ID de categoría {idCategoria} no existe. Ingrese una categoría válida.")
                    return

                sql = "INSERT INTO producto(nombreProducto, descripcionProducto, stock, precio, idCategoria) VALUES (?, ?, ?, ?, ?)"
                parametros = (nombreProducto, descripcionProducto, stock, precio, idCategoria)
                db.ejecutar_consulta(sql, parametros)
                print(f"Producto '{nombreProducto}' ingresado correctamente.")
            except Exception as e:
                print(f"Error al insertar el producto: {e}")
        else:
            print("Datos incorrectos, intente de nuevo")

    def mostrar_productos(self):
        print("Mostrando productos...")
        result = db.ejecutar_consulta("SELECT * FROM producto")
        for data in result:
            print(f"""
                Id producto: {data[0]}
                Nombre del producto: {data[1]}
                Descripción del producto: {data[2]}
                Precio: {data[3]}
                Stock: {data[4]}
                Id categoría: {data[5]}
            """)

    def modificar_producto(self):
        try:
            idProducto = int(input("Ingrese el ID del producto que desea modificar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM producto WHERE idProducto = ?", (idProducto,))
            producto = resultado.fetchone()

            if producto is None:
                print(f"No existe un producto con el ID {idProducto}.")
                return

            print(f"""
            Producto actual:
            Id producto: {producto[0]}
            Nombre del producto: {producto[1]}
            Descripción del producto: {producto[2]}
            Stock: {producto[3]}
            Precio: {producto[4]}
            Id categoría: {producto[5]}
            """)

            nombreProducto = input(f"Ingrese el nuevo nombre del producto (deje en blanco para mantener '{producto[1]}'): ") or producto[1]
            descripcionProducto = input(f"Ingrese la nueva descripción del producto (deje en blanco para mantener '{producto[2]}'): ") or producto[2]

            try:
                stock = input(f"Ingrese el nuevo stock (deje en blanco para mantener '{producto[3]}'): ") or producto[3]
                stock = int(stock) if stock else producto[3]

                precio = input(f"Ingrese el nuevo precio (deje en blanco para mantener '{producto[4]}'): ") or producto[4]
                precio = float(precio) if precio else producto[4]

                idCategoria = input(f"Ingrese el nuevo ID de la categoría (deje en blanco para mantener '{producto[5]}'): ") or producto[5]
                idCategoria = int(idCategoria) if idCategoria else producto[5]

            except ValueError:
                print("El stock, precio e ID de la categoría deben ser números válidos.")
                return

            if stock < 0 or precio < 0 or idCategoria < 1 or idCategoria > 10:
                print("El stock, precio o ID de la categoría no son válidos. Por favor, ingrese valores positivos y un ID de categoría válido.")
                return

            sql = """UPDATE producto
                    SET nombreProducto = ?, descripcionProducto = ?, stock = ?, precio = ?, idCategoria = ?
                    WHERE idProducto = ?"""
            parametros = (nombreProducto, descripcionProducto, stock, precio, idCategoria, idProducto)
            db.ejecutar_consulta(sql, parametros)
            print(f"Producto '{nombreProducto}' actualizado correctamente.")

        except ValueError:
            print("El ID del producto debe ser un número válido.")
        except Exception as e:
            print(f"Error al modificar el producto: {e}")

    def eliminar_producto(self):
        try:
            idProducto = int(input("Ingrese el ID del producto que desea eliminar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM producto WHERE idProducto = ?", (idProducto,))
            producto = resultado.fetchone()

            if producto is None:
                print(f"No existe un producto con el ID {idProducto}.")
                return

            print(f"""
            Producto a eliminar:
            Id producto: {producto[0]}
            Nombre del producto: {producto[1]}
            Descripción del producto: {producto[2]}
            Stock: {producto[3]}
            Precio: {producto[4]}
            Id categoría: {producto[5]}
            """)

            confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ").lower()
            if confirmacion == 's':
                sql = "DELETE FROM producto WHERE idProducto = ?"
                db.ejecutar_consulta(sql, (idProducto,))
                print(f"Producto con ID {idProducto} eliminado correctamente.")
            else:
                print("Operación cancelada.")

        except ValueError:
            print("El ID del producto debe ser un número válido.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")
