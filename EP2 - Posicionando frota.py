def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:    
        frota[nome_navio] += ([define_posicoes(linha, coluna, orientacao, tamanho)])
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro [linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)
    for navio in frota:
        for posicao in frota[navio]:
            for coordenada in posicao:
                tabuleiro[coordenada[0]][coordenada[1]] = 1
    return tabuleiro

def afundados (frota, tabuleiro):
    print(frota)
    print(tabuleiro)
    navios_afundados = 0
    for navio in frota:            #navio é cada chave, representa o tipo de embarcação
        for posicao in frota[navio]:        # Posição é a lista com as listas = value, posição é como se fosse de fato cada navio daquele tipo
            afundou = True
            for coordenada in posicao:   #coordenada é cada lista dentro de cada posicao, ou seja, é a lista com as coordenadas
                if tabuleiro[coordenada[0]][coordenada[1]] != 'X':
                    afundou = False
            
                navios_afundados += 1
    return navios_afundados

def posicao_valida (frota, linha, coluna, orientacao, tamanho):

    novas_posicoes = define_posicoes (linha, coluna, orientacao, tamanho)       #novas_posições armazena as posições definidas pelo jogador, é uma lista de listas com dois valores

    #agora eu quero percorrer todas as coordenadas dessa lista e ver se tem alguma igual

    for navio in frota:
        for posicao in frota[navio]:
            for coordenada in posicao:
                for i in range (len(novas_posicoes)):
                    if novas_posicoes[i] == coordenada:
                        return False

    for i in range(len(novas_posicoes)):

        if novas_posicoes[i][0] >=10:
            return False
        elif novas_posicoes[i][1] >=10:
            return False

    return True
    
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

embarcacao = {   #primeiro termo da lista é o tamanho, o segundo é a quantidade de vezes que ele aparece
    "porta-aviões": [4,1],
    "navio-tanque": [3,2],
    "contratorpedeiro": [2,3],
    "submarino": [1,4],
}

for nome_navio in embarcacao:      # vai dar o nome_navio do navio
    tamanho = embarcacao[nome_navio][0]
    qtd = embarcacao[nome_navio][1]

    for i in range(qtd):  #vai repetir a pergunta das informações 
        
        print("Insira as informações referentes ao navio {} que possui tamanho {}".format(nome_navio,tamanho))
        linha = int(input("Qual a linha desejada para colocar a embarcação? "))
        coluna = int(input("Qual a coluna desejada para colocar a embarcação? "))
        if nome_navio != "submarino":
            orientacao = input("Qual a orientação desejada para colocar a embarcação? Digite 1 para vertical e 2 para horizontal")
            if orientacao == 1:
                orientacao = "vertical"
            elif orientacao == 2:
                orientacao = "horizontal"
        if nome_navio == "submarino":
            orientacao = "horizontal" #escolha arbitrária
            
        #vai verificar se a posicao é valida
        
        if posicao_valida (frota, linha, coluna, orientacao, tamanho) == True:
            
            frota = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            
        elif posicao_valida (frota, linha, coluna, orientacao, tamanho) == False:
            print ("Esta posição não está válida!")
            
        
