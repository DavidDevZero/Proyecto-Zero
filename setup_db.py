import sqlite3

# Conexión a la base de datos (la crea si no existe)
conexion = sqlite3.connect("tracker.db")

# Abrir y leer el contenido del archivo schema.sql
with open("schema.sql", "r", encoding="utf-8") as archivo_sql:
    schema = archivo_sql.read()

# Crear cursor y ejecutar el esquema SQL
cursor = conexion.cursor()
cursor.executescript(schema)

# Confirmar y cerrar
conexion.commit()
conexion.close()

print("✅ Base de datos creada con éxito.")