print("="*15, 'Задача 1', "="*15)

my_numerator = 4+5j
my_denominator = 3423.55
try:
    result = my_numerator/my_denominator
    print('Результат деления чисел: ', result)
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

print(sorted(cars, key=lambda x: x["year"])) # Отсортировать авто по дате.

cars2 = [dic_item["model"].capitalize() for dic_item in cars]

print(cars2) # Название модели должно бить в формате title.



# Название бренда допускаеться или в формате title или uppercase (преобразовать где надо).
# тут нужно как-то применить метод .islower() и потом .capitalize()

# Название модификации модели (втрое слово) только в uppercase.
