print('Bienvenido al programa para procesar encuestas')
encuestados = int(input('Ingrese la cantidad de encuestados: '))

num_hombres_casados_mayores_25 = 0
num_hombres_solteros_marrones_20_45_mas_2000 = 0
num_hombres_menores_40_mas_3000 = 0
num_mujeres_solteras_azules_30_mas_4000 = 0
suma_edades_mujeres_casadas_negros_mas_3000 = 0
contador_mujeres_casadas_negros_mas_3000 = 0
suma_sueldos_mayores_40_mas_5000 = 0
contador_sueldos_mayores_40_mas_5000 = 0

for i in range(0, encuestados):
  edad = int(input("Edad: "))
  sexo = input("Sexo (H/M): ").lower
  salario = int(input("Salario: "))
  color_ojos = input(
      "Color de ojos (1. azules, 2. marrones, 3. negros): ").lower
  estado_civil = input("Estado civil (1. casado, 2. soltero): ").lower

  if sexo == 'h' or sexo == 'hombre':

    if estado_civil == "casado" or estado_civil == "1" and edad > 25 and salario > 1000:
      num_hombres_casados_mayores_25 += 1
    elif estado_civil == "soltero" or estado_civil == "2" and color_ojos == "2" and 20 <= edad <= 45 and salario > 2000:
      num_hombres_solteros_marrones_20_45_mas_2000 += 1
    elif edad < 40 and salario > 3000:
      num_hombres_menores_40_mas_3000 += 1

  elif sexo == "M":

    if estado_civil == "soltero" or estado_civil == "2" and color_ojos == "1" and edad == 30 and salario > 4000:
      num_mujeres_solteras_azules_30_mas_4000 += 1
    elif estado_civil == "casado" or estado_civil == "1" and color_ojos == "3" and salario > 3000:
      suma_edades_mujeres_casadas_negros_mas_3000 += edad
      contador_mujeres_casadas_negros_mas_3000 += 1

  if edad > 40 and salario > 5000:
    suma_sueldos_mayores_40_mas_5000 += salario
    contador_sueldos_mayores_40_mas_5000 += 1

print("Número de hombres casados mayores de 25 que ganan más de 1000:",
      num_hombres_casados_mayores_25)
print(
    "Número de hombres solteros de ojos marrones de 20 a 45 años que ganan más de 2000:",
    num_hombres_solteros_marrones_20_45_mas_2000)
print("Número de hombres menores de 40 que ganan más de 3000:",
      num_hombres_menores_40_mas_3000)
print(
    "Número de mujeres solteras de ojos azules de 30 años que ganan más de 4000:",
    num_mujeres_solteras_azules_30_mas_4000)
