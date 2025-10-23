from TADdeque import Deque

def maximo_janela_deslizante(nums: list[int], k: int) -> list[int]:
    '''
    Retorna o maior elemento da janela deslizante de tamanho *k*
    que percorre a lista *nums* da esquerda para à direita

    '''
    janela = Deque()
    resposta = Deque()
    if k == 0 or len(nums) == 0:
        return []
    janela.insere_inicio(0)
    for i in range(len(nums)):
        if nums[janela.consulta_inicio()] <= nums[i]:
            janela.remove_inicio()
            janela.insere_fim(i)
        if i >= k - 1:
            resposta.insere_fim(nums[janela.consulta_inicio()])
        elif janela.consulta_inicio == i - k + 1:
            janela.remove_inicio()
            janela.insere_fim(i)    
    return resposta

print(maximo_janela_deslizante([2, 1, -1, 3, 4, 6, -2, 5], 3))