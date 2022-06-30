def get_key_word(word):
    key_word = ['repeat', 'until']   
    if word in key_word and word == key_word[0]:
        word = 'кл_repeat'  
    elif word in key_word and word == key_word[1]:
        word ='кл_until'
    else:
        word = 'индентификатор'
    return word

def get_words(tokens):
    state = "старт"
    identifier = ''
    operator = ''
    number = ''
    ret = []
    i = 0
    for i in range(len(tokens)):
        match state:
            case "старт":
                if tokens[i][1] == 'буква':
                    identifier += tokens[i][0]
                    state = 'индентификатор'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'индентификатор':
                if tokens[i][1] == 'буква' or tokens[i][1] == 'число':
                   identifier += tokens[i][0]
                elif tokens[i][1] == 'пробел':
                    key = get_key_word(identifier)                    
                    ret.append((identifier, key))
                    identifier = ''
                    state = 'пробел'
                elif tokens[i][1] == 'двоеточие':
                    key = get_key_word(identifier)  
                    ret.append((identifier, key))
                    identifier = ''
                    operator += tokens[i][0]
                    state = 'присваивание'
                elif tokens[i][1] == 'лев_скобка':
                    key = get_key_word(identifier)  
                    ret.append((identifier, key))
                    identifier = ''
                    ret.append((tokens[i][0], 'лев_скобка'))
                    state = 'лев_скобка'
                elif tokens[i][1] == 'прав_скобка':
                    key = get_key_word(identifier)  
                    ret.append((identifier, key))
                    identifier = ''
                    ret.append((tokens[i][0], 'прав_скобка'))
                    state = 'прав_скобка'
                elif tokens[i][1] == 'лев_кв_скобка':
                    key = get_key_word(identifier)  
                    ret.append((identifier, key))
                    identifier = ''
                    ret.append((tokens[i][0], 'лев_кв_скобка'))
                    state = 'лев_кв_скобка'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'пробел':
                if tokens[i][1] == 'буква':
                    identifier += tokens[i][0]
                    state = 'индентификатор'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'присваивание':
                if tokens[i][1] == 'знак':
                    number += tokens[i][0]
                    state = 'знак'
                elif tokens[i][1] == 'равно':
                    operator += tokens[i][0]
                    ret.append((operator, 'оператор_присваивания'))
                    state = 'знак'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'знак':
                if tokens[i][1] == 'знак':
                    number += tokens[i][0]
                    state = 'целое_число'
                elif tokens[i][1] == 'цифра':
                    number += tokens[i][0]
                    state = 'целое_число'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'целое_число':
                if tokens[i][1] == 'цифра':
                    number += tokens[i][0]
                elif tokens[i][1] == 'пробел':
                    ret.append((number, 'число'))
                    number = ''
                    state = 'пробел'
                elif tokens[i][1] == 'прав_кв_скобка':
                    ret.append((number, 'число'))
                    number = ''
                    ret.append((tokens[i][0], 'прав_кв_скобка'))
                    state = 'прав_кв_скобка'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'лев_скобка':
                if tokens[i][1] == 'буква':
                    identifier += tokens[i][0]
                    state = 'индентификатор'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'прав_скобка':
                if tokens[i][1] == 'тчкзпт':
                    ret.append((tokens[i][0], 'тчкзпт'))
                    return ret
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'прав_кв_скобка':
                if tokens[i][1] == 'тчкзпт':
                    ret.append((tokens[i][0], 'тчкзпт'))
                    return ret
                elif tokens[i][1] == 'прав_скобка':
                    ret.append((tokens[i][0], 'прав_скобка'))
                    state = 'прав_скобка'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'лев_кв_скобка':
                if tokens[i][1] == 'цифра':
                    number += tokens[i][0]
                    state = 'целое_число'
                elif tokens[i][1] == 'знак':
                    number += tokens[i][0]
                    state = 'целое_число'
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
        i += 1