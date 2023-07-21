import requests
res = requests.get("http://google.com")
print("응답코드 :", res.status_code)
#res = requests

res.raise_for_status()
print("웹 스크래핑을 진행합니다.")



with open("mygogle.html", "w", encoding="utf8") as f: #with open(파일 , 쓰기모드, 인코딩형식)
    
    
    
    
    


#if res.status_code == requests.codes.ok:
#    print("정상입니다.")
#else:
#    print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

#//*[@id="container"]/div[3]/div[2]/div[2]