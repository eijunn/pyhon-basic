print("============= TUGAS 2 ==============")
print("====================================")
jadwal_piket = ["yatno", "yatni", "yatnep", "tono", "feritot"]

print("jadwal piket hari ini adalah:")

for item in jadwal_piket:
    print(f"- {item}")


print("==================================")
print("<<<<<<RUKUN ISLAM>>>>>>>>>")

rukun_islam = ["syahadat", "sholat", "zakat", "puasa", "haji"]

print("rukun islam diantara berikut:")

for i in range(len(rukun_islam)):
    print(f"{i + 1}. {rukun_islam[1]}")

print("==========================================")
print("<<<<<<<<<KUMPULAN KITAB>>>>>>>>>>>>>")
kitab_yg_dipelajari = ["fiqh", "tauhid", "nahwu", "tajwid", "IT"]

print("kitab-kitab yg kita pelajari:")

for i in kitab_yg_dipelajari:
    print(f">> {i}")
print("======<<<<<<>>>>>=========")
print("<<<<<BIODATA GUA NIH>>>>>>>")
biodata_gua = {
    'nama': 'evandra ismail', 'kelas': 'X', 'jumlah hafalan': 18
}
for key, value in biodata_gua.items():
    print(f"{key}:{value}")





