##10 voltas para cada 6 corredores v
##Ler os nomes e os tempos(s) v
##Guardar informações em uma matriz v

##a) Qual foi a melhor volta, e quem a fez
##b) Classificação geral(Em ordem decressente)
##c) A volta com a média mais rápida


pilotos = []

##Dever ter 6, caso menos, teste
for p in range(2): ##Laço para definição dos corredores
    corredor = []
    nome = input(f"Digite o nome do {p+1}º corredor ")
    corredor.append(nome)
    tempos = []
    ##Deve ter 10, caso menos, teste
    for v in range(3): #For para a definição dos tempos
        tempo = int(input(f"Digite o tempo do {p+1}º corredor, em segundos, da {v+1} volta "))
        tempos.append(tempo)
    corredor.append(tempos)
    pilotos.append(corredor)


melhorVolta = 0
melhorCorredor = 'a'


for mv in pilotos: ##For para varrer o array pilotos
    for t in range(6):
        if pilotos[mv][t] < melhorVolta:
            melhorVolta = pilotos[mv][t]
            melhorCorredor = pilotos[0]



print(melhorCorredor)
print(melhorVolta)