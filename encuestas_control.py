print('Bienvenido al programa para procesar encuestas')
encuestados = int(input('Ingrese la cantidad de encuestados: '))

#promedio de edad de mujeres casadas de ojos negros que ganan mas de 3000
suma_edades_mujeres_casadas_negros_mas_3000 = 0
contador_mujeres_casadas_negros_mas_3000 = 0

#numero de mujeres solteras de ojos azules de 30 años que ganan mas de 4000
num_mujeres_solteras_azules_30_mas_4000 = 0

#numero hombres casados de mas_ de 25 que ganan mas de 1000
num_hombres_casados_mayores_25_1000 = 0

#numero hombres solteros de ojos marrones de 20 a 45 años que ganan mas de 2000
num_hombres_solteros_marrones_20_45_mas_2000 = 0

#numero hombres menores de 40 que ganan mas de 3000
num_hombres_menores_40_mas_3000 = 0

#Promedio de sueldo de empleados mayores de 40 y sueldo mayor a 5000
suma_sueldos_mayores_40_mas_5000 = 0
contador_sueldos_mayores_40_mas_5000 = 0

for i in range(0,encuestados):
  sexo = int(input('Ingrese sexo (1. Femenino, 2. Masculino: )'))
  edad = int(input('Ingrese edad: '))
  sueldo = int(input('Ingrese el sueldo: '))
  estado_civil = int(input('Ingrese el estado civil (1. Casado, 2. Soltero: )'))
  
  if sexo == 1:
    ojos = int(input('Ingrese el color de ojos (1. azul, 2. marron 3. negro): '))
    if estado_civil == 1 and sueldo > 3000 and ojos == 3:
      suma_edades_mujeres_casadas_negros_mas_3000 += edad
      contador_mujeres_casadas_negros_mas_3000 += 1
    else:
      if edad == 30 and sueldo > 4000 and ojos == 1:
        num_mujeres_solteras_azules_30_mas_4000 += 1
  else:
    if edad > 25 and sueldo > 1000:
      num_hombres_casados_mayores_25_1000 += 1
    elif edad > 20 and sueldo > 2000:
      ojos = int(input('Ingrese el color de ojos (1. azul, 2. marron 3. negro): '))
      if ojos == 2:
        num_hombres_solteros_marrones_20_45_mas_2000 += 1
    elif edad < 40 and sueldo > 3000: 
      num_hombres_menores_40_mas_3000 += 1
    
  if edad > 40 and sueldo > 5000:
    suma_sueldos_mayores_40_mas_5000 += sueldo
    contador_sueldos_mayores_40_mas_5000 += 1
  
if contador_mujeres_casadas_negros_mas_3000 != 0:
  print(f'EL promedio de edad de mujeres casadas de ojos negros que ganan mas de 3000 es {suma_edades_mujeres_casadas_negros_mas_3000 / contador_mujeres_casadas_negros_mas_3000}')
else:
  print('No se registro eL promedio de edad de mujeres casadas de ojos negros que ganan mas de 3000')
 
print(f'El numero de mujeres solteras de ojos azules de 30 años que ganan mas de 4000 es {num_mujeres_solteras_azules_30_mas_4000}')

print(f'El numero hombres casados de mas de 25 que ganan mas de 1000 es {num_hombres_casados_mayores_25_1000}')

print(f'El numero hombres solteros de ojos marrones de 20 a 45 años que ganan mas de 2000 es {num_hombres_solteros_marrones_20_45_mas_2000}')

print(f'El numero hombres menores de 40 que ganan mas de 3000 es {num_hombres_menores_40_mas_3000}')

if contador_sueldos_mayores_40_mas_5000 != 0:
  print(f'El promedio de sueldo de empleados mayores de 40 y sueldo mayor a 5000 {suma_sueldos_mayores_40_mas_5000/contador_sueldos_mayores_40_mas_5000}')
else: 
  print('No se registro el promedio de sueldo de empleados mayores de 40 y sueldo mayor a 5000 ')
 
#Datos para probar
  #Mujer soltera, 30 años, sueldo: 4500, ojos: azul
  #Hombre casado, 28 años, sueldo: 1500
  #Hombre soltero, 40 años, sueldo: 2200, ojos: marrón
  #Hombre soltero, 27 años, sueldo: 2800, ojos: marrón
  #Hombre casado, 45 años, sueldo: 6000
      
        

    
  






