import json
 

# Buka file JSON
with open("JSON/data_santri.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Akses data
print("Kelas:", data["kelas"])
print("Daftar Santri:")

for santri in data["santri"]:
    print(f"- hafalan pekan ini:{santri['nama']} {santri['hafalan']})")


with open("JSON/alquran.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    print("code:", data['code'])
    print("status:", data['status'])

for surah in data["data"][:10]:
    print(f"{surah['number']}. {surah['englishName']} ({surah['englishNameTranslation']})")
    print(f"   Ayat: {surah['numberOfAyahs']}, Tipe: {surah['revelationType']}")
    print(f"   Arab: {surah['name']}\n")


