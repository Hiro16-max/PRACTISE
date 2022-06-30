from translator import get_lexeme
from lexer import get_words
from parser import parse




if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        line = file.readline()

    lexeme = get_lexeme(line)

    words = get_words(lexeme)

    parse(words)
    
    with open('output.txt', 'w') as file:
                file.write("ACCEPT")
