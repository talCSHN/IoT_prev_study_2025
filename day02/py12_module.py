# 모듈/패키지

import py10_function as calc
import math
import requests
calc.multi(10, 4) # 콘솔에 py10의 모든 코드 결과값이 나옴. -> multi부분 말고 전부 주석처리해야 곱한 값만 나옴



result = math.pow(2, 10)
print(result)

result = math.log2(4)
print(result)

# 패키지 - 모듈들을 모아둔 디렉토리(폴더)
# pip install requests

res = requests.get('https://www.naver.com') # 네이버 사이트 접속
print(res.status_code) # 200

print(res.content) # 웹스크래핑
