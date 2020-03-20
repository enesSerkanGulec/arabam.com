import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

# Excel kitabı tanımlama
kitap = Workbook()

# Aktif çalışma sayfasını seçme
sayfa = kitap.active

tabancalink = [
               "https://www.sarsilmaz.com/tr/katalog/urun/B6/4/4",
               "https://www.sarsilmaz.com/tr/katalog/urun/CM9/4/6",
               "https://www.sarsilmaz.com/tr/katalog/urun/CM9-GEN2/4/7",
               "https://www.sarsilmaz.com/tr/katalog/urun/ST9/4/8",
               "https://www.sarsilmaz.com/tr/katalog/urun/ST9-S-SS/4/111",
               "https://www.sarsilmaz.com/tr/katalog/urun/K11/4/103",
               "https://www.sarsilmaz.com/tr/katalog/urun/K10C/4/106",
               "https://www.sarsilmaz.com/tr/katalog/urun/K12/4/15"
               ]
# tabancalink.append("https://www.sarsilmaz.com/tr/katalog/urun/B6/4/4")

ozellik = list()
deger = list()


def silahbilgi(url):
    url = url

    response = requests.get(url)

    html_icerigi = response.content

    soup = BeautifulSoup(html_icerigi, "html.parser")

    bilgiler = soup.find_all("td")

    i = 0

    for b in bilgiler:
        b = b.text
        if i % 2 == 0:
            ozellik.append(b)
        else:
            deger.append(b)
        i += 1

    for o, d in zip(ozellik, deger):
        print(" {}  : {}".format(o, d))

    # Belirli hücrelere veri girme
    sayfa['A1'] = ozellik[0]
    sayfa['B1'] = ozellik[1]
    sayfa['C1'] = ozellik[2]
    sayfa['D1'] = ozellik[3]
    sayfa['E1'] = ozellik[4]
    sayfa['F1'] = ozellik[5]
    sayfa['G1'] = ozellik[6]
    if len(ozellik) >= 8:
        sayfa['H1'] = ozellik[7]
    if len(ozellik) >= 9:
        sayfa['I1'] = ozellik[8]
    if len(ozellik) >= 10:
        sayfa['J1'] = ozellik[9]


x = 0

for i in range(0, len(tabancalink)):
    silahbilgi(tabancalink[x])
    if len(deger) >= 10:
        sayfa.append(
            [deger[0], deger[1], deger[2], deger[3], deger[4], deger[5], deger[6], deger[7], deger[8], deger[9]])


    elif len(deger) >= 9:
        sayfa.append([deger[0], deger[1], deger[2], deger[3], deger[4], deger[5], deger[6], deger[7], deger[8]])


    elif len(deger) >= 8:
        sayfa.append([deger[0], deger[1], deger[2], deger[3], deger[4], deger[5], deger[6], deger[7]])

    deger.clear()
    x += 1

    # silahbilgi(tabancalink[1])
    # sayfa.append([deger[0], deger[1], deger[2], deger[3], deger[4], deger[5], deger[6], deger[7], deger[8], deger[9]])
# Kitabı kaydetme
kitap.save("tabancabilgi.xlsx")

# Kitabı Kapat
kitap.close()
