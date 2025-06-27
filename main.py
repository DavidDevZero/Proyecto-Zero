# PLAN PARA REFACTORIZAR registrar_gasto:
# 1. La función recibirá el 'usuario_id' y la 'db'.
# 2. Dentro de la función, me conectaré a la base de datos.
# 3. Crearé un cursor para dar las órdenes.
# 4. Definiré la sentencia SQL "INSERT INTO..." en una variable.
# 5. Pediré los datos al usuario (cantidad, categoría).
# 6. Usaré cursor.execute() con la sentencia SQL y los datos del usuario por separado.
# 7. Haré conn.commit() para guardar los cambios.
# 8. Cerraré la conexión con conn.close().

# base de datos en memoria
gastos_db = []
ingresos_db = []

# --- Definición de Funciones (Todas juntas) ---
def registrar_usuario():
    # Esta función todavía no hace nada
    pass

import sqlite3  # Sólo una vez, al principio

# --- Registrar gasto en la base de datos ---
def registrar_gasto(usuario_id):
    cantidad = float(input("Introduce la cantidad del gasto: "))
    categoria = input("Introduce la categoría del gasto: ")
    descripcion = input("Introduce una descripción (opcional): ")

    while True:
        try:
            cantidad_str = input("Introduce la cantidad del gasto: ")
            cantidad = float(cantidad_str)
            break
        except ValueError:
            print("Error: Por favor, introduce únicamente números.")
    
    categoria = input("Introduce la categoría del gasto: ")
    sql = "INSERT INTO gastos (usuario_id, cantidad, categoria) VALUES (?, ?, ?)"
    datos = (usuario_id, cantidad, categoria)

    try:
        with sqlite3.connect('tracker.db') as conn:
            cursor = conn.cursor()
            cursor.execute(sql, datos)
            conn.commit()
        
        print("Gasto registrado con éxito.")

    except sqlite3.Error as e:
        print(f"ERROR al interactuar con la base de datos: {e}")

# --- Registrar ingreso en la base de datos ---
def registrar_ingreso(usuario_id):
    cantidad = float(input("Introduce la cantidad del ingreso: "))
    fuente = input("Introduce la fuente del ingreso: ")

    conexion = sqlite3.connect("tracker.db")
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO ingresos (usuario_id, cantidad, fuente)
        VALUES (?, ?, ?)
    """, (usuario_id, cantidad, fuente))
    conexion.commit()
    conexion.close()

    print(" Ingreso registrado en la base de datos.")

# --- Mostrar gastos con ID para editarlos ---
def mostrar_gastos(usuario_id):
    print("\n--- LISTA DE GASTOS ---")
    conexion = sqlite3.connect("tracker.db")
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id, categoria, cantidad, fecha, descripcion FROM gastos
        WHERE usuario_id = ?
        ORDER BY fecha DESC
    """, (usuario_id,))
    resultados = cursor.fetchall()
    conexion.close()

    if not resultados:
        print(" No hay gastos registrados.")
        return

    for id, categoria, cantidad, fecha, descripcion in resultados:
        print(f"🆔 {id} | {fecha[:10]} | {categoria} | {cantidad:.2f}€ | {descripcion or 'Sin descripción'}")

# --- Modificar gasto seleccionado por ID ---
def modificar_gasto(usuario_id):
    mostrar_gastos(usuario_id)
    gasto_id = input(" Ingresa el ID del gasto que quieres modificar: ")

    nueva_categoria = input("Nueva categoría: ")
    nueva_cantidad = float(input("Nueva cantidad: "))
    nueva_descripcion = input("Nueva descripción (opcional): ")

    conexion = sqlite3.connect("tracker.db")
    cursor = conexion.cursor()
    cursor.execute("""
        UPDATE gastos
        SET categoria = ?, cantidad = ?, descripcion = ?
        WHERE id = ? AND usuario_id = ?
    """, (nueva_categoria, nueva_cantidad, nueva_descripcion, gasto_id, usuario_id))
    conexion.commit()
    conexion.close()

    print(" Gasto actualizado con éxito.")

# --- Calcular balance desde base de datos ---
def calcular_balance(usuario_id):
    conexion = sqlite3.connect("tracker.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT SUM(cantidad) FROM ingresos WHERE usuario_id = ?", (usuario_id,))
    total_ingresos = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(cantidad) FROM gastos WHERE usuario_id = ?", (usuario_id,))
    total_gastos = cursor.fetchone()[0] or 0

    conexion.close()

    balance = total_ingresos - total_gastos
    print("\n--- BALANCE GENERAL ---")
    print(f" Total Ingresos: {total_ingresos:.2f}€")
    print(f" Total Gastos:   {total_gastos:.2f}€")
    print(f" Balance Neto:   {balance:.2f}€")

# --- Menú principal del programa ---
def menu_principal(usuario_id):
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrar Gasto")
        print("2. Registrar Ingreso")
        print("3. Mostrar Gastos")
        print("4. Ver Balance")
        print("5. Modificar Gasto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_gasto(usuario_id)
        elif opcion == "2":
            registrar_ingreso(usuario_id)
        elif opcion == "3":
            mostrar_gastos(usuario_id)
        elif opcion == "4":
            calcular_balance(usuario_id)
        elif opcion == "5":
            modificar_gasto(usuario_id)
        elif opcion == "6":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

# --- Punto de entrada principal ---
if __name__ == "__main__":
    usuario_logueado_id = 1  # Simulación de usuario autenticado
    menu_principal(usuario_logueado_id)

   
