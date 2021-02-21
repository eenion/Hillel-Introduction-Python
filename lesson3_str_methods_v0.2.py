explore_str = 'Hello world!\t My name is {name} ©'
explore_str2 = 'Hello world!'
explore_str3 = 'Hello\n world!'

class MyDict(dict):
    def __missing__(self, key):
        return key

sequence = ('milk', 'cheese', 'sour cream')

print(explore_str2)
print(dir(explore_str))
print(explore_str2.capitalize()) 
print(explore_str2.casefold()) 
print(explore_str2.center(35)) 
print(explore_str2.count('o')) 
print(explore_str2.encode()) 
print(explore_str.endswith("©")) 
print(explore_str.expandtabs(4).format(name = 'Oleg'))  
print(explore_str.find('rld')) 
print(explore_str.format(name = 'Oleg')) 
print(explore_str.format_map(MyDict(name = 'Oleg'))) 
print(explore_str.index('©')) 
print(explore_str.isalnum()) 
print(explore_str.isalpha()) 
print(explore_str.isascii()) 
print(explore_str.isdecimal()) 
print(explore_str.isdigit()) 
print(explore_str.isidentifier()) 
print(explore_str.islower()) 
print(explore_str.isnumeric()) 
print(explore_str.isprintable()) 
print(explore_str.isspace()) 
print(explore_str.istitle()) 
print(explore_str.isupper()) 
print('👍'.join(sequence)) 
print(explore_str2.ljust(150, '-')) 
print(explore_str2.lower()) 
print(explore_str2.lstrip('Hello')) 
print(explore_str.lstrip('Hello').format(name = 'Oleg')) 

x = 'H'  
y = 'h'  
z = 'wr' 
tbl = explore_str2.maketrans(x, y, z) 
print(explore_str2.translate(tbl))

print(explore_str2.partition('!')) 
print(explore_str2.replace('world', 'Kitty')) 
print(explore_str.rfind('u'))
print(explore_str.rindex('l')) 
print(explore_str2.rjust(67)) 
print(explore_str2.rpartition('o')) 
print(explore_str.rsplit(maxsplit=2)) 
print(explore_str2.rstrip('rld!')) 
print(explore_str2.split(None, maxsplit=-1))
print(explore_str3.splitlines()) 
print(explore_str3.startswith('H')) 
print(explore_str2.strip('!Hed')) 
print(explore_str3.swapcase()) 
print(explore_str2.title()) 

x = {'w': 'm', 'l': 'r', 'r': 'l', 'r': 'q', 'r': 'a'} 
tbl = explore_str2.maketrans(x)
print(explore_str2.translate(tbl)) 

print(explore_str2.upper()) 
print(explore_str2.zfill(13)) 
print('The End!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')