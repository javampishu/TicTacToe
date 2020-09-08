line = input().split()
number = input()
order = 0
position = []

for i in line:
    if i == number:
        position.append(str(order))
    order += 1

if len(position) > 0:
    print(" ".join(position))
else:
    print("not found")
