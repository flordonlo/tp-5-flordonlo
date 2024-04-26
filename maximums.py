# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y




def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if x <= y and z <= y:
        return y
    elif y <= x and z <= x:
        return x
    elif y <= z and x <= z:
        return z
