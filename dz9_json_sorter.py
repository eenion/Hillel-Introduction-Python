import json

def json_transform(): 
    '''
    Функция сортирует ключи по типам в файле json с применением циклов 
    и сохраняет результат в новом файле.
    '''
    with open('HW.json', 'r') as json_data:
        dicc_d =  json.load(json_data)
        listindict = dicc_d['employee']

    listindict = dicc_d['employee']
    my_dict4 = {}
    for i in range(len(listindict)):
        name = listindict[i]['firstName']
        familia = listindict[i]['lastName']
        fio = name + ' ' + familia
        ints = []
        strings = []
        floats = []
        nons = []
        bools = []
        my_dict = listindict[i]
        for key in my_dict:
            if type(my_dict[key]) == int:
                ints.append(my_dict[key])
            elif type(my_dict[key]) == str:
                strings.append(my_dict[key])
            elif type(my_dict[key]) == float:
                floats.append(my_dict[key])
            elif type(my_dict[key]) == None:
                nons.append(my_dict[key])
            elif type(my_dict[key]) == bool:
                bools.append(my_dict[key])
        
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
      


