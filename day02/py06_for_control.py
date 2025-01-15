# for문
# 프로그래밍의 꽃

# range(9) => 0,1,2,3,4,5,6,7,8
# print(range(9))

for i in range(9): # for문 흐름제어로 들어감
    print(i, end='\t') # end인자로 출력끝을 조정 \n, \t

# 1부터 10까지의 합 55
sum = 0
for i in range(1, 1001):
    sum = sum + i

print(sum)

sum = 0
for i in range(1, 10, 2):
    print(i)