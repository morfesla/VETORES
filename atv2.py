import os

os.system("cls")

vetor_nota = []
quantidade_notas = 4

print("Adicionando 4 notas")

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    vetor_nota.append(nota)

media = sum(vetor_nota) / quantidade_notas

print("\nExibindo as notas:")

for uma_nota in vetor_nota:
    print(f"Nota: {uma_nota}")

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")