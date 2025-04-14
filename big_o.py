# o(1) constant time
def add_me(n):
    return n+n

# o(n)
def print_n(n):
    for i in range(n):
        print(i)

def print_2n(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

# o(n^2)
def print_nn(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

def print_nn(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
    for k in range(n): # n^2 + n = n^2
        print(k)

# o(log n)
