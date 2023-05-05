
# varifica posição valida
lista_posicoes = []

# varifica se a  posição é valida
# linha_valida = True
valida_posicao = True
while valida_posicao:
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
    if [linha, coluna] not in lista_posicoes:
        lista_posicoes.append([linha, coluna])
        valida_posicao = False
    else:
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')

print(lista_posicoes)
