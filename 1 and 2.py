from pprint import pprint


def get_cook_book(recipes):
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        menu = {}
        for line in file:
            recipe_name = line.strip()
            ing_count = int(file.readline().strip())
            ingredients_list = []
            for i in range(ing_count):
                ingredients = file.readline().strip()
                ingredients_name, quantity, measure = ingredients.split(' | ')
                ingredients_list.append({
                    'ingredients_name': ingredients_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book = {recipe_name: ingredients_list}
            menu.update(cook_book)
    return menu


def get_shop_list_by_dishes(dishes, person_count):
    menu = get_cook_book('recipes.txt')
    dishes_list = {}
    for dish in dishes:
        if dish in menu.keys():
            for ingredients in menu[dish]:
                item = ingredients['ingredients_name']
                if item in dishes_list.keys():
                    dishes_list[item]['quantity'] += int(ingredients['quantity']) * person_count
                else:
                    measure = ingredients['measure']
                    dishes_list[item] = {'quantity': int(ingredients['quantity']) * person_count, 'measure': measure}

    return dishes_list


pprint(get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3))
pprint(get_cook_book('recipes.txt'))
