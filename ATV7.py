import os

os.system("cls")

numeros = []
negativos = 0
soma_positivos = 0

# Preenchendo o vetor
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# Processando os dados
for num in numeros:
    if num < 0:
        negativos += 1
    elif num > 0:
        soma_positivos += num

# Resultado
print(f"Quantidade de números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")