from __future__ import annotations
from typing import Any
from dataclasses import dataclass

@dataclass
class No:
    elemento: Any
    anterior: No|None = None
    proximo: No|None = None

class ListaDuplamenteEncadeadaircularcomSentinela:
    def __init__(self) -> None:
        '''Cria uma lista duplamente encadeada vazia.'''
        self.sentinela=No(None)
        self.sentinela.proximo=self.sentinela
        self.sentinela.anterior=self.sentinela
        self.num_elementos=0

    def vazia(self) -> bool:
        '''Devolve True se a lista não possui elementos e False caso contrário.
        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> lista.vazia()
        True
        >>> lista.insere_inicio(1)
        >>> lista.vazia()
        False
        '''
        return self.sentinela.proximo==self.sentinela
    
    def __len__(self) -> int:
        '''Devolve a quantidade de elementos que estão na lista.    
        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> len(lista)
        0
        >>> lista.insere_inicio(1)
        >>> len(lista)
        1
        >>> lista.insere_inicio(2)
        >>> lista.insere_inicio(3)
        >>> len(lista)
        3
        '''
        return self.num_elementos

    def __str__(self) -> str:
        '''Devolve a representação da lista em formato de string.'''
        aux= self.sentinela
        resp= '['
        for _ in range(self.num_elementos):
            if aux.proximo.proximo==self.sentinela: #se for último elemento
                resp += f'{aux.proximo.elemento}'
            else:
                resp+= f'{aux.proximo.elemento}, '
            aux = aux.proximo    
        resp += ']'
        return resp

    def insere_inicio(self, item: Any) -> None:
        '''insere_inicio um novo nó contendo o elemento **item** em uma **posição** específica na lista duplamente encadeada. A 
        contagem das posições começa em 0 (ou seja, a 
        primeira posição da lista é a posição 0), e o valor de 
        **posicao** deve ser entre 0 e a quantidade de elementos 
        (inserção após o último elemento da lista atual). Se não 
        for informada a posição, a inserção será feita no final da
        lista.
        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> lista.insere_inicio(1)
        >>> print(lista)
        [1]
        >>> lista.insere_inicio(2)
        >>> print(lista)
        [2, 1]
        >>> lista.insere_inicio(3)
        >>> print(lista)
        [3, 2, 1]
        >>> lista.insere_inicio(4)
        >>> print(lista)
        [4, 3, 2, 1]
        '''

        Novo=No(item)
        Novo.proximo=self.sentinela.proximo
        Novo.anterior=self.sentinela
        self.sentinela.proximo.anterior=Novo
        self.sentinela.proximo=Novo

        self.num_elementos+=1

    def insere_fim(self, item: Any) -> None:
        '''insere_inicio um novo nó contendo o elemento **item** em uma **posição** específica na lista duplamente encadeada. A 
        contagem das posições começa em 0 (ou seja, a 
        primeira posição da lista é a posição 0), e o valor de 
        **posicao** deve ser entre 0 e a quantidade de elementos 
        (inserção após o último elemento da lista atual). Se não 
        for informada a posição, a inserção será feita no final da
        lista.
        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> lista.insere_fim(1)
        >>> print(lista)
        [1]
        >>> lista.insere_fim(2)
        >>> print(lista)
        [1, 2]
        >>> lista.insere_fim(3)
        >>> print(lista)
        [1, 2, 3]
        >>> lista.insere_fim(4)
        >>> print(lista)
        [1, 2, 3, 4]
        '''

        Novo=No(item)
        Novo.anterior = self.sentinela.anterior
        self.sentinela.anterior.proximo = Novo
        Novo.proximo = self.sentinela
        self.sentinela.anterior = Novo

        self.num_elementos+=1


    def remove(self, posicao: int = None) -> None:
        '''Remove o nó que está em uma **posicao** específica
        na lista duplamente encadeada. As posições começam em 0 e o
        valor de **posicao** deve estar entre 0 e a 
        quantidade de elementos - 1 (último elemento da lista).
        Se posição não for especificada, remove do fim.
        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> for i in range(10):
        ...    lista.insere_inicio(i * 10)
        >>> print(lista)
        [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
        >>> lista.remove(2)
        >>> print(lista)
        [0, 10, 30, 40, 50, 60, 70, 80, 90]
        >>> lista.remove(7)
        >>> print(lista)
        [0, 10, 30, 40, 50, 60, 70, 90]
        >>> lista.remove(4)
        >>> print(lista)
        [0, 10, 30, 40, 60, 70, 90]
        >>> lista.remove(0)
        >>> print(lista)
        [10, 30, 40, 60, 70, 90]
        >>> lista.remove(5)
        >>> print(lista)
        [10, 30, 40, 60, 70]
        '''
        if posicao is not None and (posicao < 0 or posicao >= self.num_elementos):
            raise IndexError('índice inválido.')
        
        if self.vazia():
            raise ValueError('lista vazia.')
        
        #Se só tiver um elemento
        if self.num_elementos==1:
            self.sentinela.proximo = self.sentinela
            self.sentinela.anterior = self.sentinela

        #Se não passar posição,tira do final
        elif posicao is None or posicao == self.num_elementos-1: # (-1 por causa da sentinela)
            


    def consulta(self, i: int) -> Any: #inicio e fim
        '''Devolve o conteúdo do nó localizado na posição *i* da lista duplamente encadeada sem removê-lo.
        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> lista.consulta(0)
        Traceback (most recent call last):
            ...
        ValueError: Lista vazia.
        >>> lista.insere_inicio(1)
        >>> lista.insere_inicio(2)
        >>> lista.insere_inicio(3)
        >>> print(lista)
        [3, 2, 1]
        >>> lista.consulta(2)
        3
        >>> lista.consulta(0)
        1
        >>> lista.consulta(1)
        2
        '''
        pass

    def busca_indice(self, elemento: Any) -> int:
        '''
        Devolve a posição do primeiro **elemento** encontrado na lista (considera
        0 a primeira posição da lista). Caso **elemento** não esteja na lista
        duplamente encadeada, o resultado será -1.

        Exemplos:
        >>> lista = ListaDuplamenteEncadeada()
        >>> for i in range(10):
        ...    lista.insere_inicio(i * 10)
        >>> lista.busca_indice(45)
        -1
        >>> lista.busca_indice(20)
        2
        >>> lista.busca_indice(70)
        7
        '''
        pass
