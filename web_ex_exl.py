import csv

filename = "고양이 장난감.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

columns_title = ["컬럼명1", "컬럼명2"]
writer.writerow(columns_title)

data = ["결과1", "결과2"] # [] 리스트 자료구
writer.writerow(data)