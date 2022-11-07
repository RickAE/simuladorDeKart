##10 voltas para cada 6 corredores v
##Ler os nomes e os tempos(s) v
##Guardar informações em uma matriz v

##a) Qual foi a melhor volta, e quem a fez v
##b) Classificação geral(Em ordem decressente)
##c) A volta com a média mais rápida


pilotos = []
menorTempo = 100
melhorVolta = 100
melhorCorredor = ''


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
        somaTempos = 0

        if tempo < menorTempo:
            menorTempo = tempo
            melhorCorredor = nome
            melhorVolta = v+1

        somaTempos += tempo

    corredor.append(tempos)
    pilotos.append(corredor)


print(melhorCorredor)
print(melhorVolta)

print(f'A melhor volta foi a {melhorVolta}ª do corredor {melhorCorredor}, ele demorou {menorTempo}s para completara')