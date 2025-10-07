
#Criar um jogo completo 

class Personagem:
    # construtor
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    # definindo GET
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, nova_vida):
        self.__vida = nova_vida

class Guerreiro:
    def __init__(self, nome, vida, escudo=False):
      super().__init__(nome, vida)
      self.__escudo = escudo
    @property
    def escudo(self):
        return self.__escudo
    
    @escudo.setter
    def escudo(self, escudo):
        self.__escudo = escudo
    
    def atacar(self, personagem):
        return super().atacar(personagem)
   
    #sobreescrevendo o metodo da class pai
    def atacar(self, personagem):
        personagem.vida -= 40
        print(f'{self.nome} atacou {personagem.nome} e causou 40 de dano!')
        print(f'Vida restante de {personagem.nome}: {personagem.vida}')
    
    def protecao(self):
        self.__vida




class Mago:
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def curar(self, personagem):
        personagem.vida += 15
        print(f'{self.__nome} usou o poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')
    
    def atacar(self, personagem):
        def atacar(self, personagem):
         return super().atacar(personagem)
    
    def atacar(self, personagem, arco):
        personagem.vida -= 40
        print(f'{self.nome} atacou {personagem.nome} com magia  e causou 40 de dano!')
        print(f'Vida restante {personagem.nome}: {personagem.vida}')




class Arqueiro:
    def __init__(self, nome, vida, arco=True):
        super().__init__(nome,  vida, arco)
        self.__arco = arco
     
    def atacar(self, personagem):
        return super().atacar(personagem)
    
    def atacar(self, personagem):
        personagem.vida -= 30
        print(f'{self.nome} atacou {personagem.nome} com arco e flecha e causou 30 de dano!')
        print(f'Vida restante {personagem.nome}: {personagem.vida}')

class Invocator:
    def __init__(self, nome, vida, invocações ):
        super().__init__(nome, vida, invocações)
        self.__invocações = invocações
    
    def invocar(lobo):
        Personagem.vida =-30
        print (f'{lobo.invocar}O ataque do lobo tirou 30 pontos do {Personagem.nome}')
        print(f'A vida restante {Personagem.nome}: {Personagem.vida}')
    
    def invocar(leao):
        Personagem.vida -=40
        print(f'{leao.invocar}O ataque do leão tirou 40 pontos do {Personagem.nome}')
        print(f'A vida restante{Personagem.nome}: {Personagem.vida}')

    def invocar(Fênix):
        Personagem.vida -=80
        print(f'{Fênix.invocar} O ataque da fênix tirou 80 pontos do {Personagem.nome}')
        print(f'A vida restante {Personagem.nome}: {Personagem.vida}')

personagem1 = Invocator('Gandalf', 100, 'lobo, leão e fênix')
personagem2= Arqueiro('Legolas', 100, 'arco e flecha')

personagem1.atacar(personagem2)
