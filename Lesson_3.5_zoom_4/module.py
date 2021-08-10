""" module.py - an example of Python module"""

# __counter = 0

def sum1(list):
    # global __counter
    # __counter += 1
    # print(__counter)
    sum = 0
    for element in list:
        sum += element
            
    return sum
    

def prod1(list):
    # global __counter
    # __counter += 1
    prod = 1
    for element in list:
        prod *= element
    
    return prod 

if __name__=='__main__':
    print("I prefer to be a module, but I can do some tests for you")
    l=[i+1 for i in range(5)]
    print(l)
    print(sum1(l) == 15)
    print(prod1(l) == 120)

