print('Programa para calcular el peso promedio de un grupo de personas')

peso_niños = 0
num_niños = 0
peso_jovenes = 0
num_jovenes = 0
peso_adultos = 0
num_adultos = 0
peso_ancianos = 0
num_ancianos = 0

num_personas = int(input('Ingrese el numero de personas a evaluar: '))

for i in range(0, num_personas):
  edad = int(input(f'Ingrese la edad de la persona {i+1}: '))
  peso = int(input(f'Ingrese el peso de la persona {i+1}: '))
  if edad < 13:
    peso_niños += peso
    num_niños += 1
  elif edad < 30:
    peso_jovenes += peso
    num_jovenes += 1
  elif edad < 60:
    peso_adultos += peso
    num_adultos +=1
  else:
    peso_ancianos += peso
    num_ancianos += 1

if num_niños == 0:
  print('No ingreso niños')
else:
  print(f'El peso promedio de los niños es: {peso_niños/num_niños}')

if num_jovenes == 0:
  print('No ingreso jovenes')
else:
  print(f'El peso promedio de los jovenes es: {peso_jovenes/num_jovenes}')

if num_adultos == 0:
  print('No ingreso adultos')
else:
  print(f'El peso promedio de los adultos es: {peso_adultos/num_adultos}')

if num_ancianos == 0:
  print('No ingreso ancianos')
else:
  print(f'El peso promedio de los ancianos es: {peso_ancianos/num_ancianos}')
