# =========================================================
# PROYECTO: Sistema de Gestión de Inventario (AVANCE PASO 1)
# AUTORA: Arianna
# =========================================================

def registrar_producto():
    print("\n[AVANCE] Función para registrar producto en desarrollo...")

def mostrar_inventario():
    print("\n[AVANCE] Función para listar productos en desarrollo...")

def buscar_producto():
    print("\n[AVANCE] Función para buscar productos en desarrollo...")

def main():
    activo = True
    while activo:
        print("\n=== SISTEMA DE GESTIÓN DE INVENTARIO ===")
        print("1. Registrar nuevo producto")
        print("2. Mostrar lista de productos")
        print("3. Buscar producto por nombre")
        print("4. Salir del programa")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            print("\nSaliendo del sistema...")
            activo = False
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
