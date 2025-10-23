from TADdeque import Deque

def maximo_d_deslizante(nums: list[int], k: int) -> list[int]:
    '''
    Retorna o maior elemento da d deslizante de tamanho *k*
    que percorre a lista *nums* da esquerda para à direita
    >>> maximo_d_deslizante([23, 32, 11, 11, 34, 43], 1)
    [23, 32, 11, 11, 34, 43]
    >>> maximo_d_deslizante([23, 32, 11, 11, 34, 43], 2)
    [32, 32, 11, 34, 43]
    >>> maximo_d_deslizante([2, 1, -1, 3, 4, 6, -2, 5], 3)
    [2, 3, 4, 6, 6, 6]
    '''
    d = Deque()
    resposta = []
    if k == 0 or len(nums) == 0:
        return []
    
    for i in range(len(nums)):
        if not d.vazia() and d.consulta_inicio() <= i - k: #Verifica se o elemento máximo faz parte da próxima d
            d.remove_inicio()
        while not d.vazia() and nums[i] > nums[d.consulta_fim()]: #Verifica se o elemento da lista é maior que o máximo atual armazenado no deque
            d.remove_fim()
        d.insere_fim(i)
        if i >= k - 1: #Começa a retornar apenas após o tamanho(k) especificado da d, o -1 é necessário pois o índice da lista começa em 0
            resposta.append(nums[d.consulta_inicio()])
    return resposta