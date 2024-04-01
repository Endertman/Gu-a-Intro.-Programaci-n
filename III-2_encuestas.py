num = int(input("ingresa la cantidad de personas a encuestar: "))

edad = 0

mujeres = 0
mujeres_solteras = 0
edad_mujeres_solteras = 0
mujeres_solteras_mayores_edad = 0

hombres = 0
hombres_solteros = 0
hombres_casados = 0
edad_hombres_casados = 0
hombres_casados_menores_edad = 0  


for i in range(0,8):
  
  sexo = input("ingrese el sexo (1. Femenino, 2. Masculino ): ").lower()
  edad = int(input("ingrese la edad: "))
  estado_civil = input("ingrese el estado civil (1. Soltero, 2. Casado): ").lower()

  if sexo == 1 or sexo == 'femenino' or sexo == 'mujer':
    mujeres += 1
    if estado_civil == 1 or estado_civil == 'soltero':
      mujeres_solteras += 1
      edad_mujeres_solteras += edad
      if edad > 18:
        mujeres_solteras_mayores_edad += 1

  elif sexo == 2 or sexo == 'masculino' or sexo == 'hombre':
    hombres += 1
    if estado_civil == 1 or estado_civil  == 'soltero':
      hombres_solteros += 1
    elif estado_civil == 2 or estado_civil == 'casado':
      hombres_casados += 1
      edad_hombres_casados += edad
      if edad < 18:
        hombres_casados_menores_edad += 1

# Operaciones y mostrar en pantalla resultados
porcentaje_mujeres_solteras = (mujeres_solteras_mayores_edad/mujeres)*100
print('La cantidad de mujeres solteras mayores de es del ',porcentaje_mujeres_solteras, '%')

prom_edad_mujeres_solteras = (edad_mujeres_solteras/mujeres_solteras)
print('El promedio de edad de las mujeres solteras es de ', prom_edad_mujeres_solteras)

porcentaje_hombres = (hombres/num)*100
print('El porcentaje de hombres es del', porcentaje_hombres, '%')

porcentaje_hombres_solteros = (hombres/hombres_solteros)*100
print('El porcentaje de hombres solteros es del ', porcentaje_hombres,'%')

prom_edad_hombres_casados = (edad_hombres_casados/hombres_casados)
print('El promedio de edad de los hombres casados es de ', prom_edad_hombres_casados,'%')

porcentaje_hombres_casados_menores_edad = (hombres_casados_menores_edad/hombres)*100
print('El porcentaje de hombres casados menores de edad es del ', porcentaje_hombres_casados_menores_edad,'%')

promedio_edad = (edad/num)
print(f'El promedio de edad es de {promedio_edad}')