# 주소록 프로그램

import contact
import os # 운영체제에서 사용할 기능 모듈

# 4. 연락처를 입력받는 함수
def set_address():
    try:
        name, phone, email, addr = input('정보 입력(이름, 전화번호, 이메일, 주소 순) : ').split(',')
        # print(name, phone, email, addr)
        # 7. contact 객체 생성, 리턴
        address = contact.Contact(name, phone, email, addr)
        return address # Contact 객체가 리턴
    except ValueError:
        print('데이터를 정확히 입력하세요')
        return None # 아무 것도 아닌 것

# 10. 연락처 출력
def get_address(lst_contact):
    for item in lst_contact:
        print(item)

# 12. 연락처 삭제
# 16. 연락처 삭제 함수 변경. 삭제 여부 리턴
def del_address(lst_contact, name):
    result = False # 아무것도 삭제 안했음
    for i, item in enumerate(lst_contact): # 각 객체에 번호를 매겨주는 클래스
        if item.isNameExist(name):
            del lst_contact[i] # del은 메모리에서 완전 삭제
            result = True # 삭제했음

    return result # 삭제 여부 리턴

# 8. 콘솔 화면 클리어 함수
def clear_console():
    command = 'clear' # LINUX, UNIX 클리어 명령어
    if os.name in ('nt', 'dos'): # 운영체제가 윈도우라면
        command = 'cls' # Windows 클리어 명령어

    os.system(command) # 콘솔에 명령어 실행

# 14. 파일DB 저장함수
def save_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='w', encoding='utf-8')
    for item in lst_contact:
        f.write(item.getName() + '/')
        f.write(item.getPhone() + '/')
        f.write(item.getEmail() + '/')
        f.write(item.getAddr() + '\n')

    f.close() # 파일을 열었으면 끝난 후 파일을 반드시 닫아줘야함. 안 닫으면 계속 열린 채로 메모리 차지하고 있음

# 15. 파일DB 로드 함수
def load_contact(lst_contact):
    f = open('./day03/address_db.txt', mode='r', encoding='utf-8')
    while True:
        line = f.readline() # 이름/번호/메일/주소 읽어옴
        if not line:
            break # 줄에 아무 글도 없으면 빠져나감
        
        # 2025.01.16. 15:52 talCSHN.
        # \n으로 오류 발생. \n을 리스트 저장 전에 삭제해야함
        lines = line.replace('\n','').split('/') # lines는 4개의 문자열을 가지는 리스트가 됨
        # lines = ['박관호', '6849', 'qqqq@gmail.com', '부산']
        # lines[0] == '박관호'
        address = contact.Contact(name=lines[0], phone=lines[1], email=lines[2], addr=lines[3])
        lst_contact.append(address)

    f.close()

# 5. 프로그램 실행 함수
def run():
    # 9. 주소 정보들을 담을 변수(리스트)
    lst_contact = [] # 빈 리스트
    load_contact(lst_contact)

    # set_address()
    clear_console() # 화면 클리어
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: # 연락처 추가
            info = set_address()

            if info is None:
                pass
            else:
                lst_contact.append(info) # 9. 주소정보 담기
                print('추가되었습니다.')

            input() # 단순 입력 대기

        elif sel_menu == 2: # 연락처 출력
            get_address(lst_contact)
            input()

        elif sel_menu == 3: # 연락처 삭제
            name = input('삭제할 이름 입력: ') # 12. 연락처 삭제
            res = del_address(lst_contact, name)
            if res == True:
                print('삭제되었습니다')
            else:
                print('삭제할 데이터가 없습니다.')

            input() # 단순 입력 대기

        elif sel_menu == 4: # 종료
            save_contact(lst_contact)
            break # 프로그램 종료
        else:
            pass

        clear_console()

# 6. 메뉴 구성
def get_menu():
    str_menu = ('주소록 프로그램 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n' 
                '4. 종료\n')
    print(str_menu)

    # 예외처리 try - except - (finally) 키워드 사용
    try:
        menu_num = int(input('메뉴 입력: ')) # 숫자를 표현하는 문자열
    except Exception:
        print('예외발생')
        menu_num = 0 # 메뉴와 관계 없는 숫자
    return menu_num # 문자열(1~4)을 정수로 변환

# 프로그램 시작하려면 함수가 정의 되어 있어야 하기 때문에 함수 정의가 1번 위에 있음
# 1. 프로그램 시작
if __name__ == '__main__':
    # pass # pass는 if, for, while, 함수 등에서 오류를 없애는 방법
    # print('주소록 프로그램')
    # 3. 클래스 실행 - 객체를 생성
    # first = contact.Contact('박관호', '010-2310-6849', 'yujakinasakoon@gmail.com', '울산')
    # print(first)
    run() # 제일 처음 실행되는 함수

