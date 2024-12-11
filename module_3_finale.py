data_structure = [
[1, 2, 3], # 5
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*data):
    sum = 0
    for elem in data:
        if isinstance(elem, (int,float,bool)):
            sum += elem
            continue
        if isinstance(elem, str):
            sum += len(elem)
            continue
        if isinstance(elem, (list,tuple,set)):
            sum += calculate_structure_sum(*elem)
            continue
        if isinstance(elem, dict):
            sum += calculate_structure_sum(*elem.items())
            continue
    return sum

result = calculate_structure_sum(data_structure)
print(result)

