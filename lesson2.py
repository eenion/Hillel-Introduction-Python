print('Hello World')
print('')
print('')
# # =============================================
# Соблюдение РЕР8. Неправильные отступы
print('Hello World')
if 1==1:
    print('Привіт Світ ;)')
print('')
print('')
# =============================================
# Зарезервированные слова. Служебные слова!
# int = 100000
# print('int: ', int)
# этот пример я оставляю закомментированным, поскольку падает ошибка и дальше код не запускается!
string_number = '233330000000000000000000000000003123'
print(int(string_number))
# # Исправление
my_int = 5066
print('my_int =', my_int)
string_number = '0000000000000000000000'
nsrt = int(string_number)
print('nsrt:', nsrt)
print('Тип переменной nsrt теперь:', type(nsrt))

# # =============================================
# # Определение типа переменной. Функция type()
print(type(my_int))
print('')
print('')
# # =============================================
# # Определение типов (int, float, str)

my_int = 990
print('============= Определение типов (int, float, str)===================')
print('my_int:', my_int)
print('type(my_int):', type(my_int))
print('====================================================================')
my_float = 990.990
print('my_float:', my_float)
print('type(my_float):', type(my_float))
print('====================================================================')
my_str = '990990990'
print('my_str:', my_str)
print('type(my_str):', type(my_str))
print('')
print('')
# # =============================================
# # Введение значений переменных с клавиатуры
print('========== Введение значений переменных с клавиатуры ===============')

my_value = input('Введите любое целое число:')
print('Вы ввели:', my_value)
print('Тип данных:', type(my_value))
print('')
# # функция input всегда возвращает строку

my_value = my_value*2
print('Результатом умножения строки на 2  является:', my_value)
print('Что б убедится в этом, посмотрим какой тип введенных6 данных:', type(my_value))
print('')
print('')
# =============================================
# # Приведение типа переменной

my_value = int(my_value)
print('Теперь введенные данные принимают новое значение(задвоенное) и меняют тип на int:', my_value)
print('Поэтому умножение на 2 математическое, результат:', my_value*2)
print('type(my_value):', type(my_value))
print('')
print('')
my_str = '133333310'
print('my_str:', my_str)
print('type(my_str):', type(my_str))
my_int = int(my_str)
print('my_int:', my_int)
print('type(my_int):', type(my_int))

my_str = '100377777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777769'
print('int(my_str):', int(my_str))
print('float(my_str):', float(my_str))
print('')

my_int = 13330
my_float = float(my_int)
print('my_float:', my_float)
print(my_float)
print('')

my_float = 10.035533545
print('int откидывает у данных float все что после запятой.', 'Было', my_float, 'cтало:', int(my_float))
print('')

my_float = 14440.8255252345
print('int(my_float):', int(my_float))
my_float = -14440.8255252345
print('int(my_float):', int(my_float))
print('')

# # приведение типа не математическое округление, а просто отбрасывание десятичной стороны

my_float = 120.72
my_str = str(my_float)
print('my_str:', my_str)
print('type(my_str):', type(my_str))
print('')

my_int = 13330
my_str = str(my_int)
print('my_str:', my_str)
print('type(my_str):', type(my_str))
print('')

my_str = '4444' # ten не могу оставить, код ниже падает
print('int(my_str):', int(my_str))
my_float = 1055555550.
print('my_float:', my_float)
print('type(my_float):', type(my_float))
print('')
print('')

# # =============================================
# # Булеый тип данных
my_bool = True
print('my_bool:', my_bool)
print('type(my_bool):', type(my_bool))
print('')

my_bool = 'a'=='a'
print('my_bool:', my_bool)
print('type(my_bool):', type(my_bool))
print('')

my_bool = 4!=4
print('my_bool:', my_bool)
print('type(my_bool):', type(my_bool))
print('')

my_bool = 675==567
print('my_bool:', my_bool)
print('type(my_bool):', type(my_bool))
print('')

my_bool = 4!=6
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print('')

my_bool = 6>6
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print('')

my_bool = 999>=999
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print('')

my_bool = 2352352435345>=1
print('my_bool: ', my_bool)
print('type(my_bool): ', type(my_bool))
print('')

my_bool = 214>=215
print('my_bool: ', my_bool)
new_bool = not my_bool
print('new_bool: ', new_bool)
print('type(new_bool): ', type(new_bool))
print('')

my_bool = 290 >= 220 > 3
print('my_bool: ', my_bool)
new_bool = not my_bool
print('new_bool: ', new_bool)
print('type(new_bool): ', type(new_bool))
print('')

my_int = 788
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('')

my_int = -188
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('')

my_int = 0
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('')

my_int = -1.7
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('')

my_int = 0.0
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('')

# Зміна точності
my_int = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
print('bool(my_int): ', bool(my_int))
print('type(my_int): ', type(my_int))
print('')

val_1 = 25.352463457656456
val_2 = 25.35246345754363456856785678
print(val_1==val_2)
print(abs(val_1 - val_2) < 0.001)
print('')

my_str = '1'
print('bool(my_str): ', bool(my_str))
print('')

my_str = ''
print('bool(my_str): ', bool(my_str))
print('')

my_str = '       '
print('bool(my_str): ', bool(my_str))
print('')

my_str = 'True'
print('bool(my_str): ', bool(my_str))
print('')

my_bool = True
print('my_bool: ', my_bool)
my_int = int(my_bool)
print('my_int: ', my_int)
print('type(my_int): ', type(my_int))
my_str = str(my_bool)
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print('')

my_str = 'False'
print('bool(my_str): ', bool(my_str))
print('')

my_bool = False
print('my_bool: ', my_bool)
my_int = int(my_bool)
print('my_int: ', my_int)
print('type(my_int): ', type(my_int))
my_str = str(my_bool)
print('my_str: ', my_str)
print('type(my_str): ', type(my_str))
print('bool(my_str): ', bool(my_str))
print('type(my_str): ', type(my_str))
print('')

my_val = None
print('bool(my_val): ', bool(my_val))
print('')

my_val = NotImplemented
print('bool(my_val): ', bool(my_val))
print('')

my_val = Ellipsis
print('bool(my_val): ', bool(my_val))
print('type(my_val): ', type(my_val))
print('')





# ================================================
# Условний оператор if
# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# if current_temperature < 5:
#     print('Одень шапку!')
# else:
#     print('Можеш не одевать шапку')

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# if current_temperature < 5:
#     print('Одень шапку!')
# elif current_temperature > 25:
#     print('Одень кепку!')
# else:
#     print('Можеш не одевать шапку')

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# if current_temperature < 5:
#     print('Одень шапку!')
# elif current_temperature > 25:
#     print('Одень кепку!')
# elif current_temperature < -25: # ошибка последовательности условного оператора
#     print('Останься дома!')
# else:
#     print('Можеш не одевать шапку')

# my_str = ''
# if my_str:
#     print(my_str)