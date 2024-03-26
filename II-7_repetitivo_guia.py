init = int(input('Bienvenido al programa para calcular area de formas geometricas, Presione 1 para continuar ->  '))
while init == 1:
  forma = int(input('Seleccione una de las siguentes formas: \n1. Cuadrado \n2. Circulo \n3. Triangulo \n -->'))
  if forma == 1:
    lado = int(input('Ingrese el valor del lado: '))
    area = lado * lado
    print('El area del cuadrado es: ', area)
    init = int(input('Sí desea continuar presione 1, sino presione cualquier otro numero ->  '))
  elif forma == 2:
    radio = int(input('Ingrese el valor del radio: '))
    area = 3.141590 * radio**2 
    print('El area del Circulo es: ', area)
    init = int(input('Sí desea continuar presione 1, sino presione cualquier otro numero ->  '))
  elif forma == 3:
    base = int(input('Ingrese el valor de la base: '))
    altura = int(input('Ingrese el valor de la altura: '))
    area = (base * altura) / 2
    print('El area del Triangulo es: ', area)
    init = int(input('Sí desea continuar presione 1, sino presione cualquier otro numero ->  '))
  else:
    print('Ingrese una opcion valida')
    