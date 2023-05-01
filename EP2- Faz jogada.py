#a função faz_jogada recebe o tabuleiro, uma linha e uma coluna
#se a posição tiver um navio, retorna 'X', se não, retorna '-'

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro [linha][coluna] = '-'
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    return tabuleiro