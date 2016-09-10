# exercicios trabalho 3 reescrito para python
#prof. Habib
#aluno: Genilson
#caucular nota da prova e trabalhos no final mostrar ID do aluno e aprovacao
#estou mandano 2 exercicios desse, depois me explique as diferencas em usar o divisor
# como usar e onde usar
aluno = raw_input("digite o nome ou  a ID do aluno: ")
p1 = input("digite a nota da primeira prova: ")
p2 = input("digite a nota da segunda prova: ")
t1 = input("digite a nota do primeiro trabalho: ")
t2 = input("digite a nota do segundo trabalho: ")
mp = (p1+p2) /2
mt = (t1+t2) /2
mf = (mp* 0.7) + (mt* 0.3) /2
if mf >=7.0:
	print "aluno ID:", aluno, "APROVADO COM MEDIA", mf
else:
	print "aluno ID:", aluno, "reprovado com media", mf 
