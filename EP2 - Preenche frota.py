# EP2 - Preenche frota

#devemos armazenar as posições
#implementar uma função chamada preenche_frota
#preenche_frota dese retornar o dicionario de frota com as informações do novo navio

#se a chave já existir no dicionario, ele adiciona uma nova lista aos valores
#se a chave nao existir, ele adiciona o item


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:    
        frota[nome_navio].extend([define_posicoes(linha, coluna, orientacao, tamanho)])
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota