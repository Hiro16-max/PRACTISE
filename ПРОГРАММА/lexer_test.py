def get_words(tokens):
    state = "старт"
    word = ''
    ret = []
    for token in tokens:
        match state:
            case "старт":
                if token[1] == 'буква':
                    word += token[0]
                    state = 'индентификатор'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'индентификатор':
                if token[1] == 'буква' or token[1] == 'число':
                   word += token[0]
                elif token[1] == 'пробел':                  
                    ret.append((word, 'индентификатор'))
                    word = ''
                    state = 'пробел'
                elif token[1] == 'двоеточие':  
                    ret.append((word, 'индентификатор'))
                    word = ''
                    word += token[0]
                    state = 'присваивание'
                elif token[1] == 'лев_скобка':
                    ret.append((word, 'индентификатор'))
                    word = ''
                    ret.append((token[0], 'лев_скобка'))
                    state = 'лев_скобка'
                elif token[1] == 'прав_скобка': 
                    ret.append((word, 'индентификатор'))
                    word = ''
                    ret.append((token[0], 'прав_скобка'))
                    state = 'прав_скобка'
                elif token[1] == 'лев_кв_скобка':
                    ret.append((word, 'индентификатор'))
                    word = ''
                    ret.append((token[0], 'лев_кв_скобка'))
                    state = 'лев_кв_скобка'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'пробел':
                if token[1] == 'буква':
                    word += token[0]
                    state = 'индентификатор'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'присваивание':
                if token[1] == 'знак':
                    word += tokens[0]
                    state = 'знак'
                elif token[1] == 'равно':
                    word += token[0]
                    ret.append((word, 'оператор_присваивания'))
                    word = ''
                    state = 'знак'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                        
            case 'знак':
                if token[1] == 'знак':
                    word += token[0]
                    state = 'целое_число'
                elif token[1] == 'цифра':
                    word += token[0]
                    state = 'целое_число'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'целое_число':
                if token[1] == 'цифра':
                    word += token[0]
                elif token[1] == 'пробел':
                    ret.append((word, 'число'))
                    word = ''
                    state = 'пробел'
                elif token[1] == 'прав_кв_скобка':
                    ret.append((word, 'число'))
                    word = ''
                    ret.append((token[0], 'прав_кв_скобка'))
                    state = 'прав_кв_скобка'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'лев_скобка':
                if token[1] == 'буква':
                    word += token[0]
                    state = 'индентификатор'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'прав_скобка':
                if token[1] == 'тчкзпт':
                    ret.append((token[0], 'тчкзпт'))
                    return ret
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'прав_кв_скобка':
                if token[1] == 'тчкзпт':
                    ret.append((token[0], 'тчкзпт'))
                    return ret
                elif token[1] == 'прав_скобка':
                    ret.append((token[0], 'прав_скобка'))
                    state = 'прав_скобка'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
            case 'лев_кв_скобка':
                if token[1] == 'цифра':
                    word += token[0]
                    state = 'целое_число'
                elif token[1] == 'знак':
                    word += token[0]
                    state = 'целое_число'
                elif token[1] == 'ошибка':
                    ret = 'ошибка'
                    return ret
                 
    return ret
        