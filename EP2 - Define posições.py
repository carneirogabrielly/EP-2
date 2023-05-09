#  podemos pensar que ao acessar o elemento grid[0][1] estamos acessando a linha 0 e a coluna 1

#  1. implementar uma função chamada define_posicoes

# 2. recebe como argumentos uma linha, coluna, orientacao e um tamanho

# 3. função retorna uma lista com as posições que o navio irá ocupar

def define_posicoes (linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == "vertical":
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    else:
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    return posicoes