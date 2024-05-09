#função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

vitorias = int(input("vitorias: "))
derrotas = int(input("derrotas: "))

def rankeadas(vitorias, derrotas):
    resultado = vitorias - derrotas
    return resultado

saldoVitorias  = rankeadas(vitorias, derrotas)

nivel = ""

if(saldoVitorias < 10):
    nivel = "Ferro"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)

elif(11 <saldoVitorias < 20):
    nivel = "Bronze"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)

elif(21 <saldoVitorias < 50):
    nivel = "Prata"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)

elif(51 <saldoVitorias < 80):
    nivel = "Ouro"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)

elif(81 <saldoVitorias < 90):
    nivel = "Diamante"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)

elif(91 <saldoVitorias < 100):
    nivel = "Lendario"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)

elif(saldoVitorias >= 101):
    nivel = "Imortal"
    print(f"O herói tem de saldo {saldoVitorias} e está no nível " + nivel)
