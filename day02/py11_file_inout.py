# 파일 입출력

# a(추가), r(읽기), w(쓰기)

# 쓰기
f = open('./day02/testfile.txt', mode='w', encoding='utf-8') # open -> 파일 생성
# 아무것도 안함
f.write('저는 한국사람입니다. \n')
f.write('남자입니다. \n')
f.close() # open 함수로 생성된 객체 제거. 오류 방지용

print('텍스트 파일이 생성되었습니다.')

# 읽기
f = open('./day02/testfile.txt', mode='r', encoding='utf-8')

while True: # 무한반복
    line = f.readline() # 한줄씩 읽고
    if not line: break # 읽을 줄이 없으면 반복문 탈출

    print(line)

f.close() 