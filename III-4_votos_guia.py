print('Programa para contabilizar votos')

candidato_a = 0
candidato_b = 0
candidato_c = 0

num_votos = int(input('Ingrese el numero de votos: '))

while num_votos != 0:
  print('Seleccione uno de los siguentes candidatos: \n1. Candidato A \n2. Candidato B \n3. Candidato C')
  voto = int(input('Ingrese el voto: '))
  if voto == 1:
    candidato_a += 1
    num_votos -= 1
  elif voto == 2:
    candidato_b += 1
    num_votos -= 1
  elif voto == 3:
    candidato_c += 1
    num_votos -= 1
  else:
    print('Voto invalido')

print(f'El candidato A obtuvo {candidato_a} votos,\nEl candidato B obtuvo {candidato_b} votos,\nEl candidato C obtuvo {candidato_c} votos')