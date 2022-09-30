#  https://codingdojang.com/scode/490

# 가성비 = 성능 / 가격
# [방향]
# 원래 부품의 가성비를 구하고
# 나머지 부품의 가성비를 계산 후 원래 부품의 가성비와 비교 후
# 높으면 추가하고 아니면 빼는 식으로 프로그래밍 하면 되겠다

a = [150, 10]
b = [30, 3]
c = [70, 3]
d = [15, 3]
e = [40, 3]
f = [65, 3]

ppp_a = a[0]/a[1]
grouping = [b, c, d, e, f]
sum_price = 150
sum_performance = 10

# 원래 부품 가성비보다 좋은 나머지 부품만 골라 더해준다
for i in grouping:
    if ppp_a < (i[0]/i[1]):
        sum_price += i[0]
        sum_performance += i[1]
    else:
        pass

print(sum_price//sum_performance)

