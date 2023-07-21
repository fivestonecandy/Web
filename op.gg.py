    # 라이브러리 준비하기
import csv
import requests
from bs4 import BeautifulSoup



'''# 엑셀 파일로 저장하기
filename = "챔피언 순위.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
columns_name = ["순위", "챔피언"] # 컬럼 속성명 만들기
writer.writerow(columns_name)
'''
# 엑셀 파일로 저장하기
filename = "챔피언 티어.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_name = ["순위", "챔피언", "티어"] # 컬럼 속성명 만들기

writer.writerow(columns_name)
print("원하는 라인을 적으세요")
line = input()


# 웹서버에 요청하기
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

url ="https://www.op.gg/champions?region=global&tier=platinum_plus&position="+line
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


#table = soup.html.body.table
#p1 = table.strong #soup.html.body.table.strong.span.#text


'''for i in soup.find_all('strong'):
    print(i.string)
for i in soup.find_all('p'):
    print(i.get_text())'''
    
'''for i in soup.find_all('strong'): 
    champion = i.string
    data = [{n}, champion]
    writer.writerow(data)

    n +=1'''

'''for i in champ:
    name = i.text
    data = [{n}, name]
    writer.writerow(data)
    
    n+=1
    

    writer.writerow(data)'''
    
champ = soup.find_all('td', class_='css-cym2o0 e1oulx2j6')
clas = soup.find_all('td', class_='css-ew1afn e1oulx2j3') #soup객체에서 'td'태그의 해당 클래스를 모두 찾는다.
tier_list = []
m = 0
n = 1
for x in clas:
        tier = x.text
        tier_list.append(tier)
print(tier_list)
for i in champ:
    name = i.text
    print(f"{n}위 {name} {tier_list[m]}티어")
    data = [{n}, name, tier_list[m]]
    writer.writerow(data)
    n+=1
    m+=1