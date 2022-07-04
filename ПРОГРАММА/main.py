from lexer import get_words
from parser import get_keyword
from translator import get_lexeme
# from syntax import get_words



if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        line = file.readline()

    lexemes = get_lexeme(line)

    lexemes = get_words(lexemes)
    print(lexemes)
    # if lexemes != 'ошибка':
        
    #     lexemes = get_keyword(lexemes)
    #     print(lexemes)
    #     result = analyze_syntax(lexemes)
    # else:
    #     result = False

    # with open("output.txt", "w") as file:
    #     line = file.write("ACCEPT" if result else "REJECT")



