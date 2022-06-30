from translator import get_lexeme

line = ("repeat myvar:=-123 until func(id);")

tokens = get_lexeme(line)

state = "start"
current_space = 0
current_state = ""
current_word = ""

i = 0
while i < 15:
    current_state = tokens[i][1]
    next_state = tokens[i+1][1]
    match state:

        case "start":

            if next_state == "буква" and current_state == "буква":
                state = current_state
                current_word += tokens[i][0]
            else: 
                print("Цепочка не верна")
                break
            
        case "буква":

            if next_state == "буква":
                state = current_state
                current_word += tokens[i][0]
            elif next_state == "скобка" or "двоеточие":
                state = current_state
                current_word += tokens[i][0]
            elif next_state == "пробел":
                state = current_state
                current_word += tokens[i][0]
                current_space += 1
                print("1")
            else:
                print("Цепочка не верна")
                print(1)
                break
        case "пробел":
            state = current_state
            print("1")         
            
            
    i+=1