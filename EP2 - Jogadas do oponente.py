import random


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
    navios_afundados = 0
    for navio in frota:
        for posicao in frota[navio]:
            for coordenada in posicao:
                if tabuleiro[coordenada[0]][coordenada[1]] != 'X':
                    break
            else:
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
            # preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            
            i +=1
            # if coluna == tamanho and i <= qtd:
            #     break
            #print(frota)
            

        elif posicao_valida (frota, linha, coluna, orientacao, tamanho) == False:
            
            print ("Esta posição não está válida!")
            
#criando a frota do oponente      
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

#conta quantos navios o oponente tem:

quantidade_navios = 0
for navio in frota_oponente:
        for posicao in frota_oponente[navio]:
            quantidade_navios += 1

# conta qtds navios o jogador tem:

quantidade_navios_jogador = 0
for navio in frota:
        for posicao in frota[navio]:
            quantidade_navios_jogador += 1
        
#posicionando as frotas de jogador e oponente 
tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:
    
    #monta tabuleiros
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'

        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
        return texto

    #lista com as posições já atacadas
    
    posicoes_atacadas = []
    posicoes_oponente_atacou = []

    # verifica se a  posição é valida
    
    valida_posicao = True
    
    while valida_posicao:
        print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)) 
        linha = int(input("Qual a linha desejada para atacar? "))
        if linha > 9 or linha < 0:
            print("Linha inválida")
            while linha > 9 or linha < 0:
                linha = int(input("Qual a linha desejada para atacar? "))
                if linha > 9 or linha < 0:
                    print("Linha inválida")
                    # se a linha for valida, verifica a coluna
        coluna = int(input("Qual a coluna desejada para atacar? "))
        if coluna > 9 or coluna < 0:
            # if coluna > 9 and coluna < 0:
            print("Coluna inválida")
            while coluna > 9 or coluna < 0:
                coluna = int(input("Qual a coluna desejada para atacar? "))
                if coluna > 9 or coluna < 0:
                    print("Coluna inválida")
                    # se a coluna for valida, verifica se a posição já foi informada
        
        #verifica se a posição já foi atacada antes:
        
        if [linha, coluna] not in posicoes_atacadas:
            posicoes_atacadas.append([linha, coluna])
            #atualiza o tabuleiro do oponente
            tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna) 

        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
            
        #verifica se a frota do oponente já foi toda afundada: se não foi vai continuar validando posição, se foi vai acabar o jogo
        
        #ja contei quantos navios o oponente tinha, ta armazenado em quantidade_navios
        #se a quantidade de navios afundados foi igual a quantidade de navios, acaba o jogo
        
        navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
        if navios_afundados == quantidade_navios:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            valida_posicao = False
            jogando = False


        #função para o computador escolher uma posição aleatória para atacar
        else:
            
            sortear_linha = random.randint(0,9)
            sortear_coluna = random.randint(0,9)

            while [sortear_linha, sortear_coluna] in posicoes_oponente_atacou:
                sortear_linha = random.randint(0,9)
                sortear_coluna = random.randint(0,9)

            if [sortear_linha, sortear_coluna] not in posicoes_oponente_atacou:
                posicoes_oponente_atacou.append([sortear_linha, sortear_coluna])
                #atualiza o tabuleiro do jogador
                tabuleiro_jogador = faz_jogada(tabuleiro_jogador, sortear_linha, sortear_coluna)
                print(f'Seu oponente está atacando na linha {sortear_linha} e coluna {sortear_coluna}')

            navios_afundados_jogador = afundados(frota, tabuleiro_jogador)
            if navios_afundados_jogador == quantidade_navios_jogador:
                print('Xi! O oponente derrubou toda a sua frota =(')
                jogando = False
            

        