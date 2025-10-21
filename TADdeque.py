from __future__ import annotations
from typing import Any
from dataclasses import dataclass

@dataclass
class No:
    ''' Um tipo de dado que permite representar um número
        indeterminado de dados(fluxo dados), devido a
        autorreferência(O prórpio dado) e representação de ausência de valor(None)'''
    elemento: Any
    anterior: No|None = None
    proximo: No|None = None

#Double Ended Queue (Fila Duplamente Terminada)
#Implementação Realizada de maneira circular, dinâmica e com um nó sentinela
#A sentinela serve para fins de simplificação lógica e por consequência volume de código
class Deque:
    '''Um tipo especial de fila que permite operações em ambas extremidades'''
    def __init__(self) -> None:
        '''Cria um Deque vazio.'''
        self.sentinela=No(None)
        self.sentinela.proximo = self.sentinela
        self.sentinela.anterior = self.sentinela
        self.num_elementos = 0

    def vazia(self) -> bool:
        '''
        Devolve True se o Deque não possui elementos e False caso contrário.
        Exemplos:
        >>> FilaDupla = Deque()
        >>> FilaDupla.vazia()
        True
        >>> FilaDupla.insere_inicio(1)
        >>> FilaDupla.vazia()
        False
        '''
        return self.sentinela.proximo == self.sentinela
    
    def __len__(self) -> int:
        '''
        Devolve a quantidade de elementos que estão no Deque.    
        Exemplos:
        >>> FilaDupla = Deque()
        >>> len(FilaDupla)
        0
        >>> FilaDupla.insere_inicio(1)
        >>> len(FilaDupla)
        1
        >>> FilaDupla.insere_inicio(2)
        >>> FilaDupla.insere_inicio(3)
        >>> len(FilaDupla)
        3
        '''
        return self.num_elementos

    def __str__(self) -> str:
        '''Devolve a representação do Deque em formato de string.'''
        aux= self.sentinela
        resp= '['
        for _ in range(self.num_elementos):
            if aux.proximo.proximo == self.sentinela: #se for último elemento
                resp += f'{aux.proximo.elemento}'
            else:
                resp += f'{aux.proximo.elemento}, '
            aux = aux.proximo   
        resp += ']'
        return resp

    def insere_inicio(self, item: Any) -> None:
        '''
        Insere um novo nó com o elemento **item**
        no início da Deque.
        Exemplos:
        >>> FilaDupla = Deque()
        >>> FilaDupla.insere_inicio(1)
        >>> print(FilaDupla)
        [1]
        >>> FilaDupla.insere_inicio(2)
        >>> print(FilaDupla)
        [2, 1]
        >>> FilaDupla.insere_inicio(3)
        >>> print(FilaDupla)
        [3, 2, 1]
        >>> FilaDupla.insere_inicio(4)
        >>> print(FilaDupla)
        [4, 3, 2, 1]
        '''

        Novo = No(item)
        Novo.proximo = self.sentinela.proximo
        Novo.anterior = self.sentinela
        self.sentinela.proximo.anterior = Novo
        self.sentinela.proximo = Novo

        self.num_elementos+=1

    def insere_fim(self, item: Any) -> None:
        '''
        Insere um novo nó com o elemento **item**
        no final do Deque.
        Exemplos:
        >>> FilaDupla = Deque()
        >>> FilaDupla.insere_fim(1)
        >>> print(FilaDupla)
        [1]
        >>> FilaDupla.insere_fim(2)
        >>> print(FilaDupla)
        [1, 2]
        >>> FilaDupla.insere_fim(3)
        >>> print(FilaDupla)
        [1, 2, 3]
        >>> FilaDupla.insere_fim(4)
        >>> print(FilaDupla)
        [1, 2, 3, 4]
        '''

        Novo=No(item)
        Novo.anterior = self.sentinela.anterior
        self.sentinela.anterior.proximo = Novo
        Novo.proximo = self.sentinela
        self.sentinela.anterior = Novo

        self.num_elementos+=1

    def remove_inicio(self) -> None:
        '''
        Remove o nó na primeira posição
        do Deque.
        >>> FilaDupla = Deque()
        >>> FilaDupla.remove_inicio()
        Traceback (most recent call last):
            ...
        ValueError: Deque Vazio.
        >>> for i in range(3):
        ...    FilaDupla.insere_fim(i * i)
        >>> print(FilaDupla)
        [0, 1, 4]
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        [1, 4]
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        [4]
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        []
        >>> FilaDupla.insere_inicio(576)
        >>> print(FilaDupla)
        [576]
        >>> FilaDupla.insere_fim(24)
        >>> print(FilaDupla)
        [576, 24]
        '''
        if self.vazia():
            raise ValueError("Deque Vazio.")
        
        if self.num_elementos == 1:
            self.sentinela.proximo.anterior = None
            self.sentinela.proximo.proximo = None
            self.sentinela.anterior = self.sentinela
            self.sentinela.proximo = self.sentinela
        else:
            self.sentinela.proximo = self.sentinela.proximo.proximo
            self.sentinela.proximo.anterior.anterior = None # self.sentinela.proximo.anterior é o elemento que será removido
            self.sentinela.proximo.anterior.proximo = None
            self.sentinela.proximo.anterior = self.sentinela
        self.num_elementos -= 1
    def remove_fim(self) -> None:
        '''
        Remove o nó que está no fim
        do Deque.
        Exemplos:
        >>> FilaDupla = Deque()
        >>> for i in range(10):
        ...    FilaDupla.insere_inicio(i * 10)
        >>> print(FilaDupla)
        [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [90, 80, 70, 60, 50, 40, 30, 20, 10]
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [90, 80, 70, 60, 50, 40, 30, 20]
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [90, 80, 70, 60, 50, 40, 30]
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [90, 80, 70, 60, 50, 40]
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [90, 80, 70, 60, 50]
        >>> FilaDupla2 = Deque()
        >>> FilaDupla2.insere_fim(2)
        >>> print(FilaDupla2)
        [2]
        >>> FilaDupla2.remove_fim()
        >>> print(FilaDupla2)
        []
        >>> FilaDupla2.remove_fim()
        Traceback (most recent call last):
            ...
        ValueError: Deque Vazio.
        '''        
        if self.vazia():
            raise ValueError('Deque Vazio.')
        
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

        self.num_elementos -= 1

    def consulta_inicio(self) -> Any:
        '''Devolve o conteúdo do nó localizado no começo
           do Deque sem removê-lo.
        Exemplos:
        >>> FilaDupla = Deque()
        >>> FilaDupla.consulta_inicio()
        Traceback (most recent call last):
            ...
        ValueError: Deque Vazio.
        >>> FilaDupla.insere_inicio(1)
        >>> FilaDupla.insere_inicio(2)
        >>> FilaDupla.insere_inicio(3)
        >>> print(FilaDupla)
        [3, 2, 1]
        >>> FilaDupla.consulta_inicio()
        3
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [3, 2]
        >>> FilaDupla.consulta_inicio()
        3
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        [2]
        >>> FilaDupla.consulta_inicio()
        2
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        []
        >>> FilaDupla.consulta_inicio()
        Traceback (most recent call last):
            ...
        ValueError: Deque Vazio.
        '''
        if self.vazia():
            raise ValueError("Deque Vazio.")
        return self.sentinela.proximo.elemento

    def consulta_fim(self) -> Any:
        '''Devolve o conteúdo do nó localizado no fim
           do Deque sem removê-lo.
        Exemplos:
        >>> FilaDupla = Deque()
        >>> FilaDupla.consulta_fim()
        Traceback (most recent call last):
            ...
        ValueError: Deque Vazio.
        >>> FilaDupla.insere_inicio(1)
        >>> FilaDupla.insere_inicio(2)
        >>> FilaDupla.insere_inicio(3)
        >>> print(FilaDupla)
        [3, 2, 1]
        >>> FilaDupla.consulta_fim()
        1
        >>> FilaDupla.remove_fim()
        >>> print(FilaDupla)
        [3, 2]
        >>> FilaDupla.consulta_fim()
        2
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        [2]
        >>> FilaDupla.consulta_fim()
        2
        >>> FilaDupla.remove_inicio()
        >>> print(FilaDupla)
        []
        >>> FilaDupla.consulta_fim()
        Traceback (most recent call last):
            ...
        ValueError: Deque Vazio.
        '''
        if self.vazia():
            raise ValueError("Deque Vazio.")
        return self.sentinela.anterior.elemento