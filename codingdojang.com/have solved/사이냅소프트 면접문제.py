# https://codingdojang.com/scode/410

information = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

# 1. 김씨와 이씨는 각각 몇 명 인가요?
# 2. "이재영"이란 이름이 몇 번 반복되나요?
# 3. 중복을 제거한 이름을 출력하세요.
# 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.

KimC = 0
LeeC = 0
jyLee = 0
names = information.split(",")
name_filter = []
for i in names:
    lastname = i[0]
    if i[0] == "김":
        KimC += 1
    elif i[0] == "이":
        LeeC += 1
    if i == "이재영":
        jyLee += 1
    if i in name_filter:
        continue
    name_filter += [i]

name_filter.sort()

print("김씨는 %s명입니다" % KimC)
print("이씨는 %s명입니다" % LeeC)
print("이재영이란 이름은 %d번 반복됩니다" % jyLee)
print(name_filter)
