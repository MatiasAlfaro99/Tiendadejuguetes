import CRUD as conn
db = conn.Database()

class Usuarios:
    def __init__(self):
        pass

    def agregar_usuario(self):
        run = str(input("Ingrese el RUN del usuario: "))
        nombres = str(input("Ingrese los nombres del usuario: "))
        apellidos = str(input("Ingrese los apellidos del usuario: "))
        correo = str(input("Ingrese el correo del usuario: "))
        telefono = str(input("Ingrese el teléfono del usuario: "))
        direccion = str(input("Ingrese la dirección del usuario: "))
        clave = str(input("Ingrese la clave del usuario: "))

        if len(run) > 0 and len(nombres) > 0 and len(apellidos) > 0 and len(correo) > 0 and len(clave) > 0:
            try:
                sql = "INSERT INTO usuario(run, nombres, apellidos, correo, telefono, direccion, clave) VALUES (?, ?, ?, ?, ?, ?, ?)"
                parametros = (run, nombres, apellidos, correo, telefono, direccion, clave)
                db.ejecutar_consulta(sql, parametros)
                print(f"Usuario '{nombres} {apellidos}' agregado correctamente.")
            except Exception as e:
                print(f"Error al agregar el usuario: {e}")
        else:
            print("Datos incorrectos, intente de nuevo.")

    def buscar_usuario(self):
        run = str(input("Ingrese el RUN del usuario que desea buscar: "))
        resultado = db.ejecutar_consulta("SELECT * FROM usuario WHERE run = ?", (run,))
        usuario = resultado.fetchone()

        if usuario:
            print(f"""
            Usuario encontrado:
            RUN: {usuario[0]}
            Nombres: {usuario[1]}
            Apellidos: {usuario[2]}
            Correo: {usuario[3]}
            Teléfono: {usuario[4]}
            Dirección: {usuario[5]}
            Clave: {usuario[6]}
            """)
        else:
            print(f"No se encontró un usuario con el RUN {run}.")

    def modificar_usuario(self):
        try:
            run = str(input("Ingrese el RUN del usuario que desea modificar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM usuario WHERE run = ?", (run,))
            usuario = resultado.fetchone()

            if usuario is None:
                print(f"No existe un usuario con el RUN {run}.")
                return

            print(f"""
            Usuario actual:
            RUN: {usuario[0]}
            Nombres: {usuario[1]}
            Apellidos: {usuario[2]}
            Correo: {usuario[3]}
            Teléfono: {usuario[4]}
            Dirección: {usuario[5]}
            Clave: {usuario[6]}
            """)

            nombres = input(f"Ingrese los nuevos nombres del usuario (deje en blanco para mantener '{usuario[1]}'): ") or usuario[1]
            apellidos = input(f"Ingrese los nuevos apellidos del usuario (deje en blanco para mantener '{usuario[2]}'): ") or usuario[2]
            correo = input(f"Ingrese el nuevo correo del usuario (deje en blanco para mantener '{usuario[3]}'): ") or usuario[3]
            telefono = input(f"Ingrese el nuevo teléfono del usuario (deje en blanco para mantener '{usuario[4]}'): ") or usuario[4]
            direccion = input(f"Ingrese la nueva dirección del usuario (deje en blanco para mantener '{usuario[5]}'): ") or usuario[5]
            clave = input(f"Ingrese la nueva clave del usuario (deje en blanco para mantener la clave actual): ") or usuario[6]

            sql = """UPDATE usuario
                    SET nombres = ?, apellidos = ?, correo = ?, telefono = ?, direccion = ?, clave = ?
                    WHERE run = ?"""
            parametros = (nombres, apellidos, correo, telefono, direccion, clave, run)
            db.ejecutar_consulta(sql, parametros)
            print(f"Usuario '{nombres} {apellidos}' actualizado correctamente.")
        except ValueError:
            print("El RUN del usuario debe ser válido.")
        except Exception as e:
            print(f"Error al modificar el usuario: {e}")

    def eliminar_usuario(self):
        try:
            run = str(input("Ingrese el RUN del usuario que desea eliminar: "))
            resultado = db.ejecutar_consulta("SELECT * FROM usuario WHERE run = ?", (run,))
            usuario = resultado.fetchone()

            if usuario is None:
                print(f"No existe un usuario con el RUN {run}.")
                return

            print(f"""
            Usuario a eliminar:
            RUN: {usuario[0]}
            Nombres: {usuario[1]}
            Apellidos: {usuario[2]}
            Correo: {usuario[3]}
            Teléfono: {usuario[4]}
            Dirección: {usuario[5]}
            Clave: {usuario[6]}
            """)

            confirmacion = input("¿Está seguro que desea eliminar este usuario? (s/n): ").lower()
            if confirmacion == 's':
                sql = "DELETE FROM usuario WHERE run = ?"
                db.ejecutar_consulta(sql, (run,))
                print(f"Usuario con RUN {run} eliminado correctamente.")
            else:
                print("Operación cancelada.")
        except ValueError:
            print("El RUN del usuario debe ser válido.")
        except Exception as e:
            print(f"Error al eliminar el usuario: {e}")

    def ver_usuarios(self):
        print("Mostrando todos los usuarios...")
        resultado = db.ejecutar_consulta("SELECT * FROM usuario")
        usuarios = resultado.fetchall()

        if usuarios:
            for usuario in usuarios:
                print(f"""
                RUN: {usuario[0]}
                Nombres: {usuario[1]}
                Apellidos: {usuario[2]}
                Correo: {usuario[3]}
                Teléfono: {usuario[4]}
                Dirección: {usuario[5]}
                Clave: {usuario[6]}
                """)
        else:
            print("No hay usuarios registrados.")
