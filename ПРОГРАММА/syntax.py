from operator import le


def analyze_sytax(lexemes) -> bool:
    correct_syntax = [
        ['клслово_repeat', 'не_клслово', 'оператор_присваивания', 'число', 'клслово_until', 'не_клслово', 'лев_скобка', 'не_клслово', 'прав_скобка', 'тчкзпт'],
        ['клслово_repeat', 'не_клслово', 'оператор_присваивания', 'число', 'клслово_until', 'не_клслово', 'лев_скобка', 'не_клслово', 'лев_кв_скобка', 'число', 'прав_кв_скобка', 'прав_скобка', 'тчкзпт']
    ]

    if len(lexemes) == len(correct_syntax[0]):
        option = 0
    elif len(lexemes) == len(correct_syntax[1]):
        option = 1
    else:
        return False

    return all(lexeme[1] == correct_syntax[option][id] for id, lexeme in enumerate(lexemes))





