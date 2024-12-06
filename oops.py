def sum(n):
    if n == 1 or n == 0:
        return n
    else:
        return sum(n-1)+n
print(sum(194))

def fact(v):
    if v == 1 or v == 0:
        return v
    else:
        return fact(v-1)*v
print(fact(10))

