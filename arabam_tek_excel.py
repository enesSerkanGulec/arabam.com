import requests

from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://www.arabam.com/ilan/galeriden-satilik-mercedes-benz-c-c-180-kompressor-blueefficiency-amg/cok-temiz-aractir-hatasiz/14065688"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi, "html.parser")

detaydeger = soup.find("div", {"class", "tab-item"})
a = soup.getText("div", {"class", "properties-container"})

print(a)
print(detaydeger)

# for x in detaydeger:
#     print(x)
#     print(x.text)

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
