
def find_sqrt(x):
    for i in range(x//2+1):
        if (i*i == x):
            return i
    return 0

def is_sq(x):
    y = find_sqrt(x)
    if (y*y == x):
        return True
    return False

