

# Задача 1. Дано список словарей, создать список кортежей [('red', 'high'), ('yellow', 'low')]

list1 = [{'color': 'red', 'value': 'high'}, {'color': 'yellow', 'value': 'low'}]

aa1 = list1[0]['color']
aa2 = list1[0]['value']
aa3 = list1[1]['color']
aa4 = list1[1]['value']

c1 = (aa1, aa2)
c2 = (aa3, aa4)

list_c1 = [c1, c2]
print('Задача 1: ', list_c1)

# Задача 2. Преобразовать словарь в список кортежей [('a', 1), ('b', 2), ('c', 3)]

a_dictionary = {"a": 1, "b": 2, "c": 3}

list2 = list(a_dictionary.items())  
print('Задача 2: ', list2)

# Задача 3. Создать из списков список кортежей list_c2 = [(1,5), (2,6), (3,7), (4,8)]

list_a = [1, 2, 3, 4]
list_b = [5, 6, 7, 8]

t1 = (list_a[0], list_b[0])
t2 = (list_a[1], list_b[1])
t3 = (list_a[2], list_b[2])
t4 = (list_a[3], list_b[3])

list_c2 = [t1, t2, t3, t4] 
print('Задача 3: ', list_c2)

# Задача 4. Создать кортеж занчений для первих трьох єлементов словоря

dict4 = {1:'entry 1', 2:'entry 2', 3:'entry 3', 4:'entry 4'}

list4 = []
for i in range(1,4):
    list4.append(dict4.get(i))
tuple4 = tuple(list4)
print('Задача 4: ', tuple4)

# топорный способ:
# tuple4 = (dict4.get(1), dict4.get(2), dict4.get(3))

# Задача 5. Создать кортеж из списка

list5 = ["bar", "baz", "qux", "etc"]

tuple5 = tuple(list5)
print('Задача 5: ', tuple5)
