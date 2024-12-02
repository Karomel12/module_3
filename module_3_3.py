def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [True, 23, 'str']
values_dict = {'a': 2.43, 'b': [1,2,3], 'c':False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [13, 'Строка' ]
print_params(*values_list_2, True)