import json


def manual_json_transform(): 
    '''
    Функция сортирует ключи по типам в файле json с применением циклов 
    и сохраняет резуьтат в новом файле.
    '''
    with open('HW.json', 'r') as json_data:
        dicc_d =  json.load(json_data)
        listindict = dicc_d['employee']
    name = listindict[0]['firstName']
    familia = listindict[0]['lastName']
    fio = name + ' ' + familia
    
    name = listindict[1]['firstName']
    familia = listindict[1]['lastName']
    fio1 = name + ' ' + familia

    name = listindict[2]['firstName']
    familia = listindict[2]['lastName']
    fio2 = name + ' ' + familia
    d_el = listindict[0]
    d_el1 = listindict[1]
    d_el2 = listindict[2]

    vvalue_of_dict = {
    'int': [d_el['id'], d_el['age']], 
    'string': [d_el['firstName'], d_el['lastName'], d_el['photo']], 
    'float': [d_el['salary']], 
    'none_type': [d_el['rewards']],
    'bool': [d_el['is_active']]
    }
    vvalue_of_dict1 = {
    'int': [d_el1['id'], d_el1['age']], 
    'string': [d_el1['firstName'], d_el1['lastName']], 
    'float': [d_el1['salary']], 
    'none_type': [d_el1['rewards']],
    'bool': [d_el1['is_active']]
    }
    vvalue_of_dict2 = {
    'int': [d_el2['id']], 
    'string': [d_el2['firstName'], d_el2['lastName'], d_el2['photo']], 
    'float': [d_el2['salary']], 
    'none_type': [d_el2['rewards']],
    'bool': [d_el2['is_active']]
    }

    dict0 = {fio: vvalue_of_dict}
    dict1 = {fio1: vvalue_of_dict1}
    dict2 = {fio2: vvalue_of_dict2}

    new_list =[dict0, dict1, dict2]
    
    dicc_d.update({'employee':new_list})
    
    with open('HW_result.json', 'w') as file:
        json.dump(dicc_d, file)

    return print(f'Файл успешно сохранен.')
        
def main():
    manual_json_transform()

if __name__ == '__main__':
    main()
      


