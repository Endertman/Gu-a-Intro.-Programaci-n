def mostrar_categoria():
    categorias = ["dulces", "salados", "helados", "colaciones"]
    print("Categorías disponibles:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i}. {categoria}")
    opcion = int(input("Seleccione una categoría: "))
    return categorias[opcion-1]

def mostrar_productos(categoria):
    productos = {
        "dulces": {"chocolate": 500, "caramelo": 300, "chicle": 100},
        "salados": {"papas": 1000, "nachos": 1200, "palomitas": 800},
        "helados": {"vainilla": 1500, "chocolate": 1500, "fresa": 1500},
        "colaciones": {"manzana": 200, "pera": 250, "naranja": 300}
    }
    return productos[categoria]

def calcular_descuento(total, cantidades):
    descuento = 0
    if sum(cantidades.values()) > 5:
        descuento += 0.02 * total
    if all(cantidad >= 10 for cantidad in cantidades.values()):
        descuento += 0.10 * total
    return descuento
    
def factura(productos_seleccionados, datos_cliente, forma_pago, descuento):
    print("\nFactura:")
    print("Cliente:", datos_cliente['nombre'])
    print("Dirección:", datos_cliente['direccion'])
    total = 0
    for producto, detalles in productos_seleccionados.items():
        cantidad, precio = detalles
        total += cantidad * precio
        print(f"{producto}: {cantidad} x {precio} = {cantidad * precio}")
    print(f"Descuento: -{descuento}")
    total -= descuento
    if forma_pago == "debito":
        descuento_pago = 0.02 * total
        print(f"Descuento por pago con debito: -{descuento_pago}")
        total -= descuento_pago
    print(f"Total a pagar: {total}")

def main():
    productos_seleccionados = {}
    while True:
        categoria = mostrar_categoria()
        productos = mostrar_productos(categoria)
        cantidades = {}
        while True:
            print(f"Productos disponibles en {categoria}:")
            for producto, precio in productos.items():
                print(f"{producto}: {precio}")
            producto = input("Seleccione un producto: ")
            cantidad = int(input(f"Indique la cantidad de {producto}: "))
            if producto in productos_seleccionados:
                productos_seleccionados[producto][0] += cantidad
            else:
                productos_seleccionados[producto] = [cantidad, productos[producto]]
            cantidades[producto] = cantidades.get(producto, 0) + cantidad
            continuar = input("¿Desea agregar más productos en esta categoría? (sí/no): ")
            if continuar.lower() != "sí":
                break
        continuar = input("¿Desea ir a otra categoría? (sí/no): ")
        if continuar.lower() != "sí":
            break

    datos_cliente = {
        "nombre": input("Ingrese su nombre: "),
        "direccion": input("Ingrese su dirección: ")
    }
    forma_pago = input("Seleccione la forma de pago (credito/debito/transferencia): ")
    descuento = calcular_descuento(sum(c[0] * c[1] for c in productos_seleccionados.values()), cantidades)
    factura(productos_seleccionados, datos_cliente, forma_pago, descuento)

if __name__ == "__main__":
    main()
