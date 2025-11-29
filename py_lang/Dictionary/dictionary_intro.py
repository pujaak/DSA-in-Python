info = {'name':'Amy', 'age':20, 'eligible' : True, 'id' : '007' }
print(info.keys())
print(info.values())

print(info['name'])
print(info.get('name'))
print(info.get('school'))
print(info.get('school', 0))

# print(info['school'])
try:
    print(info['school'])
except Exception as e:
    print(f"Error: KeyError: {e}")

print(info.items())
print()
for k, val in info.items():
    print(k, ":", val)