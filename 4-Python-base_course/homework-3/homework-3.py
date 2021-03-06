# TASK1
'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
 деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления
 на ноль.'''

def my_num(a, b):
    try:
        answer = a/b
        return answer
    except ZeroDivisionError:
        return 'b cannot be zero'
print(my_num(float(input('enter num1: ')), float(input('enter num2: '))))

# TASK2
'''  Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Осуществить вывод данных
о пользователе одной строкой.'''

def my_func():
    first_name = str(input("назовите себя: "))
    second_name = str(input("и фамилию тоже: "))
    year_of_birth = int(input("введите год рождения: "))
    sity = str(input("в каком городе живёте: "))
    email = str(input("ваше мыло: "))
    phone = int(input("ваш телеофон: "))
    return first_name, second_name, year_of_birth, sity, email, phone


first_name_, second_name_, year_of_birth_, sity_, email_, phone_ = my_func()
print(f'вас зовут - {first_name_} с фамилией - {second_name_} года рождения {year_of_birth_} из города {sity_}, с емейлом {email_} и телефоном {phone_}')

# TASK3
'''Реализовать функцию my_func(), которая принимает
три позиционных аргумента и возвращает сумму наибольших
двух аргументов.'''

def my_func():
    lst = list(input(''.split()))
    maximum = lst.pop()
    maximum2 = lst.pop()
    for i in lst:
        if i > maximum:
            maximum2 = maximum
            maximum = i
        elif i > maximum2:
            maximum2 = i
print(my_func())
print(my_func())
print((max(my_func()+((max-1)(my_func())))))
'''Здесь решение так и не смог докрутить. Где-то
запутался в методах. Ниже правильное решение'''

'''Всё что приходит надо перевести в лист.
Затем метод .pop удаляет указанный индекс:
    - в листе метод .index ищет минимальное значение
    - найденный индекс элемента удаляется методом .pop
return возвращает сумму

def my_func(num_1, nim_2, num_3):
    try:
        my_list = [num_1, nim_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'


print(my_func(1, 2, 3))'''

# TASK4
'''Программа принимает действительное положительное число x
и целое отрицательное число y. Выполните возведение числа x
в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции
возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый —
возведение в степень с помощью оператора **. Второй — более
сложная реализация без оператора **, предусматривающая
использование цикла.'''

1 variant
def my_func():
    x = float(input('введите полож. число: '))
    y = abs(int(input('введите отрицательное число: ')))
    answer = x ** y
    return int(answer)
print(my_func())


# 2 variant
def my_func(x, y):
    x = float(input('введите полож. число: '))
    y = abs(int(input('введите отрицательное число: ')))
    answer = x
    for i in range(y-1):
        answer *= x
    return answer
print(my_func(0, 0))

# TASK5
'''Программа запрашивает у пользователя строку чисел,
разделённых пробелом. При нажатии Enter должна
выводиться сумма чисел. Пользователь может продолжить
ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже
подсчитанной сумме. Но если вместо числа вводится
специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной
ранее сумме и после этого завершить программу.'''

def my_sum(my_str):
    my_str = str(input('введите набор чисел через пробел: ').split())
    my_int = int(my_str)
    return my_int
print(my_sum(my_str))

str_lst = str(input('введите набор чисел через пробел: '))
print(str_lst)
int_lst = [int(x) for x in str_lst.replace('','')]
print (int_lst)

# TASK6
'''Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую
 его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную
ранее функцию int_func().'''

def int_func():
    my_input = str(input('введите слово латиницей: '))
    return my_input.title()
print(int_func())

