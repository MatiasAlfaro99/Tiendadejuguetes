import sqlite3

database = "tienda_juguetes.db"

class Database:
    def ejecutar_consulta(self, consulta, parametros = ()):
        with sqlite3.connect (database) as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(consulta, parametros)
            conn.commit()
            return result
        

# db = Database()
# resultado = db.ejecutar_consulta("Select * from producto")
# print(resultado.fetchall())