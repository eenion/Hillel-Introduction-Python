import json

def json_transform(): 
    '''
    Функция сортирует ключи по типам в файле json с применением циклов 
    и сохраняет результат в новом файле.
    '''
    with open('HW.json', 'r') as json_data:
        dicc_d =  json.load(json_data)
        
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
    
    with open('HW_result.json', 'w') as file:
        json.dump(dicc_d, file)

    return print('Файл успешно сохранен.')

def main():
    json_transform()

if __name__ == '__main__':
    main()
      


