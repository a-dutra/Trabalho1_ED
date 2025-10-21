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


    def remove_fim(self) -> None:
        '''
        remove o nó que está no fim
        da lista duplamente encadeada circular com sentinela
        Exemplos:
        >>> lista = ListaDuplamenteEncadeadaircularcomSentinela()
        >>> for i in range(10):
        ...    lista.insere_inicio(i * 10)
        >>> print(lista)
        [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        >>> lista.remove_fim()
        >>> print(lista)
        [90, 80, 70, 60, 50, 40, 30, 20, 10]
        >>> lista.remove_fim()
        >>> print(lista)
        [90, 80, 70, 60, 50, 40, 30, 20]
        >>> lista.remove_fim()
        >>> print(lista)
        [90, 80, 70, 60, 50, 40, 30]
        >>> lista.remove_fim()
        >>> print(lista)
        [90, 80, 70, 60, 50, 40]
        >>> lista.remove_fim()
        >>> print(lista)
        [90, 80, 70, 60, 50]
        >>> lista2 = ListaDuplamenteEncadeadaircularcomSentinela()
        >>> lista2.insere_fim(2)
        >>> print(lista2)
        [2]
        >>> lista2.remove_fim()
        >>> print(lista2)
        []
        '''        
        if self.vazia():
            raise ValueError('lista vazia.')
        
        #Se tiver um elemento
        if self.num_elementos == 1:
            self.sentinela.proximo.proximo = None  #Usado apenas para o nó deletado não apontar para lugares indesejados 
            self.sentinela.proximo.anterior = None #[...]
            self.sentinela.proximo = self.sentinela
            self.sentinela.anterior = self.sentinela
        else:
            self.sentinela.anterior = self.sentinela.anterior.anterior
            self.sentinela.anterior.proximo.anterior = None #Usado apenas para o nó deletado não apontar para lugares indesejados
            self.sentinela.anterior.proximo.proximo = None  #[...]
            self.sentinela.anterior.proximo = self.sentinela





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
