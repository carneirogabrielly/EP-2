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