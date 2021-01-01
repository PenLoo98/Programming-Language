# 8장 문제
# Q10

#1. 클래스 정의
#2. 합계/평균 함수 정의
#3. 출력


class Calculator:
    def __init__(self, num):
        self.num = num


    def sum(self):
        S = 0
        for i in self.num:
            S += i
        return S


    def avg(self):
        sum= self.sum()
        return sum/len(self.num)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())
cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())

