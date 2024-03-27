cantidad = int(input("ingresa la cantidad de ventas: "))
i = 0
menor = 0
medio = 0
mayor = 0
while i  < cantidad:
  venta = int(input("ingresa el valor de la venta: "))
  if venta <= 200:
    menor += 1
    i += 1
  elif venta >200 and venta <400:
    medio +=1
    i += 1
  else: 
    mayor += 1
    i += 1
print(f"la cantidad de ventas menores o iguales a 200 Bs.F es de: {menor}")
print(f"la cantidad de ventas entre 200 y 400 Bs.F es de: {medio}") 
print(f"la cantidad de ventas mayores a 400 Bs.F es de: {mayor}")