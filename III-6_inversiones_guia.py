inversion_inicial = int(input("Ingrese la cantidad a invertir: "))
años = 0
interes = 0.07 

while inversion_inicial < 3 * inversion_inicial:
    interes_anual = inversion_inicial * interes
    inversion_inicial += interes_anual
    años += 1

print("Se necesitan", años, "años para triplicar la inversión.")