print('квадратное уравнение (a * x ** 2 + b * x + c = 0):')
a = int(input('1 коэффициент: '))
b = int(input('2 коэффициент: '))
c = int(input('3 коэффициент: '))

d = b ** 2 - 4 * a * c
print(d)
if d > 0:
  x1 = (-b + (d ** 0.5)) / 2 * a
  x2 = (-b - (d ** 0.5)) / 2 * a
  print('первый корень = ', x1)
  print('второй корень = ', x2)
elif d == 0:
  x = -b / 2 *a
  print('корень = ', x)
else:
  print('нет корней')