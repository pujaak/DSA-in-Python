# 1. update()
print("# 1. update()")
marks1 = {'phy': 40, 'chem': 50, 'bio': 53}
marks2 = {'hist' : 65, 'geo': 71}
print(marks1)
marks1.update(marks2)
print(marks1)
marks1.update({'maths': 58, 'eng' : 90})
marks1.update({'comp' : 90})
print(marks1)

print()
# 2. clear()
print("# 2. clear()")
print(marks2)
marks2.clear()
print(marks2)

# 3. pop()
print()
print("# 3. pop()")
marks1.pop('chem')
print(marks1)

# 4. popitem()
print()
print("# 4. popitem()")
marks1.popitem()
print(marks1)

# 5. del
print()
print("# 5. del")
del marks1['geo']
print(marks1)

# deletes entire dictionary:
del marks1
try:
    print(marks1)
except Exception as e:
    print(f"Error: {e}")