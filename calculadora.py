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
