def get_trans_table() -> dict:
    table = {i: 'буква' for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for i in '0123456789':
        table[i] = 'цифра'
    table['-'] = 'знак'
    table[' '] = 'пробел'
    table[';'] = 'тчкзпт'
    table['='] = 'равно'
    table['('] = 'лев_скобка'
    table[')'] = 'прав_скобка'
    table['['] = 'лев_кв_скобка'
    table[']'] = 'прав_кв_скобка'   
    table[':'] = 'двоеточие'
    return table

table = get_trans_table()

def get_lexemes(line) -> list:
    ret = []
    for i in line:
        if i in table:
            ret.append([i, table[i].lower()])
        else:
            ret.append([i, 'ошибка'])
    return ret