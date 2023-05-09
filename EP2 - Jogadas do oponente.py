import random


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
                valida_posicao = False
                jogando = False
            

