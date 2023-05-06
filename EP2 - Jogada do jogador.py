        
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
        

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:
    
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
            #atualiza o tabulei do oponente
            tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna) 

        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
            
        #verifica se a frota do oponente já foi toda afundada: se não foi vai continuar validando posição, se foi vai acabar o jogo
        
        #primeiro vou ter que contar quantos navios o oponente tinha
        #ja fiz isso antes do inicio do loop, ta armazenado em quantidade_navios
        #se a quantidade de navios afundados foi igual a quantidade de navios, acaba o jogo
        
        navios_afundados = afundados(frota_oponente, tabuleiro_oponente)
        if navios_afundados == quantidade_navios:
            print('Parabéns! Você derrubou todos os navios do seu oponente!')
            valida_posicao = False
            jogando = False