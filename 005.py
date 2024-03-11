num_alunos = int(input('Digite o número de alunos: '))

nomes_alunos = []
notas_matematica = []
notas_ciencias = []
notas_ingles = []

for i in range(num_alunos):

    nome = input(f"Digite o nome do Aluno {i + 1}: ")
    nomes_alunos.append(nome)

    nota_cien = float(input("Digite a nota de Ciências: "))
    notas_ciencias.append(nota_cien)

    nota_mat = float(input("Digite a nota de Matemática: "))
    notas_matematica.append(nota_mat)

    nota_ing = float(input("Digite a nota de Inglês: "))
    notas_ingles.append(nota_ing)


medias_ind = [sum(notas) / 3 for notas in zip(notas_matematica , notas_ingles , notas_ciencias)]

media_turma_mat = sum(notas_matematica) / num_alunos
media_turma_cien = sum(notas_ciencias) / num_alunos
media_turma_ing = sum(notas_ingles) / num_alunos

indice_maior_media = medias_ind.index(max(medias_ind))
aluno_maior_media = nomes_alunos[indice_maior_media]

print('\nMédias da Turma: ')
print(f'Média em Matemática: {media_turma_mat}')
print(f'Média em Inglês: {media_turma_ing}')
print(f'Média em Ciências: {media_turma_cien}')

print(f'\nO Aluno com a maior média geral é {aluno_maior_media}')