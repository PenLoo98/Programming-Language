#q13
# def DashInsert(a):
a = input()  # 1. 숫자로 구성된 문자열 입력
b = []
for i in a:
    b += [int(i)]

global count
global index_count
count = 0
index_count = 1

if b[0] % 2 == 0:
    pass  # count = 0
elif b[0] % 2 == 1:
    count = 1
b[0] = str(b[0])

for j in b[1:]:
    if (count == 1) and (j % 2 == 1):  # 홀홀
        b[index_count] = "-%d" % j  # -삽입
    elif (count == 1) and (j % 2 == 0):  # 홀짝
        count -= 1
        b[index_count] = str(j)
    elif (count == 0) and (j % 2 == 1):  # 짝홀
        count += 1
        b[index_count] = str(j)
    elif (count == 0) and (j % 2 == 0):  # 짝짝
        b[index_count] = "*%d" % j  # *삽입
    index_count += 1


c = list(reversed(b))
d = ""
while c:
    d += c.pop()

print(d)