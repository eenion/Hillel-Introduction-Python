import json

def open_json_and_make_dict(link_to_json):
    with open(link_to_json, 'r') as json_data:
        dicc_d =  json.load(json_data)
    print('Файл загружен.')
    return dicc_d
    
def dict_sort_by_type(dicc_d): 
    '''
    Функция сортирует ключи по типам в файле json с применением циклов.
    '''
          
    employee = dicc_d['employee']
    my_dict4 = {}
    for person in employee:
        first_name = person.get('firstName')
        last_name = person.get('lastName')
        fio = f"{first_name} + ' ' + {last_name}"
        ints = []
        strings = []
        floats = []
        nons = []
        bools = []
        for pers_key, pers_value in person.items():
            if type(pers_value) == int:
                ints.append(pers_value)
            elif type(pers_value) == str:
                strings.append(pers_value)
            elif type(pers_value) == float:
                floats.append(pers_value)
            elif type(pers_value) == None:
                nons.append(pers_value)
            elif type(pers_value) == bool:
                bools.append(pers_value)
        
        my_dict2 = {'int':ints, 'string':strings, 'float':floats, 'None':nons, 'bool':bools}
        my_dict3 = {fio : my_dict2}
        my_dict4.update(my_dict3)
        
    dicc_d.update({'employee':my_dict4})

    print('Словарь отсортирован по типам.')
    return dicc_d
    
def save_sorted_dict(dicc_d):
    with open('HW_result.json', 'w') as file:
        json.dump(dicc_d, file)
    return print('Файл успешно сохранен.')

def main():
    save_sorted_dict(dict_sort_by_type(open_json_and_make_dict('HW.json')))

if __name__ == '__main__':
    main()
      


