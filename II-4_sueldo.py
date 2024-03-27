trabajo1 = "ocupacion_uno"
trabajo2 = "ocupacion_dos"
trabajo3 = "ocupacion_tres"
trabajo4 = "ocupacion_tres"

horasTrabajadas1 = 12
sueldoPorHora1 = 3.20

horasTrabajadas2 = 10
sueldoPorHora2 = 4.10

horasTrabajadas3 = 8
sueldoPorHora3 = 3.80

horasTrabajadas4 = 13
sueldoPorHora4 = 2.95

def calculaSueldo(trabajo1 , horasTrabajadas1, sueldoPorHora1):
    return (horasTrabajadas1 * sueldoPorHora1)

salarioTotal = calculaSueldo(trabajo1, horasTrabajadas1, sueldoPorHora1) + \
              calculaSueldo(trabajo3, horasTrabajadas3, sueldoPorHora3) +\
              calculaSueldo(trabajo4, horasTrabajadas4, sueldoPorHora4)/4

print("El salario total es: $",format(salarioTotal, ".2f"))
