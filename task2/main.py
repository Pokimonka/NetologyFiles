#вероятно можно было проще, или есть инструменты
# для считывания файла и формирования json.object,
#но я написала вот такой костыль)))
cook_book = {}
def parse_file():
    count_ingredients = 0
    inner_dict = []
    m_key = ""
    with open("recipe.txt", "r") as file1:
        for line in file1:
            strip_line = line.strip("\n")
            if strip_line.isdigit() and type(int(strip_line)) == int:
                count_ingredients = int(line.strip("\n"))
                continue
            if count_ingredients != 0:
                tmp = strip_line.split("|")
                in_d = {'ingredient_name': tmp[0], 'quantity': tmp[1], 'measure': tmp[2]}
                inner_dict.append(in_d)
                count_ingredients -= 1
            elif type(strip_line) == str:
                if strip_line != "":
                    m_key = strip_line
                if len(inner_dict) != 0:
                    cook_book[m_key] = inner_dict
                    inner_dict = []
        cook_book[m_key] = inner_dict

#по заданию функция принимает только два значения, так что cook_book глобальная
def get_shop_list_by_dishes(dishes, person_count):
    result = "{"
    first = True
    # Если есть другие варианты добавление в словарь одинаковых ключей - напишите пожалуйста
    for dish in dishes:
        for ingr in cook_book[dish]:
            tmp = {}
            tmp[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': int(ingr['quantity'])*person_count}
            if first:
                result += "\n" + "\t" + str(tmp)
                first = False
            else:
                result += "," + "\n" + "\t" + str(tmp)
    result += "\n}"
    return result

if __name__ == '__main__':
    parse_file()
    print((get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)))
    print((get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 3)))
