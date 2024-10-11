import CRUD as conn
db = conn.Database()

class Categorias:
    def __init__(self):
        pass

    def mostrar_categorias(self):
        print("Mostrando categorías...")
        result = db.ejecutar_consulta("SELECT * FROM categoria")
        for data in result:
            print(f"""
                Id categoría: {data[0]}
                Nombre de la categoría: {data[1]}
            """)

    def agregar_categoria(self):
        nombreCategoria = str(input("Ingrese el nombre de la nueva categoría: "))

        if len(nombreCategoria) > 0:
            try:
                sql = "INSERT INTO categoria(nombreCategoria) VALUES (?)"
                parametros = (nombreCategoria,)
                db.ejecutar_consulta(sql, parametros)
                print(f"Categoría '{nombreCategoria}' ingresada correctamente.")
            except Exception as e:
                print(f"Error al insertar la categoría: {e}")
        else:
            print("El nombre de la categoría no puede estar vacío.")

    def modificar_categoria(self):
        try:
            idCategoria = int(input("Ingrese el ID de la categoría que desea modificar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM categoria WHERE idCategoria = ?", (idCategoria,))
            categoria = resultado.fetchone()

            if categoria is None:
                print(f"No existe una categoría con el ID {idCategoria}.")
                return

            print(f"""
            Categoría actual:
            Id categoría: {categoria[0]}
            Nombre de la categoría: {categoria[1]}
            """)

            nombreCategoria = input(f"Ingrese el nuevo nombre de la categoría (deje en blanco para mantener '{categoria[1]}'): ") or categoria[1]

            if len(nombreCategoria) > 0:
                sql = "UPDATE categoria SET nombreCategoria = ? WHERE idCategoria = ?"
                parametros = (nombreCategoria, idCategoria)
                db.ejecutar_consulta(sql, parametros)
                print(f"Categoría '{nombreCategoria}' actualizada correctamente.")
            else:
                print("El nombre de la categoría no puede estar vacío.")

        except ValueError:
            print("El ID de la categoría debe ser un número válido.")
        except Exception as e:
            print(f"Error al modificar la categoría: {e}")

    def eliminar_categoria(self):
        try:
            idCategoria = int(input("Ingrese el ID de la categoría que desea eliminar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM categoria WHERE idCategoria = ?", (idCategoria,))
            categoria = resultado.fetchone()

            if categoria is None:
                print(f"No existe una categoría con el ID {idCategoria}.")
                return

            print(f"""
            Categoría a eliminar:
            Id categoría: {categoria[0]}
            Nombre de la categoría: {categoria[1]}
            """)

            confirmacion = input("¿Está seguro que desea eliminar esta categoría? (s/n): ").lower()
            if confirmacion == 's':
                sql = "DELETE FROM categoria WHERE idCategoria = ?"
                db.ejecutar_consulta(sql, (idCategoria,))
                print(f"Categoría con ID {idCategoria} eliminada correctamente.")
            else:
                print("Operación cancelada.")

        except ValueError:
            print("El ID de la categoría debe ser un número válido.")
        except Exception as e:
            print(f"Error al eliminar la categoría: {e}")

    def mostrar_menu_categorias(self):
        while True:
            print("\t===============================")
            print("Mantenimiento de categorías")
            print("\t===============================")
            print("[1] Agregar Categoría")
            print("[2] Ver Categorías")
            print("[3] Modificar Categoría")
            print("[4] Eliminar Categoría")
            print("[5] Volver al menú principal")
            print("\t===============================")

            try:
                option = int(input("Selecciona una opción: "))

                if option == 1:
                    self.agregar_categoria()
                elif option == 2:
                    self.mostrar_categorias()
                elif option == 3:
                    self.modificar_categoria()
                elif option == 4:
                    self.eliminar_categoria()
                elif option == 5:
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

