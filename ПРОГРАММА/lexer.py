from string import digits

def get_keyword(lexemes): 
    keywords = ["and", "array", "asm", "begin", "break", "case", "const",
                "constructor", "continue", "destructor", "div", "do", "downto",
                "else", "end", "false", "file", "for", "function", "goto", "if",
                "implementation", "in", "inline", "interface", "label", "mod", "nil",
                "not", "object", "of", "on", "operator", "or", "packed", "procedure",
                "program", "record", "repeat", "set", "shl", "shr", "string", "then",
                "to", "true", "type", "unit", "until", "uses", "var", "while", "with", "xor"]

    for word, lexeme in enumerate(lexemes):
        if lexeme[1] == "индентификатор":
            if lexeme[0].lower() in keywords:
                lexemes[word] = (lexeme[0], "клслово")
            else:
                lexemes[word] = (lexeme[0], "не_клслово")

    return lexemes

def _is_word(lexeme: str) -> bool:
    return any((symbol not in digits) and (symbol != '-') for symbol in lexeme)


def get_words(tokens):
    ret = []
    word = ''
    for token in tokens:
        match token[1]:
            case "буква":
                word += token[0]
            case "цифра":
                word += token[0]
            case "знак":
                word += token[0]
            case "пробел":
                if word:
                    ret.append((word, "индентификатор" if _is_word(word) else "число"))
                    word = ""
            case _:
                if word:
                    ret.append(
                        (word, "индентификатор" if _is_word(word) else "число"))
                    word = ""
                ret.append(token)

    return ret
            