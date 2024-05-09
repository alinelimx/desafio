nomeHeroi = "Hero"
XP = 50

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
