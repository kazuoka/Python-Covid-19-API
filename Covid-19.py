import requests

''' response=requests.get("https://covid19.th-stat.com/api/open/today")
# print(response.json()) ดูข้อมูลทั้งหมด
data=response.json()
print("ติดเชื้อสะสม = ",data["Confirmed"])
print("หายแล้ว = ",data["Recovered"])
print("รักษาอยู่ใน รพ. = ",data["Hospitalized"])
print("เสียชีวิต = ",data["Deaths"]) ''' 

response=requests.get("https://covid19.th-stat.com/api/open/cases/sum")
data=response.json()
# print(data["Province"]) ดูข้อมูลทุกจังหวัด
for i,(k,v) in enumerate(data["Province"].items()):
    # print(i,k,v)
    print("จังหวัด = ",k ,"จำนวน = ",v)


