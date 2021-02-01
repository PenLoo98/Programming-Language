# https://codingdojang.com/scode/405
#   예상 해결방법
# 1. replace 함수
# 2. sys 함수
# 3. 정규 표현식

# 1. replace 함수
text = "code contents"
text.replace("\t", "\s\s\s\s")
print(text)

# 2. 정규식
# import re
# codetext = re.compile('.[\t].')
# codetext.sub('.[\s\s\s\s].', 'code')
