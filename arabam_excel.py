import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook

# Excel kitabı tanımlama
kitap = Workbook()

# Aktif çalışma sayfasını seçme
sayfa = kitap.active

url = "https://www.arabam.com/ikinci-el/otomobil?take=50"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

markamodel = soup.find_all("td", {"class", "listing-modelname pr"})
yil = soup.find_all("td", {"class", "listing-text pl8 pr8 tac pr"})
fiyat = soup.find_all("td", {"class", "pl8 pr8 tac pr"})
yil2 = soup.find_all("td", {"class", "fade - out - content - wrapper"})
arabalink = soup.find_all("a", {"class", "listing-text-new word-break val-middle color-black2018"})

linksayac = 1



k = 0
l = 0

for b in markamodel:




    b = b.text


    # Belirli hücrelere veri girme
    sayfa['A1'] = "MARKA"
    sayfa['B1'] = "YIL"
    sayfa['C1'] = "KM"
    sayfa['D1'] = "RENK"
    sayfa['E1'] = "İL"
    sayfa['F1'] = "FİYAT"
    sayfa['G1'] = "LİNK"
    al = arabalink[l].get("href")


    sayfa.append(
        [b, yil[k].text, yil[k + 1].text, yil[k + 2].text, yil[k + 3].text.split(' ')[0], fiyat[l].text, al])

    k += 4
    l += 1

# Kitabı kaydetme
kitap.save("arabam.xlsx")

# Kitabı Kapat
kitap.close()










































# print(yil[4].text)
# print(yil[5].text)
# print(yil[6].text)
# print(yil[7].text)

# .replace("a","s"))
# print(fiyat[1].text)
#
# print("marka sayısı" + str(len(markamodel)))
# print("yıl sayısı" + str(len(yil) / 4))
# print("fiyat sayısı" + str(len(fiyat)))

#
# for b in yil:
#   b = b.text
#   print(b)
