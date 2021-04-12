import json


class JsonSorter():
    link_to_json = 'HW.json' 
    save_to_file = 'HW_result.json'

    def open_json_and_make_dict(self, link_to_json = 'HW.json'):
        self.link_to_json = link_to_json
        with open(link_to_json, 'r') as json_data:
            dicc_d =  json.load(json_data)
        print(f'Файл {link_to_json} загружен.')
        return dicc_d
        
    def dict_sort_by_type(self, dicc_d): 
        self.dicc_d = dicc_d
        '''
        Функция сортирует ключи по типам в файле json с применением циклов.
        '''
            
        employee = dicc_d['employee']
        my_dict4 = {}
        for person in employee:
            first_name = person.get('firstName')
            last_name = person.get('lastName')
            fio = f"{first_name} {last_name}"
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
        
    def save_sorted_dict(self, dicc_d, save_to_file = 'HW_result.json'):
        self.dicc_d = dicc_d
        with open(save_to_file, 'w') as file:
            json.dump(dicc_d, file)
        return print(f'Файл {save_to_file} успешно сохранен.')


sorter = JsonSorter()

print("Используем пути файлов по дефолту:")
sorter.save_sorted_dict(sorter.dict_sort_by_type(sorter.open_json_and_make_dict()))

print("-"*40)

print("Вводим альтарнативные пути файлов:")
sorter.save_sorted_dict(sorter.dict_sort_by_type(
    sorter.open_json_and_make_dict('HW_alternative.json')), 
    'HW_result__alternative.json')