from abc import ABC, abstractmethod

class AbstractRobot(ABC):
    """Classe abstrata para real e test robots"""

    @abstractmethod
    def posicao_00(self):
        ...

    @abstractmethod
    def posicao_01(self):
        ...

    @abstractmethod
    def posicao_02(self):
        ...
    
    @abstractmethod
    def posicao_10(self):
        ...
    
    @abstractmethod
    def posicao_11(self):
        ...

    @abstractmethod
    def posicao_12(self):
        ...

    @abstractmethod
    def posicao_20(self):
        ...
    
    @abstractmethod
    def posicao_21(self):
        ...

    @abstractmethod
    def posicao_22(self):
        ...

    @abstractmethod
    def conectar(self):
        ...

    @abstractmethod
    def desconectar(self):
        ...
    
    @abstractmethod
    def pegar_ficha(self):
        ...
    
    @abstractmethod
    def soltar_ficha(self):
        ...
        
    @abstractmethod
    def voltar_base(self):
        ...

    @abstractmethod
    def intermediaria_rampa(self):
        ...

    @abstractmethod
    def intermediaria_tabuleiro(self):
        ...
    
    @abstractmethod
    def pos_pegar(self):
        ...

    @abstractmethod
    def jogada_robo(self,jogada_robo_linha,jogada_robo_coluna):
        ...
