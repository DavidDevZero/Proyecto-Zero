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
    gasto = {"usuario_id": usuario_id, "cantidad": cantidad, "categoria": categoria} # crear diccionario
    gastos_db.append(gasto) # agregar a la lista
    print("✅gasto registrado con exito.") # confirmacion

def registrar_ingreso(usuario_id):
    cantidad = float(input("introduce la cantidad del ingreso: ")) # convertir a numero
    fuente = input("introduce la fuente del ingreso: ") # pedir fuente
    ingreso = {"usuario_id": usuario_id, "cantidad": cantidad, "fuente": fuente} # crear diccionario
    ingresos_db.append(ingreso) # agregar a la lista
    print("✅ingreso registrado con exito.") # confirmacion

def obtener_balance(usuario_id):
    pass

def mostrar_gastos(usuario_id):
    pass

def menu_principal(usuario_id):
    while True:     # bucle infinito
        print("\n=== MENU PRINCIPAL ===")
        print("1. registrar gasto")
        print("2. registrar ingreso")
        print("3. salir")

        opcion = input("elige una opcion: ")

        if opcion == "1":
            registrar_gasto(usuario_id)
        elif opcion == "2":
            registrar_ingreso(usuario_id)
        elif opcion == "3":
            print("👋 saliendo del programa...")
            break
        else:
            print("❌ opcion no valida. intentalo de nuevo") 
   
# --- Punto de Entrada (Al final del todo, un solo bloque) ---        
if __name__ == "__main__":
    usuario_logueado_id = 1
    menu_principal(usuario_logueado_id)