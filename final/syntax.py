def analyze_syntax(lexemes) -> bool:
    state = 'нач'
    for lexeme in lexemes:
        match state:
            case 'нач':
                if lexeme[1] == 'клслово_repeat':
                    state = 'имя1'
                else:
                    return False
            case 'имя1':
                if lexeme[1] == 'идентификатор':
                    state = 'присваивание'
                else:
                    return False
            case 'присваивание':
                if lexeme[1] == 'оператор':
                    state = 'знак1'
                else:
                    return False
            case 'знак1':
                if lexeme[1] == 'знак':
                    state = 'число1'
                elif lexeme[1] == 'число':
                    state = 'клслово'
                else:
                    return False
            case 'число1':
                if lexeme[1] == 'число':
                    state = 'клслово'
                else:
                    return False
            case 'клслово':
                if lexeme[1] == 'клслово_until':
                    state = 'имя2'
                else:
                    return False
            case 'имя2':
                if lexeme[1] == 'идентификатор':
                    state = 'отк_скоб'
                else:
                    return False
            case 'отк_скоб':
                if lexeme[1] == 'лев_скобка':
                    state = 'имя3'
                else:
                    return False
            case 'имя3':
                if lexeme[1] == 'идентификатор':
                    state = 'отк_кв_скоб'
                else:
                    return False
            case 'отк_кв_скоб':
                if lexeme[1] == 'прав_скобка':
                    state = 'выход'
                elif lexeme[1] == 'лев_кв_скобка':
                    state = 'знак2'
                else:
                    return False
            case 'знак2':
                if lexeme[1] == 'знак':
                    state = 'число2'
                elif lexeme[1] == 'число':
                    state = 'зак_кв_скоб'
                else:
                    return False
            case 'число2':
                if lexeme[1] == 'число':
                    state = 'зак_кв_скоб'
                else:
                    return False
            case 'зак_кв_скоб':
                if lexeme[1] == 'прав_кв_скобка':
                    state = 'зак_скоб'
                else:
                    return False
            case 'зак_скоб':
                if lexeme[1] == 'прав_скобка':
                    state = 'выход'
                else:
                    return False
            case 'выход':
                if lexeme[1] == 'тчкзпт':
                    return True
    return False