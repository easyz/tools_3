array = []
for i in range(1, 10):
    array.append(10 - i)
array.sort(lambda(lhs, rhs): return lhs-rhs)
print(array)