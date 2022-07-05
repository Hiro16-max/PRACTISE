def get_keywords(lexemes) -> list: 
    keywords = ['and', 'array', 'asm', 'begin', 'break', 'case', 'const',
                'constructor', 'continue', 'destructor', 'div', 'do', 'downto',
                'else', 'end', 'false', 'file', 'for', 'function', 'goto', 'if',
                'implementation', 'in', 'inline', 'interface', 'label', 'mod', 'nil',
                'not', 'object', 'of', 'on', 'operator', 'or', 'packed', 'procedure',
                'program', 'record', 'repeat', 'set', 'shl', 'shr', 'string', 'then',
                'to', 'true', 'type', 'unit', 'until', 'uses', 'var', 'while', 'with', 'xor']

    for id, pair in enumerate(lexemes):
        if pair[1] == 'идентификатор' and pair[0].lower() in keywords:
            if pair[0].lower() == 'repeat':
                lexemes[id] = [pair[0], 'клслово_repeat']
            elif pair[0].lower() == 'until':
                lexemes[id] = [pair[0], 'клслово_until']
            else:
                lexemes[id] = [pair[0], 'другое_клслово']
    return lexemes