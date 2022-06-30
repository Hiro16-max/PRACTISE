def get_words(tokens):
    state = "старт"
    identifier = ""
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
                else: return False
            case 'индентификатор':
                if tokens[i][1] == 'буква' or tokens[i][1] == 'число':
                   identifier += tokens[i][0]
                elif tokens[i][1] == 'пробел':                    
                    ret.append((identifier, 'индентификатор'))
                    identifier = ''
                    ret.append((tokens[i][0], 'пробел'))
                    state = 'пробел'
                elif tokens[i][1] == 'двоеточие':
                    ret.append((identifier, 'индентификатор'))
                    identifier = ''
                    operator += tokens[i][0]
                    state = 'присваивание'
                elif tokens[i][1] == 'лев_скобка':
                    ret.append((identifier, 'индентификатор'))
                    identifier = ''
                    state = 'лев_скобка'
                    ret.append((tokens[i][0], 'лев_скобка'))
                elif tokens[i][1] == 'прав_скобка':
                    ret.append((identifier, 'индентификатор'))
                    identifier = ''
                    state = 'прав_скобка'
                    ret.append((tokens[i][0], 'прав_скобка'))
                elif tokens[i][1] == 'лев_кв_скобка':
                    ret.append((identifier, 'индентификатор'))
                    identifier = ''
                    state = 'лев_кв_скобка'
                    ret.append((tokens[i][0], 'лев_кв_скобка'))
                else: return False
            case 'пробел':
                if tokens[i][1] == 'буква':
                    identifier += tokens[i][0]
                    state = 'индентификатор'
                else: return False
            case 'присваивание':
                if tokens[i][1] == 'знак':
                    operator += tokens[i][0]
                    ret.append((operator, 'оператор_присваивания'))
                    state = 'знак'
                elif tokens[i][1] == 'равно':
                    operator += tokens[i][0]
                    ret.append((operator, 'оператор_присваивания'))
                    state = 'знак'
                else: return False
            case 'знак':
                if tokens[i][1] == 'знак':
                    ret.append((tokens[i][0], 'знак'))
                    state = 'целое_число'
                elif tokens[i][1] == 'число':
                    number += tokens[i][0]
                    state = 'целое_число'
                else: return False
            case 'целое_число':
                if tokens[i][1] == 'цифра':
                    number += tokens[i][0]
                elif tokens[i][1] == 'пробел':
                    ret.append((number, 'число_без_знака'))
                    number = ''
                    state = 'пробел'
                elif tokens[i][1] == 'прав_кв_скобка':
                    ret.append((number, 'число_без_знака'))
                    number = ''
                    state = 'прав_кв_скобка'
                else: return False
            case 'лев_скобка':
                if tokens[i][1] == 'буква':
                    identifier += tokens[i][0]
                    state = 'индентификатор'
                else: return False
            case 'прав_скобка':
                if tokens[i][1] == 'тчкзпт':
                    ret.append((tokens[i][0], 'тчкзпт'))
                    return ret
                else: return False
            case 'прав_кв_скобка':
                if tokens[i][1] == 'тчкзпт':
                    ret.append((tokens[i][0], 'тчкзпт'))
                    return ret
                elif tokens[i][1] == 'прав_скобка':
                    state = 'прав_скобка'
                    ret.append((tokens[i][0], 'прав_скобка'))
                else: return False
            case 'лев_кв_скобка':
                if tokens[i][1] == 'цифра':
                    number += tokens[i][0]
                    state = 'целое_число'
                elif tokens[i][1] == 'знак':
                    ret.append((tokens[i][0], 'знак'))
                    state = 'целое_число'
                else: return False
        i += 1