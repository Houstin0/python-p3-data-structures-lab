spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_list=[spice.get("name") for spice in spicy_foods ]
    print(spicy_list)
    return spicy_list
# get_names(spicy_foods)        

def get_spiciest_foods(spicy_foods):
    spicy_list=[spice for spice in spicy_foods if spice["heat_level"]>5]
    print(spicy_list)
    return spicy_list
# get_spiciest_foods(spicy_foods)    

def print_spicy_foods(spicy_foods):
    spicy_list=[print(f"{spice['name']} ({spice['cuisine']}) | Heat Level: {'🌶'*spice['heat_level']}") for spice in spicy_foods]
    return spicy_list
# print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spice in spicy_foods:
        if cuisine==spice["cuisine"]:
            print(spice)
            return spice 
# get_spicy_food_by_cuisine(spicy_foods,"American")

def print_spiciest_foods(spicy_foods):
    spiciest=[spice for spice in spicy_foods if spice["heat_level"]>5]
    print_spicy_foods(spiciest)
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    total_heat=sum( spice["heat_level"] for spice in spicy_foods)
    length=len(spicy_foods)
    average=total_heat/length
    print(average)
    return average
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    new_list=spicy_foods.copy()
    new_list.append(spicy_food)
    print(new_list)
    return new_list
create_spicy_food(spicy_foods, {
                'name': 'Griot',
                'cuisine': 'Haitian',
                'heat_level': 10,
            },)
