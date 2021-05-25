import random

perguntas = [
    ("Quanto é 5 + 3? ", 8),
    ("Quanto é a raiz quadrada de 16? ", 4),
    ("Quanto é 3 * 3? ", 9),
    ("Quano é 28 - 13? ", 15),
    ("Quanto é 20 / 4? ", 5),
    ("Quanto é 5 ^ 3? ", 125)
]
respostas = []
perguntasAleatorias = random.choices(perguntas, k = 3)

for x in range(len(perguntasAleatorias)):
    respostas.append(int(input(perguntasAleatorias[x][0])))

print("Gabarito:")
for x in range(len(perguntasAleatorias)):
    print(perguntasAleatorias[x])

acertos = 0
for x in range(len(perguntasAleatorias)):
    if perguntasAleatorias[x][1] == respostas[x]:
        acertos = acertos + 1

print("Você respondeu", acertos, "perguntas corretamente.")

if acertos >= 2:
    print("Você foi APROVADO!")
else:
    print("Você foi REPROVADO!")
