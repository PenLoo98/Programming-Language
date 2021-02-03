# https://codingdojang.com/scode/414

numbers = [-1, 1, 3, -2, 2]
plusNums = []
minusNums = []

for i in numbers:
    if i > 0:
        plusNums += [i]
    elif i < 0:
        minusNums += [i]

result = minusNums + plusNums

print(result)