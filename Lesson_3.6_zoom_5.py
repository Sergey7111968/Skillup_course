# OOP

list
lion1 = ['Alex', 4, 50]
lion2 = ['Boo', 2, 38.5]

lions = [ lion1, lion2]

# dictionary
 
lions = {
    'lion1' : {
        'name' : 'Alex' ,
        'age' : 4,
        'weght' : 50
    },
    'lion2' : {
        'name' : 'Boo' ,
        'age' : 2,
        'weght' : 38.5
    }
}

lions['lion3'] = {
    'name' : 'Zoo' ,
    'age' : 3,
    'weght' : 12
}

lions['audi'] = {
    'name' : 'Audi' ,
    'series' : 'A',
    'model' : '6',
    'year' : 2019
}


# from pprint import pprint
# pprint(lions)

def validate_lion(name: str, data: dict) -> bool:
    if name in lions:
        return False
    required_fields = ['name', 'age', 'weight']
    for key in data:
        if key not in required_fields:
            print(f'"{key}" field is not supported')
            return False
    print(f'"{key}" field is supported')
    return True

def add_lion(name: str, data: dict) -> None:
    lion_is_valid = validate_lion(name = name, data = data)
    if lion_is_valid:
        lions[name] = data

# from pprint import pprint
# pprint(lions)


foo = {
    'name' : 'Foo',
    'data' : {
        'name' : 'Zoo' ,
        'age' : 3,
        'weight' : 12
    }
}
add_lion(**foo)

from pprint import pprint
pprint(lions)

# Alex = {
#     'name' : 'Alex',
#     'age' : 4,
#     'weight' : 40.5
# }

# print(Alex['name'], Alex['age'], Alex['weight'])

# class Alex:
#     name = 'Alex'
#     age = 4
#     weight = 40.5

# print(Alex.name, Alex.age, Alex.weight)
