def get_words(tokens) -> list:
    state = 'нач'
    word = ''
    ret = []
    for token in tokens:
        match state:
            case 'нач':
                if token[1] == 'буква':
                    word += token[0]
                    state = 'идентификатор'
                else:
                    state = 'E'
            case 'идентификатор':
                if token[1] == 'буква' or token[1] == 'цифра':
                    word += token[0]
                elif token[1] == 'пробел':
                    ret.append([word, 'идентификатор'])
                    word = ''
                    state = 'пробел'
                elif token[1] == 'двоеточие':
                    ret.append([word, 'идентификатор'])
                    word = ''
                    word += token[0]
                    state = 'присваивание'
                elif token[1] == 'лев_скобка':
                    ret.append([word, 'идентификатор'])
                    word = ''
                    ret.append([token[0], token[1]])
                    state = 'отк_скобок'
                elif token[1] == 'прав_скобка':
                    ret.append([word, 'идентификатор'])
                    word = ''
                    ret.append([token[0], token[1]])
                    state = 'тчкзпт'
                elif token[1] == 'лев_кв_скобка':
                    ret.append([word, 'идентификатор'])
                    word = ''
                    ret.append([token[0], token[1]])
                    state = 'знак'
                else:
                    state = 'E'
            case 'пробел':
                if token[1] == 'буква':
                    word += token[0]
                    state = 'идентификатор'
                elif token[1] == 'цифра':
                    word += token[0]
                    state = 'число'
                elif token[1] == 'знак':
                    ret.append([token[0], token[1]])
                    state = 'знак'
                elif token[1] == 'пробел':
                    continue
                else:
                    state = 'E'
            case 'отк_скобок':
                if token[1] == 'буква':
                    word += token[0]
                    state = 'идентификатор'
                elif token[1] == 'пробел':
                    continue
                else:
                    state = 'E'
            case 'присваивание':
                if token[1] == 'равно':
                    word += token[0]
                    ret.append([word, 'оператор'])
                    word = ''
                    state = 'знак'
                else:
                    state = 'E'
            case 'знак':
                if token[1] == 'цифра':
                    word += token[0]
                    state = 'число'
                elif token[1] == 'знак':
                    ret.append([token[0], token[1]])
                    state = 'пробел'
                elif token[1] == 'пробел':
                    continue
                else:
                    state = 'E'
            case 'число':
                if token[1] == 'цифра':
                    word += token[0]
                elif token[1] == 'пробел':
                    ret.append([word, 'число'])
                    word = ''
                    state = 'пробел'
                elif token[1] == 'прав_кв_скобка':
                    ret.append([word, 'число'])
                    word = ''
                    ret.append([token[0], token[1]])
                    state = 'закрытие скобок'
                else:
                    state = 'E'
            case 'закрытие скобок':
                if token[1] == 'прав_скобка':
                    ret.append([token[0], token[1]])
                    state = 'тчкзпт'
                else:
                    state = 'E'
            case 'тчкзпт':
                if token[1] == 'тчкзпт':
                    ret.append([token[0], token[1]])
                    return ret
                else:
                    state = 'E'
            case 'E':
                ret = 'ошибка'
                return ret        
    return ret        