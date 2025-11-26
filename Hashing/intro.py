# lst = [1, 2, 3, 2, 2, 1, 4, 3, 2, 10]
# user input:
lst = []
size = int(input("Enter length of list: "))
print("Enter the elements of list: ")
for i in range(size):
    lst.append(int(input()))
# print(lst)
hmap = dict()
for i in lst:
    if i in hmap:
        hmap[i] += 1
    else:
        hmap[i] = 1
# print(hmap)
count = int(input("Enter the number of elements to check their frequency in the list: "))
for i in range(count):
    n = int(input("Enter the number to check its frequency in the list: "))
    print(hmap.get(n,0))