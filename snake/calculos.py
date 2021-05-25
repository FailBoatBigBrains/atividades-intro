import math

def calcular_media_simples(x, y):
    media_simples = (x + y) / 2
    print(media_simples)
    return media_simples

def calcular_media_ponderada(x, y, p1, p2):
    media_ponderada = ((x * p1) + (y * p2)) / (p1 + p2)
    print(media_ponderada)
    return media_ponderada

def calcular_area_de_triangulo(a, b, c):
    s = (a + b + c) / 2
    area_triangulo = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area_triangulo

def calcular_media_simples_2(lista):
    soma = 0
    for i in lista:
        soma += i
    media_simples_2 = soma / len(lista)
    print(media_simples_2)
    return media_simples_2

def calcular_media_ponderada_2(lista):
    dividendo = 0
    divisor = 0
    for x in range(len(lista)):
        dividendo += lista[x][0] * lista[x][1]
        divisor += lista[x][1]
    media_ponderada_2 = dividendo / divisor
    print(media_ponderada_2)
    return media_ponderada_2

def calcular_area_de_triangulo_ou_retangulo(a, b, c = None):
    if c is None:
        area = a * b
    else:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(area)
    return area
