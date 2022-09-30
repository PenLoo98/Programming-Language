# https://codingdojang.com/scode/473

# 00:00~23:59 하루 중
# 3이 표시되는 경우 표현

hour1 = 0
hour10 = 0
minute1 = 0
minute10 = 0

#  3이 표시되는 시간이 몇'초' 인지 카운트
count_second = 0

# 시간 : 분 형식으로 표현
for i in range(24):
    for j in range(60):
            print('%d%d : %d%d' % (hour10, hour1, minute10, minute1))
            minute1 += 1
            if minute1 == 10:
                minute1 = 0
                minute10 += 1
            if (minute10 == 6) and (minute1 == 0):
                minute10 = 0
                minute1 = 0
                hour1 += 1
            if hour1 == 10:
                hour1 = 0
                hour10 += 1
            # 시간, 분 자리에 3이 하나라도 있으면 카운트를 합니다
            if hour1 == 3 or minute10 == 3 or minute1 == 3:
                count_second += 60

print(count_second)



