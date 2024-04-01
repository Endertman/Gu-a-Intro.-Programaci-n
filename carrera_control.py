print("Programa para determinar si un estudiante es apto para seguir cursando la carrera")

carrera = int(input("ingrese la carrera: \n1. Economia \n2. Computación \n3. Administrativo \n4. Contabilidad \n"))
            
if carrera == "economia" or carrera == 1:
  año = int(input("ingrese el año: "))
  semestre = int(input("ingrese el semestre: "))
  promedio = int(input("ingrese el promedio: "))
  if año <= 2 and semestre > 3 and promedio > 15:
    print("El estudiante es apto para seguir cursando la carrera de economia")
  else: 
    print("El estudiante no es apto para seguir cursando la carrera de economia")

elif  carrera == "computacion" or carrera == 2:       
  año = int(input("ingrese el año: "))
  semestre = int(input("ingrese el semestre: "))
  promedio = int(input("ingrese el promedio: "))
  if año <= 3 and semestre > 5 and promedio > 13:
    print("El estudiante es apto para seguir cursando la carrera computacion")
  else: 
    print("El estduiante no es apto para seguir cursando la carrera computacion")
  
elif carrera == "administrativo" or carrera == 3:
  año = int(input("ingrese el año: "))
  semestre = int(input("ingrese el semestre: "))
  promedio = int(input("ingrese el promedio: "))
  if año <= 4 and semestre > 6 and promedio > 14:
    print("El estudiante es apto para seguir cursando la carrera de administracion")
  else: 
    print("El estuduiante no es apto para seguir cursando la carrera administracion")

elif carrera == "contabilidad" or carrera == 4:
  año = int(input("ingrese el año: "))
  semestre = int(input("ingrese el semestre: "))
  promedio = int(input("ingrese el promedio: "))
  if año <= 5 and semestre > 7 and promedio > 12:
    print("El estudiante es apto para seguir cursando la carrera de contabilidad")
  else:
    print("El estuduiante no es apto para seguir cursando la carrera contabilidad")
else:
  print("error")  

