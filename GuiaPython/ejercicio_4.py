def division_enteros(a, b):
    cociente = 0
    while a >= b:
        a -= b
        cociente += 1
    return cociente, a

def main():
    a = int(input("Ingrese el valor de a (entero positivo): "))
    b = int(input("Ingrese el valor de b (entero positivo): "))
    
    if a < b:
        print("El valor de a debe ser mayor o igual que b.")
    else:
        cociente, resto = division_enteros(a, b)
        print(f"El cociente es {cociente} y el resto es {resto}.")

if __name__ == "__main__":
    main()
