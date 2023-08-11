# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# def count_vowels(word):
#     vowels = 'аеёиоуыэюя'
#     count = 0
#     for letter in word:
#         if letter.lower() in vowels:
#             count += 1
#     return count
# def check_rhythm(poem):
#     words = poem.split(" ") 
#     syllables = []
#     for word in words:
#         syl = word.split("-")
#         phrase_syllables = []
#         for word in syl:
#             syllable_count = count_vowels(word)
#             phrase_syllables.append(syllable_count)
#         syllables.append(phrase_syllables)
#     for i in range(1, len(syllables)):
#         if syllables[i] != syllables[i-1]:
#             return "Пам парам"
#     return "Парам пам-пам"
# poem = input ("Введите стихотворение: ")
# result = check_rhythm(poem)
# print (result)


# Задача 36: Напишите функцию вывода таблицы умножения print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

num_rows = int(input('Введите число строк: '))
num_columns = int(input('Введите число столбцов: '))
def printOperationTable(operation, num_rows, num_columns):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            print(operation(row, column), end='\t')
        print()
printOperationTable(lambda x,y: x*y, num_rows, num_columns)