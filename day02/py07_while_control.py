# while문
# for문과 동일

loop = 10
while loop >= 0: #loop변수값이 0보다 큰 동안
    print(loop, end='\t')
    loop = loop - 1
print()

# 위의 while문과 같은 출력
for i in range(10, -1, -1):
    print(i, end='\t')

print()

# 무한 반복
num = 0
while True:
    print('Hello', num)
    num = num + 1