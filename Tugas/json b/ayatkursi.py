import requests

# API untuk teks Arab
url_arab = "https://api.alquran.cloud/v1/ayah/2:255/quran-simple"
# API untuk terjemahan Inggris
url_en = "https://api.alquran.cloud/v1/ayah/2:255/en.asad"

# Ambil data dari API
data_arab = requests.get(url_arab).json()
data_en = requests.get(url_en).json()

# Ambil isi teks & nama surah
ayat_arab = data_arab["data"]["text"]
surah_name = data_arab["data"]["surah"]["englishName"]

ayat_en = data_en["data"]["text"]

# Print hasil
print(f"Ayat Al-Kursi (2:255) - Arab:\n{ayat_arab}\n")
print(f"Terjemah (EN):\n{ayat_en}")