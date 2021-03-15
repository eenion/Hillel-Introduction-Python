# Задача 1. Дан файл, в котором через пробел записаны натуральные числа. Вывести на экран суммы всех цифр из файла.

summ = 0
with open('natural_numbers.txt') as f:
    for line in f:
        for i in line:
            if i.isdigit():
                summ += int(i)
print("Задача 1: сумма цифр в файле =", summ)

# Задача 2. Требуется скопировать данные из одного файла в другой, но в обратном порядке.

with open("file_out.txt", "r") as f_out:
    text = f_out.read()
text = text[::-1]
with open("file_in.txt", "w") as f_in:
    f_in.write(text)
print("Задача 2: Данные скопированы в обратном порядке успешно")

# Задача 3. Скопировать из одного файла в другой только определенные символы (например, ряд гласных) и посчитать их общее количество.

# Переносим список неповторяющихся гласных символов и их кол-во: 

with open("filewithtext.txt") as txtfile:
    text_origin = txtfile.read()
text_set = set(text_origin.lower())
original_vowels = set("ауоыиэяюёеіЇєaeiouyäöüǫęóą") # укр, рус, белорус, англ, немец, француз, польский
vowels_in_text = text_set.intersection(original_vowels)
# print(vowels_in_text)
print("Задача 3(кол-во неповторяющихся гласных): ", len(vowels_in_text))
with open("file_with_vowels_only_original.txt", "w") as f1:
    f1.write(str(vowels_in_text))

# Переносим список всех гласных символов и их общее кол-во: 

with open("filewithtext.txt") as txtfile:
    text_general = txtfile.read()
original_vowels = "ауоыиэяюёеіЇєaeiouyäöüǫęóą"
text_general = text_general.lower()
filtered_text = []
general_sum_vowels = 0
for i in text_general:
    if i in original_vowels:
        general_sum_vowels += 1
        filtered_text.append(i)
with open("file_with_vowels_only_general.txt", "w") as f2:
    f2.write(str(filtered_text))
print("Задача 3(Общее кол-во гласных): ", general_sum_vowels)

# Задача 4. Осуществить запись одинаковых данных в типизированные и текстовый файлы. Сравнить размер файлов. 

import os 

pathtxt = 'file.txt'
pathpy = 'file.py'

with open('file.txt', 'w') as ftxt:
    ftxt.write("(,,,)=(^.^)=(,,,)")

with open('file.py', 'w') as fpy:
    fpy.write("(,,,)=(^.^)=(,,,)")

statustxt = os.stat('file.txt') 
statuspy = os.stat('file.py')
sizetxt = statustxt.st_size
sizepy =  statuspy.st_size    

if sizetxt < sizepy:
    print(f"Задача 4: Текстовый файл {pathtxt} меньше по размеру, чем питоновский файл {pathpy}")
elif sizetxt > sizepy:
    print(f"Задача 4: Текстовый файл {pathtxt} больше по размеру, чем питоновский файл {pathpy}")
elif sizetxt == sizepy:
    print(f"Задача 4: Текстовый файл {pathtxt} и питоновский файл {pathpy} имеют одинаковый размер {sizepy} байт.")
