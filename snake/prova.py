import random

perguntas = [
    ("Quanto é 5 + 3? ", 8),
    ("Quanto é a raiz quadrada de 16? ", 4),
    ("Quanto é 3 * 3? ", 9),
    ("Quanto é 28 - 13? ", 15),
    ("Quanto é 20 / 4? ", 5),
    ("Quanto é 5 ^ 3? ", 125)
]
respostas = []
perguntasAleatorias = random.choices(perguntas, k = 3)

for questao, gabarito in perguntasAleatorias:
    respostas.append(int(input(questao)))

print("Gabarito:")
for x in perguntasAleatorias:
    print(x)

acertos = 0
for cont, valor in enumerate(perguntasAleatorias):
    if valor[1] == respostas[cont]:
        acertos = acertos + 1

print("Você respondeu", acertos, "perguntas corretamente.")

if acertos >= 2:
    print("Você foi APROVADO!")
else:
    print("Você foi REPROVADO!")
