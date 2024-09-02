my_dict = {'Anna': 1991, 'Vyacheslav': 2020, 'Zhanna': 1972,}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Aldar'))
z = my_dict.pop('Zhanna')
print(z)
my_dict ['Bulat'] = 1968
my_dict ['Fedor'] = 1962
print(my_dict)

my_set = {10,11,12,10,11,12,13,14, 1107.0703, 'мир'}
print(my_set)
my_set.update([15, 100, (21,22,23)])
print(my_set)
my_set.remove(12)
print(my_set)