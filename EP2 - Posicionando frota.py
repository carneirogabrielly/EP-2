frota = {}

embarcacao = {   #primeiro termo da lista é o tamanho, o segundo é a quantidade de vezes que ele aparece
    "porta-aviões": [4,1],
    "navio-tanque": [3,2],
    "contratorpedeiro": [2,3],
    "submarino": [1,4],
}

for nome_navio in embarcacao:      # vai dar o nome_navio do navio
    tamanho = embarcacao[nome_navio][0]
    qtd = embarcacao[nome_navio][1]
    
    i = 0
    
    while i < qtd:
    
        print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(nome_navio,tamanho))
        linha = int(input("Qual a linha desejada para colocar a embarcação? "))
        coluna = int(input("Qual a coluna desejada para colocar a embarcação? "))
        if nome_navio != "submarino":
            orientacao = int(input("Qual a orientação desejada para colocar a embarcação? Digite 1 para vertical e 2 para horizontal "))
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
        else:
            orientacao = "horizontal" #escolha arbitrária
            
        #vai verificar se a posicao é valida
        
        if posicao_valida (frota, linha, coluna, orientacao, tamanho) == True:
            
            #vai atualizar a frota
            
            frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)

            i +=1
            
        elif posicao_valida (frota, linha, coluna, orientacao, tamanho) == False:
            
            print ("Esta posição não está válida!")
            
print(frota)

