dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys = set(dct.keys())
print(keys)
vals = set(dct.values())
print(vals)
combined = keys | vals
print(combined)