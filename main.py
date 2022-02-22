import time
import random
answer = ['yes','Yes','no','No']
win = 0
player = input('Введите имя пользователя: ')
num = int(input("Введите число от 1 до 10: "))
v = random.randint(1,10)
while num >= 11 or num < 1:
 num = int(input('Число не подходит,введи число от 1 до 10'))
while num != v:
 time.sleep(0.7)
 print(".")
 time.sleep(0.7)
 print(".")
 time.sleep(0.7)
 print(".")
 print("Не угадал,попробуй еще раз")
 num = int(input(""))
if num == v:
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  time.sleep(1)
  print(".")
  print("Поздравляю!,ты угадал")
  win += 1
  print('Поздравляю вы выиграли :',win,' раз')
  continuation = input('Хотите сыграть еще раз? ')
  while continuation == answer[0] or continuation == answer[1]:
     num = int(input("Введите число от 1 до 10: "))
     while num != v:
         time.sleep(0.7)
         print(".")
         time.sleep(0.7)
         print(".")
         time.sleep(0.7)
         print(".")
         print("Не угадал,попробуй еще раз")
         num = int(input(""))
         if num == v:
              time.sleep(1)
              print(".")
              time.sleep(1)
              print(".")
              time.sleep(1)
              print(".")
              print("Поздравляю!,ты угадал")
              win += 1
              print('Поздравляю вы выиграли :',win,' раз')
              continuation = input( 'Хотите сыграть еще раз? ')
if continuation == answer[2] or continuation == answer[3]:
    print('Спасибо за игру',player)
