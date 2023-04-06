def calcular_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
notas = [6.5,8.5,9.5,9.0]
media = calcular_media(notas)
print('A média ', media)
