# https://codingdojang.com/scode/442

# 내심 개념 이용해야할듯

import math
a, b, c = map(float, input("삼각형의 세 변을 입력하시오(띄워쓰기로 구분)\n").split(" "))
# a = 12.0
# b = 12.0
# c = 8.0

s = 0.5*(a+b+c)
# 삼각형 넓이: 내접원 반지름으로 구한 넓이 = 헤론 공식으로 구한 삼각형 넓이
# s * r = math.sqrt((s(s-a)(s-b)(s-c)))
r = (math.sqrt(s*(s-a)*(s-b)*(s-c)))/s

print("The radius of the round table is: %.3f" % r)
