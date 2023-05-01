def posiciona_frota (frota):
    tabuleiro = []
    for i in range(10):
        tabuleiro.append([0]*10)
    for navio in frota:
        for posicao in frota[navio]:
            for coordenada in posicao:
                tabuleiro[coordenada[0]][coordenada[1]] = 1
    return tabuleiro