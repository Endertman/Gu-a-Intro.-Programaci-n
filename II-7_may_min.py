print("determinar el numero mayor entre 3 numeros reales")
a = float(input("ingresa un valor para A: "))
b = float(input("ingresa un valor para B: "))
c = float(input("ingresa un valor para C: "))
if a > b and a > c:
  print("el numero mayor es A con el valor de: ", a)
elif b > a and b > c:
  print("el numero mayor es B con el valor de: ", b)
else:
  print("el numero mayor es C con el valor de: ", c)
