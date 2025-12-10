alunos = []

for n in range(5):
    print(f'\n----- Aluno {n + 1}')
    nome = input('Informe o nome do aluno: ')
    
    notas = []
    for i in range(5):
        nota = float(input(f'Informe a nota {i + 1} '))
        notas.append(nota)
        
    media = sum(notas) / len(notas)
    print(media)

    aluno = {
        'Nome': nome,
        'Notas': notas,
        'media': media
    }

    alunos.append(aluno)
    # Exibindo os dados 
    for estudante in alunos:
        print(f'Nome: {estudante["Nome"]}')
        print(f'Notas: {estudante["Notas"]}')
        print(f'media: {estudante["media"]}\n')


    