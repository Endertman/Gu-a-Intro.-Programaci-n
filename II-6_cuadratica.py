import math
print("ecuacion de 2 grado, forma = ax^2+bx+c=0, (ax+c)^2 o (ax-c)^2")
a = int(input("ingresa el valor de a: "))
b = int(input("ingresa el valor de b: "))
c = int(input("ingresa el valor de c: "))
discriminante = b**2-4*a*c
if discriminante > 0:
  print("hay 2 soluciones reales")
  x1 = (-b+math.sqrt(discriminante))/2*a
  x2 = (-b-math.sqrt(discriminante))/2*a
  print(f"x1 es {x1} y x2 es {x2}")
elif discriminante == 0:
  print("hay 2 soluciones iguales")
  x = (-b+math.sqrt(discriminante))/2*a
  print("es igual a ", x,)
else:
  print("no hay soluciones reales")