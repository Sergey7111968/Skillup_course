# 1. Создать ф-цию которая будет возвращать группу детей в качестве списка из словарей

def list_children():
    Children = {
        'child1' : {
        'name' : 'Alex',
        'age' : 4,
        'weight' : 40.5
        },
         'child2' : {
        'name' : 'Max',
        'age' : 5,
        'weight' : 20
        },
    }
        
    from pprint import pprint
    pprint([Children])
    
list_children()

# 2. Создать ф-цию которая будет возвращать группу детей в качестве списка из классов

def class_children():
    class child:
        name = 'Alex'
        age = 4
        weight = 40.5

    Alex=child()
        
    class child:
        name = 'Max'
        age = 5
        weight = 20

    Max=child()
    
    from pprint import pprint
    pprint([ Alex.name, Alex.age, Alex.weight, Max.name, Max.age, Max.weight])


class_children()