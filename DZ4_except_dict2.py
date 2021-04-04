print("="*15, 'Задача 1', "="*15)

my_numerator = 4+5j
my_denominator = 3423.55
try:
    result = my_numerator/my_denominator
    print('Результат деления чисел:', result)
except TypeError:
    print('Операция деления со строками невозможна')
except ValueError:
    print('Операция деления со строками невозможна')
except ZeroDivisionError: 
    print('Делить на 0 неользя!')



print("="*15, 'Задача 2', "="*15)


cars = [
        {"brand": "ford", "model": "MusTAng Gt500", "year": 2018},
        {"brand": "ZAZ", "model": "Fortza", "year": 2001},
        {"brand": "VW", "model": "Golf GTI", "year": 1999}
]

sorted_cars = sorted(cars, key=lambda x: x["year"])

result_cars_list = []
for any_dict in sorted_cars:
    cap_ze_value_model = any_dict["model"].capitalize()
    any_dict.update({"model": cap_ze_value_model})
    if len(any_dict["model"].split()) > 1:
        mod_value = any_dict["model"].split()[-1]
        uper_mod_value = mod_value.upper()
        any_dict.update({"model": any_dict["model"].split()[0]+" "+uper_mod_value})
    if any_dict["brand"] != any_dict["brand"].upper():
        cap_ze_value_brand = any_dict["brand"].capitalize()
        any_dict.update({"brand": cap_ze_value_brand})
    result_cars_list.append(any_dict)
print('original_car_list: ', cars)
print('      |')
print('      |')
print('      |')
print('      V')
print('result_cars_list: ', result_cars_list)
 