# Desafio Classificador de nível de Herói

#**O Que deve ser utilizado** Variáveis, Operadores, Laços de repetição, Estruturas de decisões

## Objetivo
#Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 5.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

## Saída
#Ao final deve se exibir uma mensagem:
#"O Herói de nome **{nome}** está no nível de **{nivel}**"

nomeHeroi = input("nome do heroi: ")
XP = int(input("XP: "))

for i in range(7):
    if XP < 1000:
        nivel = "Ferro"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 1000
    elif XP > 1001 and XP < 2000:
        nivel = "Bronze"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 1000
    elif XP > 2001 and XP < 5000:
        nivel = "Prata"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 3000
    elif XP > 5001 and XP < 7000:
        nivel = "Ouro"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 2000
    elif XP > 7001 and XP < 8000:
        nivel = "Platina"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 1000
    elif XP > 8001 and XP < 9000:
        nivel = "Ascendente"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 1000
    elif XP > 9001 and XP < 10000:
        nivel = "Imortal"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)
        XP += 1000
    elif XP >= 10001:
        nivel = "Radiante"
        print("O Herói de nome", nomeHeroi, "está no nível de", nivel)

