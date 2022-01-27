from bs4 import BeautifulSoup
import requests
import pandas as pd




#STUDI KASUS 6
#Serializing data HTML
from pandas import DataFrame

buildwithangga = requests.get("https://buildwithangga.com/catalog/code-courses")
buildwithangga = BeautifulSoup(buildwithangga.text, "html.parser")
judul_kursus_buildwithangga = buildwithangga.select(".course-name")
daftar_harga_buildwithangga = buildwithangga.select(".course-type span")

judul_kursus_buildwithangga = [judul.getText().strip('\n.').lstrip() for judul in judul_kursus_buildwithangga]
daftar_harga_buildwithangga = [int(harga.getText().strip('\nRp,').replace(',', '')) for harga in daftar_harga_buildwithangga]

daftarJudulDanHarga = list(zip(judul_kursus_buildwithangga, daftar_harga_buildwithangga))
pd.set_option('display.max_rows', None)
data = pd.DataFrame(daftarJudulDanHarga, columns=["Judul","Harga"])

print(data)

print('\n')


print("Urutkan judul kursus buildwithangga berdasarkan nama")
print(sorted(judul_kursus_buildwithangga))
termahal = lambda x : max(x)
print('\n')
print("Harga kursus yang paling mahal buildwithangga : Rp."+str(termahal(daftar_harga_buildwithangga))+"\n")






