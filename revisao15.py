# Li
alunos = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
notas = [7.5, 5.0, 6.0, 8.2, 4.5]

for nota in notas:
    if nota >= 6:
        indice = notas.index(nota)
        print(alunos[indice])