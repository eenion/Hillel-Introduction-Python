list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


def filter_to_even_list(some_list):
    filtered_to_even = list(filter(lambda x: x % 2 == 0, some_list))
    
    return filtered_to_even


def filter_to_odd_list(some_list):
    filtered_to_odd = list(filter(lambda x: (x-1) % 2 == 0, some_list))
    
    return filtered_to_odd


def zip_some_lists(list1, list2, list3):    
    ziped_list = list(zip(list1, list2, list3))
        
    return ziped_list


def sum_tuples_in_list(some_list):
    list_with_summed_up_tuples = list(map(sum, some_list))
    
    return list_with_summed_up_tuples


def main():
    print("1. Четные числа первого и второго списка: ", 
          filter_to_even_list(list_1), filter_to_even_list(list_3))
    print("2. Со второго все нечетные: ", filter_to_even_list(list_2)) 
    print("3. Обеденить списки в один список кортежей пар: ", 
          zip_some_lists(list_1, list_2, list_3))
    print("4. По каждому кортежу определить сумму его значений: ", 
          sum_tuples_in_list(zip_some_lists(list_1, list_2, list_3)))
    print("5. После получения списка п.4 оставить в нем только нечетние значения: ",
          filter_to_odd_list(sum_tuples_in_list(zip_some_lists(list_1, list_2, list_3))))




if __name__ == '__main__':
    main()
    