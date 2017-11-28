#exercicios trabalho 3  
#prof. Habib
#aluno: Genilson
#programa recebe 3 valores independent da ordem dos numeros maior ou menor,
# ..o progragrama devolvera os valores em ordem crescente.


print "informe abaixo  tres sequencias numericas"
x = input("...digite o primeiro numero: ")
y = input("...digite o segundo numero: ")
z = input("...digite o terceiro numero: ")
if x <= y <= z:
	print "a ordem crescente e:", x, y, z
	print "X VALE", x
	print "y VALE", y
	print "z VALE", z
elif x <= z <= y:
	print "a ordem crescente e:", x, z, y
	print "X VALE", x
	print "y VALE", z
	print "z VALE", y
elif y <= x <= z:
	print "a ordem crescente e:", y, x, z
	print "X VALE", y
	print "y VALE", x
	print "z VALE", z
elif y <= z <= x:
	print "a ordem crescente e:", y, z, x
	print "X VALE", y
	print "y VALE", z
	print "z VALE", x
elif z <= x <= y:
	print "a ordem crescente e:", z, x, y
	print "X VALE", z
	print "y VALE", x
	print "z VALE", y
elif z <= y <= x:
	print "a ordem crescente dos numeros e:", z, y, x
	print "X VALE", z
	print "y VALE", y
	print "z VALE", x  
