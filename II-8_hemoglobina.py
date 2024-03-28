print("programa para saber los niveles de hemoglobina")

edad = (int(input('Ingrese  edad, si tiene menos de un año de edad ingrese 0: ')))
if edad == 0:
  meses = (int(input('Ingrese  edad en numero de meses')))
  nivel_hemoglobina = float(input("ingresa los niveles de hemoglobina: "))
  if meses < 1:
    if nivel_hemoglobina >=13 and nivel_hemoglobina <=26:
      print("el nivel de hemoglobina es positivo")
    else:
      print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")
  elif meses >= 1 and meses <= 6:
    if nivel_hemoglobina >= 10 and nivel_hemoglobina <= 18:
      print("el nivel de hemoglobina es positivo")
    else:
      print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")
  elif meses >= 6 and meses <= 12:
    if nivel_hemoglobina >= 11 and nivel_hemoglobina <= 15:
      print("el nivel de hemoglobina es positivo")
    else:
      print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")
else:
  nivel_hemoglobina = float(input("ingresa los niveles de hemoglobina: "))
  if edad >= 5 and edad <= 10:
    if nivel_hemoglobina >= 12.6 and nivel_hemoglobina <= 15.5:
      print("el nivel de hemoglobina es positivo")
    else:
      print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")
  elif edad >= 10 and edad < 15:
    if nivel_hemoglobina >= 13 and nivel_hemoglobina <= 15.5:
      print("el nivel de hemoglobina es positivo")
    else:
      print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")
  elif edad >= 15:
    sexo = input("ingresa el sexo, 1. masculino o 2. femenino: ")
    sexo = sexo.upper()
    sexo = sexo.lower()
    if sexo == "masculino" or sexo == 1:
      if nivel_hemoglobina >= 14 and nivel_hemoglobina <= 18:
        print("el nivel de hemoglobina es positivo")
      else:
        print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")
    elif sexo == "femenino" or sexo == 2:
      if nivel_hemoglobina >= 12 and nivel_hemoglobina <= 16:
        print("el nivel de hemoglobina es positivo")
      else:
        print("el nivel de hemoglobina es negativo, tiene posibilidad de anemia")

