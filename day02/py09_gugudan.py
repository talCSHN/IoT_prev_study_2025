#  구구단 프로그램
# 2 x 1 = 2 ~ 9 x 9 = 81 까지

for i in range(2, 10):
    # print(i)
    for j in range(1, 10):
        if j == 9:
            break
        # print(i * j) - 값만 출력
        print(i, 'x', j, '=', i*j, end='\t')
    print()