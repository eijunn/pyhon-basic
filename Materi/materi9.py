print("MATERI 9 - FUNCTION PTYHON DASAR")
print("================================")

# BELAJAR  LAMBDA GESS

waifu = lambda nama: print(f"hello {nama} mau ga jadi istri ku??")

waifu("mahiru")
print("mahiru: ohhh mau dong eivan kun wkwkwkwk")

# KALAU UNTUK DEF DAN LAMBDA TDK PERLU PRINT CUKUP PANGGIL SAJA VARIABLE NYA...
# SEKIAN THX

print("<-=LATIHAN LAMBDA=->")

#  map untuk mentranformasi data

nilai_string = "1000"
nilai_integer = int(nilai_string)
kalikan_dua_salah = nilai_string * 5
kalikan_dua_bener = nilai_integer * 5
print(kalikan_dua_bener, kalikan_dua_salah)

nilai_mentah = [1.9, 2.5, 4.9, 8.7, 9,1]
nilai_kali_seratus = map(lambda nilai: nilai * 100, nilai_mentah)
# konfersi map objek menjadi list
list_nilai_kali_seratus = list(nilai_kali_seratus)
print(f"nilai mentahan{nilai_mentah}")
print(f"nilai x 100{nilai_kali_seratus}")

print("====sorted=====")

daftar_siswa = [
    {"nama": "evan", "angka": 100},
    {"nama": "Aan", "angka": 69},
    {"nama": "akbar", "angka": 80}
]




print("FILTER")








































