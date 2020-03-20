from openpyxl import Workbook
# Excel kitabı tanımlama
kitap = Workbook()

# Aktif çalışma sayfasını seçme
sayfa = kitap.active

# Belirli hücrelere veri girme
sayfa['A1'] = "İsim"
sayfa['B1'] = "Soyisim"
sayfa['C1'] = "Adres"
sayfa['D1'] = "Telefon"

# Satırdaki hücrelere veri girme
sayfa.append(["Ufuk", "Temir", "Osmanlı Mah. Selçuklu Cad. No:1", "0599 811 44 55"])

# Kitabı kaydetme
kitap.save("dosya2.xlsx")

# Kitabı Kapat
kitap.close()