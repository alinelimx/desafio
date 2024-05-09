#Escrevendo as classes de um Jogo

#**O Que deve ser utilizado** Variáveis, Operadores, Laços de repetição, Estruturas de decisões, Funções, Classes e Objetos

## Objetivo:

#Crie uma classe generica que represente um herói de uma aventura e que possua as seguintes propriedades: nome, idade, tipo (ex: guerreiro, mago, monge, ninja )

#além disso, deve ter um método chamado atacar que deve atender os seguientes requisitos:
#- exibir a mensagem: "o {tipo} atacou usando {ataque}")
#- aonde o {tipo} deve ser concatenando o tipo que está na propriedade da classe
#- e no {ataque} deve seguir uma descrição diferente conforme o tipo, seguindo a tabela abaixo:

#se mago -> no ataque exibir (usou magia)
#se guerreiro -> no ataque exibir (usou espada)
#se monge -> no ataque exibir (usou artes marciais)
#se ninja -> no ataque exibir (usou shuriken)

## Saída
#Ao final deve se exibir uma mensagem:
#- "o {tipo} atacou usando {ataque}"
  #ex: mago atacou usando magia
  #guerreiro atacou usando espada

class Hero:
    #construtor
    def __init__ (self, nome, idade, tipo):
        #self é usado para referenciar a própria instância da classe dentro dos métodos da classe em Python.
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if (self.tipo == 'mago'):
            ataque = 'magia'
        elif (self.tipo == 'guerreiro'):
            ataque = 'espada'
        elif (self.tipo == 'monge'):
            ataque = 'artes marciais'
        elif (self.tipo == 'ninja'):
            ataque = 'shuriken'
        else:
            ataque = 'ataque desconhecido'
        print(f"O {self.tipo} atacou usando {ataque}")

# Capturando inputs do usuário
nome = input("Digite o nome do herói: ")
idade = int(input("Digite a idade do herói: "))
tipo = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ")

# Criando o objeto Heroi com os inputs do usuário
heroi = Hero(nome, idade, tipo)
heroi.atacar()