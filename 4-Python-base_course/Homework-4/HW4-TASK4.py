'''Представлен список чисел. Определите элементы списка,
не имеющие повторений. Сформируйте итоговый массив чисел,
соответствующих требованию. Элементы выведите в порядке
их следования в исходном списке. Для выполнения задания
обязательно используйте генератор.
Пример исходного списка:
[2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]'''

# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# my_solve = {el for el in my_list if el//el == 1}
# '''при написании уравнения el//el != 1 в выводе
# пишет set(), при el//el == 1 в выводе пишет
# {1, 2, 3, 4, 7, 10, 11, 44, 23}'''
# my_solve = {el for el in my_list if el%el == 1}
# '''в выводе пишет set()'''
# print(my_solve)


my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_solve = {i for i in my_list if i%i == 1}
print(my_solve)
print(type(my_solve))
