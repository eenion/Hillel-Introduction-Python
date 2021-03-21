import json


def loop_json_transform(): 
    '''
    Функция сортирует ключи по типам в файле json с применением циклов 
    и сохраняет резуьтат в новом файле.
    '''
    with open('HW.json', 'r') as json_data:
        dicc_d =  json.load(json_data)
        listindict = dicc_d['employee']

    listindict = dicc_d['employee']

    for i in range(len(listindict)):
        name = listindict[i]['firstName']
        familia = listindict[i]['lastName']
        fio = name + ' ' + familia
        ints = []
        strings = []
        floats = []
        nons = []
        bools = []
        for j in range(len(listindict)):
            my_dict = listindict[j]
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
                vvalue_of_dict1 = {'int': ints[j]}
                # vvalue_of_dict2 = {'string': ints[j]}
                dict1 = {fio: vvalue_of_dict1}
  
     
    dicc_d.update({'employee':dict1})
    
    with open('HW_result.json', 'w') as file:
        json.dump(dicc_d, file)

    
def main():
    loop_json_transform()

if __name__ == '__main__':
    main()
      


