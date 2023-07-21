# 라이브러리 준비하기
import csv
import requests
from bs4 import BeautifulSoup
import os
os.system('pause')
def clear_console():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
#사용자 요청 확인
while 1 :
    clear_console()
    print("원하는 라인을 적으세요.","ex) top, mid, jungle, adc, support, exit",)
    line = input()
    if line == "exit" :
        print("종료합니다.")
        break
    
    

    # 웹서버에 요청하기
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    url ="https://www.op.gg/champions?region=global&tier=platinum_plus&position="+line
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    champ = soup.find_all('td', class_='css-cym2o0 e1oulx2j6')
    clas = soup.find_all('td', class_='css-ew1afn e1oulx2j3') #soup객체에서 'td'태그의 해당 클래스를 모두 찾는다.
    tier_list = []
    m = 0
    n = 1
    for x in clas:
            tier = x.text
            tier_list.append(tier)
    for i in champ:
        name = i.text
        print(f"{n}위 {name} {tier_list[m]}티어")
        n+=1
        m+=1
    os.system('pause')