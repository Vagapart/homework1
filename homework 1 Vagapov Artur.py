# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# 1 часть ДЗ
А0 = 101

А1 = 100
А1 == А0


lst =  [x for x in range(5, 1000, 5)]

import numpy as np
import pandas as pd


med = np.median(lst)

lst2 =  [x for x in lst if  x > med]
if (5 in lst):
    test1 = "супер тест 1"
    test2 = "тест 2, если 1 в листе"
else:
    test1 = "test 1"
    
# 2 часть ДЗ 

allsecondsUsers = int(input("ведите число секунд: "))  # просим ввести число секунд
hours = allsecondsUsers // 3600 # 3600 секунд в часе
allseconds = allsecondsUsers % 3600 
minutes = allseconds // 60 # 60 секунд в минуте
seconds = allseconds % 60 

print("%d секунд, это %d часов %d минут %d секунд" % (allsecondsUsers, hours, minutes, seconds))

# 3 часть ДЗ 

num = input("Введите число: ")
print(int(num) + int(num+num) + int(num+num+num))


# 4 часть ДЗ 

num = input("Введите число, целое положительное: ")
maxNum = 0
n = 1
while n < len(num):
    if int(num[n]) > maxNum:
        maxNum = int(num[n])
    n = n + 1
print(maxNum)

# 5 часть ДЗ 
margin = int(input("Введите выручку компании: "))
rashod = int(input("Введите расходы компании: "))
if margin > rashod:
    print("Компания отработала с прибылью, рентабельность компании %f" % (margin/rashod))
    colSotrudnikov = int(input("Сколько сотрудников в компании: "))
    print("Прибыль фирмы в расчете на одного сотрудника %f" % (margin/colSotrudnikov))
else:
    print("Компания отработала в убыток")
    
# 6 часть ДЗ
kmStart = int(input("Сколько пробежал спортсмен в первый день: "))
kmFinish = int(input("Сколько должен бегать спортсмен: "))
day = 1 # номер для
while kmStart <= kmFinish:
    kmStart = kmStart*1.1
    day = day +1
print(day)
