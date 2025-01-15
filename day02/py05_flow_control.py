# 흐름제어
# if, for, while

## int() - 정수화, float() - 실수화, double() - 복소수화
age = int(input('나이를 입려하세요 > ')) # age에 문자열이 입력됨. 30 입력 -> '30'

## if문을 시작하겠다를 의미하는 마지막 단어 -> :
if age > 19 and age < 61:
    # if문이 참(True)이면 아래의 구문을 실행
    # if문(흐름제어) 안으로 들어옴
    print('술 사가세요')
elif age > 60: # 다른 조건이 필요할 때 (else if)
    print('술 그만드세요')
else:
    # if문이 거짓(False)이면 아래의 구문을 실행
    print('야, 집에 가')