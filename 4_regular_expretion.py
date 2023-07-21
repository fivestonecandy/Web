#정규식) 주민번호, 차량번호 등 일정한 형태의 수열 식별하는 정규식 코드
#정규식 예제) 뺑소니, 신고 후 도주차량 목격 이후 경찰에 진술하는 상황, 네자리 글자 중 ca?e만 기억남 ex) care, cafe, cave
import re

p = re.compile("ca.e") #pattern = recompile("정규식") 탐색
# . (ca.e): 하나의 문자 의미, case, cafe O | caffe, casse X
# ^ (^de): 문자열의 시작을 의미, desk, deth, destination O | fesk, feth X
# $ (se$): 문자열의 끝을 의미, base, case O | bace, teth X

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지않음")
m = p.match("cafe")
print_match(m)
