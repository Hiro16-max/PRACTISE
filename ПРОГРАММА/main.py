from lexer_test import get_words
from parser import get_keyword
from translator import get_lexeme
from syntax import analyze_sytax



if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        line = file.readline()

    lexemes = get_lexeme(line)
    print(lexemes)
    lexemes = get_words(lexemes)
    if lexemes != 'ошибка':
        print(lexemes)
        lexemes = get_keyword(lexemes)
        result = analyze_sytax(lexemes)
    else:
        result = False

    with open("output.txt", "w") as file:
        line = file.write("ACCEPT" if result else "REJECT")



