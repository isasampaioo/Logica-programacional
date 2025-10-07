# atributos - carcteristicas do objeto
# metodos - açõess que o objeto pode fazer

# nome e vida - atacar
# self - quando quero me referir a algum atributo de classe 
# construtor - quando quero criar um novo objeto, chamo o construtor para acesar os atributos

import random
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

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
        self.__vida = max(0, nova_vida)  # Vida nunca negativa

    def atacar(self, personagem):
        if personagem.vida > 0:
            personagem.vida -= 20
            print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida, agora está com --{personagem.vida}--')
        else:
            print(f'{personagem.nome} já está fora do jogo!')

class Especiais:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self, personagem):
        if personagem.vida > 0:
            personagem.vida -= 30
            print(f'{self.nome} (Especial) atacou {personagem.nome} e tirou 30 pontos de vida, agora está com --{personagem.vida}--')
        else:
            print(f'{personagem.nome} já está fora do jogo!')

print(30*'-', 'JOGO', 30*'-')
print()

personagens = [
    Personagem('Piu piu', 100),
    Personagem('Frajola', 100),
    Personagem('Pernalonga', 100),
    Personagem('Hortelino', 100)
]

especiais = [
    Especiais('Diabo da tasmania'),
    Especiais('Lola'),
    Especiais('Eufrazio')
]

for p in personagens:
    print(f'Personagem: {p.nome}')
    print(f'Vida: {p.vida}')
    print()

for e in especiais:
    print(f'Personagem Especial: {e.nome}')
print()

todos = personagens + especiais
vivos = personagens.copy()

print(30*'-', 'ATAQUES', 30*'-')

while True:
    vivos = [p for p in personagens if p.vida > 0]
    if not vivos:
        print("Todos os personagens perderam!")
        break
    atacante = random.choice(todos)
    alvo = random.choice(vivos)
    if atacante == alvo:
        continue
    atacante.atacar(alvo)
    if alvo.vida == 0:
        print()
        print(f'----{alvo.nome} perdeu o jogo!---')
        break
print()
