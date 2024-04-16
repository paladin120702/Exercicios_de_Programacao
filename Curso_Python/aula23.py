from itertools import zip_longest

l1 = [1, 2, 3, 4, 5]
l2= [1, 2, 3, 4, 5, 6, 7]

lista = [x + y for x, y in zip_longest(l1, l2, fillvalue=0)]
print(lista)