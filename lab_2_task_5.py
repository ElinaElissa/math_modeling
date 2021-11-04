a = int(input('введите целое число делимое: '))
b = int(input('введите целое число делитель: '))
if (b != 0) and (a % b == 0):
  c = a // b
  print('a делится на b')
  print('частное: ', c)
elif (b != 0) and (a % b != 0):
  d = a % b
  c = a // b
  print('a не делится на b')
  print('остаток: ', d)
  print('частное: ', c)
else:
  print('a не делится на b, так как делитель равен 0')

