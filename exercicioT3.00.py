#exercicios trabalho 3 reescrito para python
#prof. Habib
#aluno: Genilson
#calcular nota da prova e trabalhos no final mostrar ID do aluno e aprovacao

# qual melhor metodo para criar o programa? percebi que usando n/100 o python so interpreta como real 
#se digitar a nota e forma de real... outro metodo parece ser melhor... se puder me explicar depois..

aluno = raw_input("digite o nome ou  a ID do aluno: ")
p1 = input("digite a nota da primeira prova: ")
p2 = input("digite a nota da segunda prova: ")
t1 = input("digite a nota do primeiro trabalho: ")
t2 = input("digite a nota do segundo trabalho: ")
mp = (p1 + p2) /2
mt = (t1 + t2) /2
mf = (mp * 70/100) + (mt * 30/100)

if mf >=(70/100):
	print "aluno ID:", aluno, "APROVADO COM MEDIA", float, mf
else:
	print "aluno ID:", aluno, "reprovado com media", float, mf 
