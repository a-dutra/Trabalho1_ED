from TADdeque import Deque

def maximo_janela_deslizante(nums: list[int], k: int) -> list[int]:
    '''
    Retorna o maior elemento da janela deslizante de tamanho *k*
    que percorre a lista *nums* da esquerda para à direita
    >>> maximo_janela_deslizante([23, 32, 11, 11, 34, 43], 1)
    [23, 32, 11, 11, 34, 43]
    >>> maximo_janela_deslizante([23, 32, 11, 11, 34, 43], 2)
    [32, 32, 11, 34, 43]
    >>> maximo_janela_deslizante([2, 1, -1, 3, 4, 6, -2, 5], 3)
    [2, 3, 4, 6, 6, 6]
    '''
    janela = Deque()
    resposta = Deque()
    if k == 0 or len(nums) == 0:
        return []
    janela.insere_inicio(0)
    for i in range(len(nums)):
        if nums[janela.consulta_inicio()] <= nums[i]: #Verifica se o elemento da lista é maior que o máximo atual armazenado no deque
            janela.remove_inicio()
            janela.insere_fim(i)
        if janela.consulta_inicio() == i - k: #Remove o elemento máximo se ele não fizer parte da janela atuals
            janela.remove_inicio()
            janela.insere_fim(i)
        if i >= k - 1: #Começa a retornar apenas após o tamanho(k) especificado da janela, o -1 é necessário pois o índice da lista começa em 0
            resposta.insere_fim(nums[janela.consulta_inicio()])
    return print(resposta)