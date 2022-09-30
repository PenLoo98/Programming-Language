# https://codingdojang.com/scode/488

# 0~9까지의 문자로 된 숫자를 입력 받았을 때, 이 입력 값이 0~9까지의 숫자가 각각 한 번 씩만 사용된 것인지 확인하는 함수를 구하시오.
# sample inputs: 0123456789 01234 01234567890 6789012345 012322456789
# sample outputs: true false false true false


nums = input("숫자를 입력하시오 \n:").split(" ")

for i in nums:
    if len(i) != 10:  # 숫자의 길이가 10 아니면
        print("false", end=" ")
        continue
    setnums = []
    setnums += set(i)
    if (len(setnums) == len(i)):  # 중복이 없다면
        print("true", end=" ")
    else:
        print("false", end=" ")


