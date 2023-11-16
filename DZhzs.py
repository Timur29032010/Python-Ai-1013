result = []
def divider(a, b):
    if a < b:
        raise RuntimeError
    if b > 100:
        raise TypeError
    return a/b
data = {0: 2, 2: 5, "Y neznaiu": 0, 6: 0, []: 15, 8 : 4}
for key in data:
 print(result)