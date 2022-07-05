
from determinant import get_keywords
from translator import get_lexemes
from syntax import analyze_syntax
from lexical import get_words

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        line = file.readline()

    lexemes = get_words(get_lexemes(line))
    
    result = analyze_syntax(get_keywords(lexemes)) if lexemes != 'ошибка' else False

    with open("output.txt", "w") as file:
            line = file.write("ACCEPT" if result else "REJECT")