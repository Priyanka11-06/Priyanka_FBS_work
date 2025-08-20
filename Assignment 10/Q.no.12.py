# create three list of numbers, their squares and cube

num = int(input("Enter tha no of element"))
list1 = []
square = []
cube = []

for i in range(num):
    ele = int(input("Enter the element"))
    list1 = list1 + [ele]
    square = square + [ele*ele]
    cube = cube + [ele*ele*ele]

print(list1)
print(square)
print(cube)