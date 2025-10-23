from TADdeque import Deque

def max_janela(nums: list[int], k: int) -> list[int]:
    '''
    Retorna o maior elemento da d deslizante de tamanho *k*
    que percorre a lista *nums* da esquerda para à direita
    >>> max_janela([23, 32, 11, 11, 34, 43], 1)
    [23, 32, 11, 11, 34, 43]
    >>> max_janela([23, 32, 11, 11, 34, 43], 2)
    [32, 32, 11, 34, 43]
    >>> max_janela([2, 1, -1, 3, 4, 6, -2, 5], 3)
    [2, 3, 4, 6, 6, 6]
    '''
    d = Deque()
    resposta = []
    if k == 0 or len(nums) == 0:
        return []
    
    for i in range(len(nums)):
        if not d.vazia() and d.consulta_inicio() <= i - k: #Verifica se o elemento máximo faz parte da janela
            d.remove_inicio()                              #Não realiza a iteração com a lista vazia para não lançar um erro
        
        while not d.vazia() and nums[i] > nums[d.consulta_fim()]: #Verifica se o elemento da lista é candidato a ser o maior     
            d.remove_fim()
        d.insere_fim(i)
        if i >= k - 1: #Começa a retornar apenas após o tamanho(k) especificado da d, o -1 é necessário pois o índice da lista começa em 0
            resposta.append(nums[d.consulta_inicio()])
    return resposta