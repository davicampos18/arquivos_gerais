#Entrada / Solicitar ao usuário a quantidade de alunos matrículado para definir o FOR
alunos = int(input("Por gentileza, digite o número de alunos matrículado na matéria: "))

media = 0

#Entrada, processamento e saída de dados
for i in range(alunos):
  aluno = input(f"Digite o nome do aluno: ")
  nota1 = float(input(f"Digite a primeira nota de {aluno}: "))
  nota2 = float(input(f"Digite a segunda nota de {aluno}: "))
  nota3 = float(input(f"Digite a terceira nota de {aluno}: "))

  media_aluno = (nota1 + nota2 + nota3) / 3
  media += media_aluno

  if media_aluno >= 7:
    print(f"\n{aluno}, foi Aprovado com a média {media_aluno:.2f}!\n\nSua Primeira nota foi: {nota1:.2f};\nSua Segunda nota foi: {nota2:.2f};\nSua terceira nota foi: {nota3:.2f}.\n\n")
  elif media_aluno < 7:
    falta = 7 - media_aluno
    print(f"\n{aluno}, foi Reprovado com a média {media_aluno:.2f}, faltando {falta:.2f}!\n\nSua Primeira nota foi: {nota1:.2f};\nSua Segunda nota foi: {nota2:.2f};\nSua terceira nota foi: {nota3:.2f}.\n\n")

print(f"A média da turma é de {media:.2f}")