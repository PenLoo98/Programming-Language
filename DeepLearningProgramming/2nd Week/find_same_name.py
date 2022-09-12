def find_same_name(a):
 n=len(a) # 리스트의 자료 개수를 n에 저장
 result = set() # 결과를 저장할 빈 집합
 for i in range(0, n-1): # 0 부터 n-2 까지 반복
  for j in range(i+1, n): # i+1 부터 n-1 까지 반복
   return result
if a[i] == a[j]: # 이름이 같으면
 result.add(a[i]) # 찾은 이름을 result에 추가
 name = ["Tom", "Jerry", "Mike", "Tom"] # 대소문자 유의: 파이썬은 대소문자를 구분함
 print(find_same_name(name))
 name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
 print(find_same_name(name2))