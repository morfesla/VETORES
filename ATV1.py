import os

os.system('cls' if os.name == 'nt' else 'clear')

vetor_nota = []
quantidade_notas = 3

print("Adicionando 3 notas")

for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    vetor_nota.append(nota)

media = sum(vetor_nota) / quantidade_notas

print("\nExibindo as notas:")

for uma_nota in vetor_nota:
    print(f"Nota: {uma_nota}")

print(f"Média: {media}")