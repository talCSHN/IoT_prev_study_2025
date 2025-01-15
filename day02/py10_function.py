# 함수
# 수학의 함수와 동일

print('함수') # 내장(built-in)함수

# 함수 정의(delfinition)
# 사용자 정의 함수
# 같은 로직을 두 번 이상 쓸 경우 사용자 정의 함수 만들어야함

def add(a, b):
    result = a + b
    return result # return -> 결과 돌려줌(반환)

def minus(a, b):
    result = a - b
    return result

def multi(a, b):
    result = a * b
    print('곱은 ->', result)
    # return 다음에 값이 없으면 아무 값도 반환 안함 -> return 생략함

def divide():
    result = 100/4
    print('나누기 결과는', result)

x = 11
y = 22
z = add(x, y)
print('합의 결과는', z)

x = 101
y = 203
print('합의 결과는', add(x, y))

x = 35
y = 15
print('차의 결과는', minus(x, y))

x = 30
y = 10
multi(x, y)
# z = multi(x, y)
# print(z)

x = 100
y = 5
divide()

#  내장함수 - 자주 사용할 것 같은 함수를 미리 만들어둔 것
# 대부분 stdlib(standard library)에 들어있음
print(max(1, 3, 7, 15))
print(min(1, 3, 7, 15))
print(abs(-5)) # 절대값
print(2 ** 10)
print(pow(2, 10)) # 거듭제곱


