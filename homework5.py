my_list = ['яблоко', 'банан', 'киви', 'груша','ананас','кокос']
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[3:])
my_list[3] = 'авакадо'
print(my_list)

my_dict = {'car': 'машина', 'plane' : 'самолет', 'a train' : 'поезд'}
print(my_dict.get('plane'))
my_dict.setdefault('cat', 'кошка')
print(my_dict)