''' Создать текстовый файл (не программно). Построчно
записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести
фамилии этих сотрудников. Выполнить подсчёт средней величины
дохода сотрудников.
Пример файла:

Иванов 23543.12
Петров 13749.32'''

with open('hw5-task3.txt') as my_f:
    if line in my_f < 20000:
        print(line)
    else:
        line += 1
