def registrar_venta():
    total = 0
    while True:
        print("11. Hamburguesa")
        print("12. Completo")
        print("13. Papas Fritas")
        print("14. Salir")
        opcion = int(input("Ingrese opción: "))
        
        if opcion == 11:
            total += hamburguesa()
        elif opcion == 12:
            total += completo()
        elif opcion == 13:
            total += papas_fritas()
        elif opcion == 14:
            break
        else:
            print("Opción no válida.")
    return total

def hamburguesa():
    ingredientes = {"palta": 800, "tomate": 700, "cebolla": 600, "mayo": 500, "mostaza": 400}
    base = 1000
    carne = 1500
    total = base + carne
    
    for ing, precio in ingredientes.items():
        respuesta = input(f"Desea {ing} sí o no: ")
        if respuesta.lower() == 'sí':
            total += precio
    print(f"Su venta es de: {total}")
    return total

def completo():
    ingredientes = {"palta": 700, "tomate": 600, "chucrut": 500, "mayo": 500, "mostaza": 400}
    base = 800
    vienesa = 1200
    total = base + vienesa
    
    for ing, precio in ingredientes.items():
        respuesta = input(f"Desea {ing} sí o no: ")
        if respuesta.lower() == 'sí':
            total += precio
    print(f"Su venta es de: {total}")
    return total

def papas_fritas():
    papas = {"familiar": 5000, "mediana": 2500, "chica": 900}
    total = 0
    
    for tipo, precio in papas.items():
        respuesta = input(f"Desea papa {tipo} sí o no: ")
        if respuesta.lower() == 'sí':
            total += precio
    print(f"Su venta es de: {total}")
    return total

def main():
    total_ventas = 0
    while True:
        print("--Bienvenido a Comida al paso--")
        print("1. Registrar Venta")
        print("2. Consultar Ventas")
        print("3. Salir")
        opcion = int(input("Ingrese opción: "))
        
        if opcion == 1:
            total_ventas += registrar_venta()
        elif opcion == 2:
            print(f"El total de ventas hasta el momento es de: {total_ventas}")
        elif opcion == 3:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
