number = int(raw_input('Digite um numero inteiro: '))
count = 0
 
for num in range(number, 0, -1):
  if number % num == 0:
    count = count + 1
 
if count == 2:
  print 'numero', number, 'eh primo.'
else:
  print 'numero', number, 'nao eh primo'
