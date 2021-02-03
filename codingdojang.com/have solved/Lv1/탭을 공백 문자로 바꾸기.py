# https://codingdojang.com/scode/405

# 1. 파일 읽고 쓰기
before = open("C:/Users/sohnc/Desktop/tab.txt", 'r')
after = open("C:/Users/sohnc/Desktop/4space.txt", 'w')
    
tab_contents = before.readlines()

for i in tab_contents:
    j = str(i)
    k = j.replace("\t", "    ")
    after.write(k)

before.close()
after.close()


# 2. 정규식
# import re
# Tab = re.compile('[\t]')
# space = Tab.sub('    ', "\tTabCode")
# print(space)


