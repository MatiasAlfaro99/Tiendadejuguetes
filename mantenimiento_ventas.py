import CRUD as conn
db = conn.Database()

class Ventas:
    def __init__(self):
        pass

    def cambiar_estado_envio(self):
        try:
            idVenta = int(input("Ingrese el ID de la venta que desea actualizar el estado de envío: "))
            resultado = db.ejecutar_consulta("SELECT * FROM venta WHERE idVenta = ?", (idVenta,))
            venta = resultado.fetchone()

            if venta is None:
                print(f"No existe una venta con el ID {idVenta}.")
                return

            print(f"""
            Venta actual:
            ID Venta: {venta[0]}
            Estado de envío: {venta[3]}
            """)

            print("Opciones de estado de envío:")
            print("[1] A la espera de envío")
            print("[2] En proceso de envío")
            print("[3] Entregado")

            opcion_estado = int(input("Selecciona una opción de estado: "))
            estado_envio = ""

            if opcion_estado == 1:
                estado_envio = "A la espera de envío"
            elif opcion_estado == 2:
                estado_envio = "En proceso de envío"
            elif opcion_estado == 3:
                estado_envio = "Entregado"
            else:
                print("Opción de estado no válida.")
                return

            sql = "UPDATE venta SET estadoEnvio = ? WHERE idVenta = ?"
            parametros = (estado_envio, idVenta)
            db.ejecutar_consulta(sql, parametros)
            print(f"Estado de envío de la venta con ID {idVenta} actualizado a '{estado_envio}' correctamente.")

        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al cambiar el estado de envío: {e}")

    def buscar_venta(self):
        try:
            idVenta = int(input("Ingrese el ID de la venta que desea buscar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM venta WHERE idVenta = ?", (idVenta,))
            venta = resultado.fetchone()

            if venta:
                print(f"""
                Venta encontrada:
                ID Venta: {venta[0]}
                Fecha de Venta: {venta[1]}
                Estado de Envío: {venta[3]}
                """)
            else:
                print(f"No se encontró una venta con el ID {idVenta}.")
        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al buscar la venta: {e}")

    def ver_detalle_venta(self):
        try:
            idVenta = int(input("Ingrese el ID de la venta cuyo detalle desea ver: "))
            resultado = db.ejecutar_consulta("SELECT * FROM detalle_venta WHERE idVenta = ?", (idVenta,))
            detalles = resultado.fetchall()

            if detalles:
                for detalle in detalles:
                    print(f"""
                    Detalle de Venta:
                    ID Venta: {detalle[0]}
                    ID Producto: {detalle[1]}
                    Cantidad: {detalle[2]}
                    Precio Unitario: {detalle[3]}
                    """)
            else:
                print(f"No hay detalles registrados para la venta con ID {idVenta}.")
        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al ver el detalle de la venta: {e}")

    def eliminar_venta(self):
        try:
            idVenta = int(input("Ingrese el ID de la venta que desea eliminar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM venta WHERE idVenta = ?", (idVenta,))
            venta = resultado.fetchone()

            if venta is None:
                print(f"No existe una venta con el ID {idVenta}.")
                return

            print(f"""
            Venta a eliminar:
            ID Venta: {venta[0]}
            Fecha de Venta: {venta[1]}
            Estado de Envío: {venta[3]}
            """)

            confirmacion = input("¿Está seguro que desea eliminar esta venta? (s/n): ").lower()
            if confirmacion == 's':
                sql = "DELETE FROM venta WHERE idVenta = ?"
                db.ejecutar_consulta(sql, (idVenta,))
                print(f"Venta con ID {idVenta} eliminada correctamente.")
            else:
                print("Operación cancelada.")
        except ValueError:
            print("El ID de la venta debe ser un número válido.")
        except Exception as e:
            print(f"Error al eliminar la venta: {e}")

    def ver_ventas(self):
        print("Mostrando todas las ventas...")
        resultado = db.ejecutar_consulta("SELECT * FROM venta")
        ventas = resultado.fetchall()

        if ventas:
            for venta in ventas:
                print(f"""
                ID Venta: {venta[0]}
                Fecha de Venta: {venta[1]}
                Estado de Envío: {venta[3]}
                """)
        else:
            print("No hay ventas registradas.")

    def mostrar_menu_ventas(self):
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
                    self.cambiar_estado_envio()
                elif option == 2:
                    self.buscar_venta()
                elif option == 3:
                    self.ver_detalle_venta()
                elif option == 4:
                    self.eliminar_venta()
                elif option == 5:
                    self.ver_ventas()
                elif option == 6:
                    break
                else:
                    print("Por favor selecciona una opción válida.")
            except ValueError:
                print("Error: Debes ingresar un número.")
            except Exception as e:
                print(f"Error inesperado: {e}")

