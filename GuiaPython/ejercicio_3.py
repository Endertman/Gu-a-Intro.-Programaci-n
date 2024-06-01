def vender_pasaje():
    destinos = {"Santiago": 18000, "Arica": 18500, "Temuco": 20580, "Concepción": 18600}
    ventas = {"Santiago": 0, "Arica": 0, "Temuco": 0, "Concepción": 0}
    total_maletas = 0
    total_pasajes = 0
    
    while True:
        print("Destinos:")
        for i, destino in enumerate(destinos, 1):
            print(f"{i}. {destino} ${destinos[destino]}")
        opcion = int(input("Seleccione destino: "))
        destino_seleccionado = list(destinos.keys())[opcion-1]
        precio = destinos[destino_seleccionado]
        
        vuelta = input("¿Desea pasaje de vuelta? (sí/no): ")
        if vuelta.lower() == "sí":
            precio *= 2
        
        maletas = int(input("Cantidad de maletas: "))
        if maletas > 1:
            precio += (maletas - 1) * 5000
        
        print(f"\n*************PASAJE INTERURBANOS*****************")
        print(f"Destino: {destino_seleccionado} ida {'y vuelta ' if vuelta.lower() == 'sí' else ''}Valor ${precio}")
        print(f"Unidades equipaje: {maletas} Valor ${0 if maletas <= 1 else (maletas - 1) * 5000}")
        print(f"TOTAL: ${precio}")
        print("****************************************************\n")
        
        ventas[destino_seleccionado] += 1
        total_maletas += 0 if maletas <= 1 else (maletas - 1) * 5000
        total_pasajes += precio
        
        nuevo = input("¿Necesita otro pasaje? (sí/no): ")
        if nuevo.lower() != "sí":
            break
    
    print("\n*************PASAJE INTERURBANOS*****************")
    print("Resumen de Ventas del día")
    for destino, cantidad in ventas.items():
        print(f"{destino}: {cantidad}")
    print(f"TOTAL EN PASAJES: ${total_pasajes}")
    print(f"TOTAL EN MALETAS: ${total_maletas}")
    print("****************************************************")

if __name__ == "__main__":
    vender_pasaje()
