def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero/2) + 1): #Neste caso ele divide o numero por 2 e soma 1, isso faz com que o range fique entre 2 até o a metade do numero +1
        if numero % i == 0:
            return False
    return True
    
numero = 53

if verificar_primo(numero):
    print(numero, 'é primo')
else:
    print(numero,'não é primo')