# -*- coding: utf-8 -*-
"""lab3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G7tyUSDgiljpA-yhRyFJY-V1GHlLm2mp
"""

a = int(input("Введите число от 1 до 12"))
if a == 1:
  print("Январь")
elif a == 2:
 print("Февраль")
elif a == 3:
  print("Март")
elif a == 4:
  print("Апрель")
elif a == 5:
  print("Май")
elif a == 6:
  print("Июнь")
elif a == 7:
  print("Июль")
elif a == 8:
  print("Август")
elif a == 9:
  print("Сентябрь")
elif a == 10:
  print("Октябрь")
elif a == 11:
  print("Ноябрь")
elif a == 12:
  print("Декабрь")
else:
  print("Вы ввели неправильное число!")

a = int (input("Введите число"))
if (a%2 == 0):
  print("Число чётное")
else:
  print ("Число нечётное")

N = int(input("Введите число"))
if(N > 40):
  print("stonks")
if(N < 40):
  print("not stonks")

def is_year_leap(year):
    year = int(input("Введите год: "))
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False
print (is_year_leap(int(input())))

def is_prime(num):
  if num < 2:
    return False
  if num == 2:
    return True
  if num % 2 == 0:
    return False
    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):
      if num % i ==0:
        return False
  return True

a = float(input())
b = float(input())
if (a / b==3.6) or ((-138 / 2) ** 1.3 <= b <=-69 / 28 ** 5.1* 4):
 a, b = b, a
print(a, b)

a = int(input("Введите число"))
b = int(input("Введите число"))
c = int(input("Введите число"))
d = int(input("Введите число"))
e = int(input("Введите число"))
eq = 0
min = 0
num1 = -256
num2 = 1024

if a % 2 == 0:
  eq += 1
if b % 2 == 0:
  eq += 1
if c % 2 == 0:
  eq += 1
if d % 2 == 0:
  eq += 1
if e % 2 == 0:
  eq += 1

if a < 0 == 0:
  min += 1
if b < 0 == 0:
  min += 1
if c < 0 == 0:
  min += 1
if d < 0 == 0:
  min += 1
if e < 0 == 0:
  min += 1

for i in range(num1,num2 +1):
  if i == a:
    print("Первое число находится в промежутке")
  elif i == b:
      print("Второе число находится в промежутке")
  elif i == c:
    print ("Третье число находится в промежутке")
  elif i == d:
    print("Четвёртое число находится в промежутке")
  elif i == e:
    print("Пятое число находится в промежутке")


if a != b and b != c and c != d and d!=e:
  print("Числа уникальные")
else:
  print("Числа не уникальные")

print("Чётные ", eq)
print("Отрицательные ", min)

a = int(input("Введите число"))
b = int(input("Введите число"))
с = int(input("Введите число"))
d = ((a**2+b**3)/(с+3))/4
round(d)
if round(d) % 2 == 0:
  print("Ответ чётный")
else:
  print("Ответ нечётный")

print(round(d))