
# # Задача 1. Проработать встроенние функции множеств.
# print(dir(set))
# my_set = {1, 2, 3, 4, 5, (-4, 5, 3)}
# my_set4 = {1, 2, 3, 4, 5, (-4, 5, 3), 33, 44}
# my_set.clear()
# my_set2 = my_set.copy()
# my_set.add(9)
# my_set3 = my_set.difference(my_set2)
# my_set =  my_set.difference_update(my_set2)
# my_set = my_set4.intersection(my_set2)
# my_set =  my_set4.intersection_update(my_set2)
# my_set.discard((-4, 5, 3))
# my_set.remove(3)
# my_set5 = my_set.union(my_set4)
# my_set.update(my_set4)
# my_set.symmetric_difference_update(my_set4)
# my_set6 = my_set.symmetric_difference(my_set4)
# my_set4.pop()
# my_set.isdisjoint(my_set4)
# my_set.issubset(my_set4)
# my_set.issuperset(my_set4)


# # Задача 2. Одним действием (одной строкой) виполнить intersection єтих множеств

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}

# set_x1 = set1 & set2 & set3
# print("Задача 2. 1-й способ: ", set_x1)

# set_x2 = set1.intersection(set2, set3)
# print("Задача 2. 2-й способ: ", set_x2)

# # Задача 3. Одним действием (одной строкой) виполнить difference єтих множеств

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}

# set_d1 = set1 - set2 - set3
# print("Задача 3. 1-й способ: ", set_d1)

# set_d2 = set1.difference(set2, set3)
# print("Задача 3. 2-й способ: ",  set_d2)

# # Задача 4. Одним действием (одной строкой) виполнить union єтих множеств

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 5, 6}
# set3 = {3, 4, 6, 7}

# set_u1 = set1|set2|set3
# print("Задача 4. 2-й способ: ", set_u1)

# set_u2 = set1.union(set2, set3)
# print("Задача 4. 2-й способ: ", set_u2)

# # Задача 5. Добавить список элементов к заданному набору

# sampleSet = {"Yellow", "Orange", "Black"}
# sampleList = ["Blue", "Green", "Red"]

# sampleSet = sampleSet.union(set(sampleList))
# print("Задача 5: ", sampleSet)

# # Задача 6. Вернуть новый набор идентичных предметов из заданных двух наборов

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.intersection(set2)
# print("Задача 6: ", set3)

# # Задача 7. Возвращает новый набор со всеми элементами из обоих наборов, удаляя дубликаты.

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.union(set2)
# print("Задача 7: ", set3)

# # Задача 8. Учитывая два набора Python, обновите первый набор элементами, которые существуют только в первом наборе, но не во втором наборе.

# set1 = {10, 20, 30}
# set2 = {20, 40, 50}

# set3 = set1.difference(set2)
# print("Задача 8: ", set3)

# # Задача 9. Удалите єлементи 10, 20, 30 из следующего набора

# set1 = {10, 20, 30, 40, 50}

# set1.remove(10)
# set1.remove(20)
# set1.remove(30)
# print("Задача 9: ", set1)

# # Задача 10. Вернуть набор всех элементов в A или B, но не в обоих

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# set1.symmetric_difference_update(set2)
# print("Задача 10: ", set1)

# # Задача 11. Проверьте, есть ли в двух наборах какие-либо общие элементы. Если да, отобразите общие элементы.

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# set3 = set1.intersection(set2)
# print("Задача 11: ", set3)

# # Задача 12. Обновите набор 1, добавив элементы из набора 2

# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 70, 80, 90, 10}

# set1.update(set2)
# print("Задача 12: ", set1)

# # Задача 13. Удалите элементы из set1, которые не являются общими для set1 и set2

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# set3 = set1.intersection(set2)
# print("Задача 13: ", set3)

# # Задача 14. Используя Все полученние знания по всем типам данних виполнить рефакторинг кода задачи с сложним списком из лекции 4. Код уменьшить до минимального количества строк
