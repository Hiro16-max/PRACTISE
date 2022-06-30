def parse(arr):
    i = 0
    state = 'старт'
    for i in range(len(arr)):
        a = arr[i][1]
        match state:
            case 'старт':
                if arr[i][1] == 'кл_repeat':
                    state = 'кл_слово'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'кл_слово':
                if arr[i][1] == 'индентификатор':
                    state = 'индентификатор'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'индентификатор':
                if arr[i][1] == 'оператор_присваивания':
                    state = 'оператор_присваивания'
                elif arr[i][1] == 'лев_скобка':
                    state = 'лев_скобка'
                elif arr[i][1] == 'прав_скобка':
                    state = 'прав_скобка'
                elif arr[i][1] == 'лев_кв_скобка':
                    state = 'лев_кв_скобка'
                elif arr[i][1] == 'число':
                    state = 'число'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'лев_скобка':
                if arr[i][1] == 'индентификатор':
                    state = 'индентификатор'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'прав_скобка':
                if arr[i][1] == 'тчкзпт':
                    return True
                else: 
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'лев_кв_скобка':
                if arr[i][1] == 'число':
                    state = 'число'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'прав_кв_скобка':
                if arr[i][1] == 'прав_скобка':
                    state = 'прав_скобка'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'оператор_присваивания':
                if arr[i][1] == 'число':
                    state = 'число'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'число':
                if arr[i][1] == 'кл_until':
                    state = 'кл_until'
                elif arr[i][1] == 'прав_кв_скобка':
                    state = 'прав_кв_скобка'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
            case 'кл_until':
                if arr[i][1] == 'индентификатор':
                    state = 'индентификатор'
                else:
                    with open('output.txt', 'w') as file:
                        file.write("REJECT")
                    exit()
    i += 1