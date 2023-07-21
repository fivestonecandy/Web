import requests

res = requests.get("http://google.com")
res.raise_for_status() #올바른 코드, html문서를 가져온거라면 문제 없이 진행하고, 아니라면 오류 발생, 이후의 동작안하고 코드 종료시킨다.
print("웹 스크래핑을 진행합니다.")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf-8") as f:
    f.write(res.text)



#if res.status_code == requests.codes.ok:
#    print("정상입니다.")
#else:
#    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

#//*[@id="container"]/div[3]/div[2]/div[2]