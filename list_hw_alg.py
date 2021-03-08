my_list = [
    [1, None, 2, 3, 4 + 5j, 6],
    [1.0, 2.5, None, 3, 9, 4.0 + 5.2j, 6.1],
    ['1', '2', '3.6', None, '4+5.7j', '6']
] # объявляем список my_list, которому присваиваем значение: список из трех списков


int_list = [] # объявляем пустой список int_list в который будем перемещать целые числа 
float_list = [] # объявляем пустой список  float_list в который будем перемещать дробные числа
str_list = [] # объявляем пустой список str_list в который будем перемещать строки
for item in my_list: # передаем список my_list в цикл и итерируемся по нему (перебираем каждый элемент item)
    types = [] # объявляем пустой список types (забегая наперед - для перемещения в него названия типов каждого элемента)
    for elem in item: # передаем список  item в цикл и итерируемся по нему
        el_type = type(elem) # объявляем переменную el_type и присваеваем ей название типа для каждого элемента подсписка item
        types.append(el_type.__name__) # при каждой итерации в список types добавляем переменную el_type из которой берем только имя типа
    single_types = [] # объявляем пустой список single_types
    for i_type in types: # передаем список types в цикл и итерируемся по нему
        if i_type not in single_types: # задаем условие, что если  элемент i_type отсутствует в списке single_types, то выполнить действие в 19 строке
            single_types.append(i_type) # добавляем в список single_types поочередно элемент  i_type (если выполняется условие в строке 18)
    types_count = [] # объявляем пустой список types_count (забегая наперед - для перемещения в него количество типов эелементов)
    for element_type in single_types: # передаем список single_types в цикл и итерируемся по нему 
        type_count = types.count(element_type) # объявляем переменную type_count в которой подсчитываем количесвто каждого типа данных среди элементов из списка types
        types_count.append(type_count) # добавляем в список types_count поочередно количество каждого типа данных
    max_types_count = max(types_count) # объявляем переменную max_types_count, которая является элементом с  максимальным значением из списка types_count 
    index_max = types_count.index(max(types_count)) # объявляем переменную index_max, которой присваиваем индекс максимального значения элемента списка types_count
    main_type = single_types[index_max] # объявляем переменную  main_type, которой присваиваем значение элемента списка single_types, индекс которого соответствует максимальному значению 
    separated_list = [] # объявляем пустой список separated_list 
    for element in item: # передаем список item в цикл и итерируемся по нему
        if type(element).__name__ == main_type: # задаем условие, если имя типа элемента равно имени переменной main_type
            separated_list.append(element) # тогда добавляем этот элемент в список separated_list

    int_list.extend(separated_list) # добавляем в список int_list отфильтрованный список separated_list
    float_list.extend(separated_list) # добавляем в список float_list отфильтрованный список separated_list
    str_list.extend(separated_list) # добавляем в список str_list отфильтрованный список separated_list

res_int_list = [] # объявляем пустой список res_int_list
for i in int_list: # передаем список int_list в цикл и итерируемся по нему
    if type(i).__name__ == 'int': # если название типа каждого элемента списка int_list совпадает с строкой 'int'
        res_int_list.append(i) # тогда добавляем этот элемент в список res_int_list
print('res_int_list: ', res_int_list) # выводим на экран список res_int_list с сопроводительным пояснением в виде строки 'res_int_list: '

res_float_list = [] # объявляем пустой список res_float_list
for i in float_list: # передаем список float_list в цикл и итерируемся по нему
    if type(i).__name__ == 'float': # если название типа каждого элемента списка float_list совпадает с строкой 'float'
        res_float_list.append(i) # тогда добавляем этот элемент в список res_float_list
print('res_float_list: ', res_float_list) # выводим на экран список res_float_list с сопроводительным пояснением в виде строки 'res_float_list: '

res_str_list = [str(i) for i in str_list] # применяем генератор спика с логикой: каждый элемент списка str_list перевести в строку и добавить в список res_str_list
print('res_str_list: ', res_str_list) # выводим на экран список res_str_list с сопроводительным пояснением в виде строки 'res_str_list: '
