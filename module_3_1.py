calls = 0
def count_calls ():            #Счетчик
    global calls
    calls = int(calls) + 1

def string_info (string):       #Работа со строкой
    count_calls()
    string = (len(string), string.upper(),string.lower())
    return string

def is_contains (string, list_to_search):      #Проверка нахождения в списке
    count_calls()
    if string.lower() in str(list_to_search).lower():
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

# P.s Пытался сделать через input, к сожалению не вышло, не знаю как input привести к списку
# print()
# print(string_info(input('Введите слово: ')))
# print()
# print(is_contains(input('Введите слово: ').lower(),list(input('Список для проверки: '))))