def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y



def max_of_three(x, y, z):
     if x <= y and z <= y:
        return y
    elif y <= x and z <= x:
        return x
    elif y <= z and x <= z:
        return z
