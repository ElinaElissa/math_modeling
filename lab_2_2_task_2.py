a = int(input('введите длину отрезка: '))
b = int(input('введите длину отрезка: '))
c = int(input('введите длину отрезка: '))
if (a + b <= c) or (a + c <= b) or (c + b <= a):
  print('треугольник не существует')
elif (a == c) or (a == b) or (c == b):
  print('равнобедренный')
elif c == a == b:
  print('равносторонний')
elif (a != c) and (a != b) and (c != b):
    print('разносторонний')
else:
  print('треугольник существует')