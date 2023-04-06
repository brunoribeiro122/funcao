def ano_bi(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True
#anos para comparar
dados_teste = [1900,2000,2016,1987,2020]
#resultado real
resultados_reais = [False, True, True, False, True]#Neste caso o codigo esta verificando e a funcao esta certa ou não
#checar funcao
for i in range(len(dados_teste)):
    yr = dados_teste[i] #Atribui o contador da repetição a variavel yr
    print(dados_teste[i],'->', end='')
    result = ano_bi(yr) #Adiciona a variavel yr dentro da função
    if result == resultados_reais[i]:
        print('Ok')
    else: 
        print('Falha')