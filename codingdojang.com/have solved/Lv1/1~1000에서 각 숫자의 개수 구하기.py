#  https://codingdojang.com/scode/504

# 숫자의 개수를 세는 변수 생성
for j in range(10):
    globals()["cnt{}".format(j)] = 0

# 숫자의 각 자릿수로 쪼개고 갯수를 더함
for i in range(1, 1001):
    if 0 < i < 10:
        for num in range(10):
            if i == num:
                globals()["cnt{}".format(num)] += 1

    if 10 <= i < 100:
        for num in range(10):
            if i//10 == num:
                globals()["cnt{}".format(num)] += 1
            if i%10 == num:
                globals()["cnt{}".format(num)] += 1

    if 100 <= i < 1000:
        for num in range(10):
            if i//100 == num:
                globals()["cnt{}".format(num)] += 1
            if (i % 100) // 10 == num:
                globals()["cnt{}".format(num)] += 1
            if (i % 100) % 10 == num:
                globals()["cnt{}".format(num)] += 1

    if i == 1000:
        cnt1 += 1
        cnt0 += 3

for num in range(10):
    print("%d: %d개" % (num, globals()["cnt{}".format(num)]))