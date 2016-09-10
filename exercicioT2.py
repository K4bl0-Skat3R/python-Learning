#exercicios trabalho 3 reescrito para python
#prof. Habib
#aluno: Genilson
#programa le tres numero e determina se [e ou nao um triangulo e printa qual seu tipo
# PS: o exercico pede apenas para dizer se e um triangulo isosceles
# professor pra nao me esquecer do raw_input vou usar nesse
#exercicio pelo visto nas versoes 3.xx novas do python "input" e a mesma coisa
#o raw_iput pode ser armazenado qlqer coisa (letrs e numros) ja o input apenas numeros
# me corrija na sala

#TRIANGULOS
print "digite abaixo os lados de um triangulo qualquer \n"
a = float (raw_input("Lado A: "))
b = float (raw_input("Lado B: "))
c = float (raw_input("lado C: "))
if a + b > c:
	if a<=0 or b<=0 or c<=0: 
		print "Valor invalido em um dos lados"
	elif a == b and a == c:
		print "Triangulo equilatero"
	elif a == b or b == c or a == c:
		print "Triangulo Isosceles"
	elif (a != b and c) or (b!= a and c) or a != c:
		print "Triangulo escaleno"
	elif a**2 == b**2+c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
		print "Triangulo retangulo"
else:
	print "nao e um triangulo"
