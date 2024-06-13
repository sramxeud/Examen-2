import sqlite3

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()


class AgenteInteligente:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def buscar(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def comparar(self, tabla, columna, valor):
        query = f"SELECT * FROM {tabla} WHERE {columna} = ?"
        return self.buscar(query, (valor,))

    def cerrar(self):
        self.conn.close()


agente = AgenteInteligente('biblioteca.db')

# Realizar una búsqueda
resultados = agente.buscar('SELECT * FROM libros')
print(resultados)

# Realizar una comparación
resultados = agente.comparar('libros', 'autor', 'Miguel de Cervantes')
print(resultados)

# Cerrar la conexión
agente.cerrar()
