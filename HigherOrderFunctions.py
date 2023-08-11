# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

def count_vowels(word):
    vowels = 'аеёиоуыэюя'
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count
def check_rhythm(poem):
    words = poem.split(" ") 
    syllables = []
    for word in words:
        syl = word.split("-")
        phrase_syllables = []
        for word in syl:
            syllable_count = count_vowels(word)
            phrase_syllables.append(syllable_count)
        syllables.append(phrase_syllables)
    for i in range(1, len(syllables)):
        if syllables[i] != syllables[i-1]:
            return "Пам парам"
    return "Парам пам-пам"
poem = input ("Введите стихотворение: ")
result = check_rhythm(poem)
print (result)