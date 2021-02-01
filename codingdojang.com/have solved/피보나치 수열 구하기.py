# https://codingdojang.com/scode/461

# 1. 피보나치 수열 구함
# 2. 인풋 n 이하의 피보나치 수열 필터링

n = int(input("정수 n을 입력하시오\n:"))
fibo = [0, 1]

for i in range(0, 100):  # 피보나치 수열 만듦, 항 102개로 제한
    sum = fibo[i]+fibo[(i+1)]
    fibo += [sum]


under_N = []
for j in range(0, 102):  # n 이하의 숫자 필터링
    if n >= fibo[j]:
        under_N += [fibo[j]]


print(under_N)

