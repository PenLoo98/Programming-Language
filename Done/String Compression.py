# q14
# 1. 문자 입력
# 2. 연속반복 횟수 카운트
#    for + 이전 문자열 저장 +현재 문자열 저장 비교 + 카운트1
# 3. 숫자+반복횟수로 변환
# 4. 출력

a = 'aaabbccd'
b = []
global bef
global count
bef = a[0]
count = 0


for i, word in enumerate(a):
    aft = word
    while bef == aft:
        count += 1
        if i == len(a)-1:
            b.append(bef+'%d' % count)
        break
    if bef != aft:
        b.append(bef+'%d' % count)
        count = 1
        if i == len(a) - 1:
            b.append(aft+'1')
    bef = aft


print(''.join(b))

