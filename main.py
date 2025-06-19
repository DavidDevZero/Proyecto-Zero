# base de datos en memoria
gastos_db = []
ingresos_db = []

# --- Definición de Funciones (Todas juntas) ---
def registrar_usuario():
    # Esta función todavía no hace nada
    pass

def registrar_gasto(usuario_id):
    cantidad = float(input("introduce la cantidad de gasto: ")) # convertir a numero
    categoria = input("introduce la categoria gasto: ") # pedir categoria
    gasto = {"usuario_id": usuario_id, 
             "cantidad": cantidad, 
             "categoria": categoria} # crear diccionario
    gastos_db.append(gasto) # agregar a la lista
    print("✅gasto registrado con exito.") # confirmacion

def registrar_ingreso(usuario_id):
    cantidad = float(input("introduce la cantidad del ingreso: ")) # convertir a numero
    fuente = input("introduce la fuente del ingreso: ") # pedir fuente
    ingreso = {"usuario_id": usuario_id, 
               "cantidad": cantidad, 
               "fuente": fuente} # crear diccionario
    ingresos_db.append(ingreso) # agregar a la lista
    print("✅ingreso registrado con exito.") # confirmacion

def mostrar_gastos(usuario_id):
    print("\n--- LISTA DE GASTOS ---")

    if not gastos_db:
        print("📭 No hay gastos registrados.")
        return

    gastos_encontrados = False
    for gasto in gastos_db:
        if gasto["usuario_id"] == usuario_id:
            print(f"📌 Categoría: {gasto['categoria']} | Cantidad: {gasto['cantidad']:.2f}€")
            gastos_encontrados = True

    if not gastos_encontrados:
        print("🤷 No tienes gastos registrados todavía.")

def calcular_balance(usuario_id):
    total_ingresos = sum(ingreso["cantidad"] for ingreso in ingresos_db if ingreso["usuario_id"] == usuario_id)
    total_gastos = sum(gasto["cantidad"] for gasto in gastos_db if gasto["usuario_id"] == usuario_id)
    balance = total_ingresos - total_gastos
    print("\n--- BALANCE GENERAL ---")
    print(f"💵 Total Ingresos: {total_ingresos:.2f}€")
    print(f"💸 Total Gastos: {total_gastos:.2f}€")
    print(f"💰 Balance Neto: {balance:.2f}€")

def menu_principal(usuario_id):
    while True:     # bucle infinito
        print("\n=== MENU PRINCIPAL ===")
        print("1. registrar gasto")
        print("2. registrar ingreso")
        print("3. mostrar gastos")
        print("4. ver balance")
        print("5. salir")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            registrar_gasto(usuario_id)
        elif opcion == "2":
            registrar_ingreso(usuario_id)
        elif opcion == "3":
            mostrar_gastos(usuario_id)
        elif opcion == "4":
            calcular_balance(usuario_id)
        elif opcion == "5":
            print("👋 saliendo del programa...")
            break
        else:
            print("❌ opcion no valida. intentalo de nuevo") 
   
# --- Punto de Entrada (Al final del todo, un solo bloque) ---        
if __name__ == "__main__":
    usuario_logueado_id = 1     # simulacion de inicio de sesion
    menu_principal(usuario_logueado_id)