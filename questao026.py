eleitores=int(input('Quantidade de eleitores: '))
cand1=cand2=cand3=0
for i in range(eleitores):
    voto=int(input('Digite em quem quer votar(1, 2, 3): '))
    if voto==1:
        cand1+=1
    if voto==2:
        cand2+=1
    if voto==3:
        cand3+=1
print('Candidato 1:', cand1)
print('Candidato 2:', cand2)
print('Candidato 3:', cand3)