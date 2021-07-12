import http.client 
import json
conn=http.client.HTTPSConnection("api.collectapi.com")
headers = { 
    'content-type':"application/json",
    'authorization': "apikey 0pCj9Y6DXQjZbcAX0RCHWV:4MTwI5X5jQaGNeXficnFcn"
}
il=input("il giriniz")
if il=="":
    print("İl alanını boş girdiniz varsayın Ankara ayarlandı")
    il=="Izm'r"
else:
    il=il.strip().capitalize()
ilce=input("ilçe giriniz")
if ilce=="":
    print("İçe alanını boş girdiniz varsayın Bergama ayarlandı")
    il=="Bergama"
else: 
    ilce=ilce.strip().capitalize()
print(il,ilce)
bilgi="/health/dutyPharmacy?ilce="+ilce+"&il="+il
conn.request("GET",bilgi,headers=headers)
res=conn.getresponse()
data=res.read()
veri=data.decode("utf-8")
json_veri=json.loads(veri)
if json_veri["success"]==True:
    bilgi=json_veri["result"][0]
    print("Eczane Adı: "+bilgi["name"]+"Adresi:"+bilgi["address"])
else:
    print("işlem başarısız")
