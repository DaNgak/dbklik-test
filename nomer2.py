import requests, os, csv
from bs4 import BeautifulSoup

# URL dari halaman Wikipedia yang berisi daftar kabupaten di Indonesia
url = 'https://id.wikipedia.org/wiki/Daftar_kabupaten_di_Indonesia'

# Melakukan permintaan GET ke URL
response = requests.get(url)

# Parse konten halaman dengan BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Menemukan tabel yang berisi daftar kabupaten
table = soup.find('table', {'class': 'wikitable'})

# List untuk menyimpan data kabupaten
kabupaten_list = []

# Mendapatkan semua baris di tabel
rows = table.find_all('tr')

for row in rows[1:]:  # Lewati header
    cols = row.find_all('td')
    if len(cols) > 3:  # Pastikan ada cukup kolom
        kabupaten = cols[2].text.strip()
        provinsi = cols[3].text.strip()
        kabupaten_list.append([kabupaten, provinsi])


# Buatkan folder result jika belum ada
if not os.path.exists('result'):
    os.makedirs('result')

# Menulis data kabupaten ke file CSV
with open('result/daftar_kabupaten.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Kabupaten', 'Provinsi'])
    writer.writerows(kabupaten_list)

print("Data kabupaten berhasil disimpan ke daftar_kabupaten.csv")
