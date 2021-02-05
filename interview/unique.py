seen = set()
a = [1, 2, 1, 3, 3]
uniq = [x for x in a if x not in seen and not seen.add(x)]


print(uniq)