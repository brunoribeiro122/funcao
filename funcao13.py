#palindromo = palavra ou frase que se pode ler
#indiferentemente, da esquerda para a direita ou vice-versa.

def verificar_palindromo(texto):
    texto = texto.lower().replace(" ","")
    return texto == texto[::-1]

#text[::-1] inverte o texto

texto = 'a gorda ama a droga'
if verificar_palindromo(texto):
    print(texto, 'é um palíndromo')
else:
    print(texto, 'não é um palíndromo.')

