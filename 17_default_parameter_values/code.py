# Description: Default parameter values
def add(x, y = 8):
    print(x + y)

add(x = 5) # 13
add(x = 5, y = 2) # 7
add(y = 5, x = 3) # 8


## default parameter values
default_y = 3

def add(x, y = default_y):
    sum = x + y

add(2) # 5
default_y = 4
add(2) # 5
