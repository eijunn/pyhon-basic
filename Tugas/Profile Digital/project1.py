

nama = input("masukan nama: ")
umur = int(input("umur: "))
kelas = input("masukan kelas: ")

cita_cita = input("masukan cita-cita anda: ")
waktu_belajar = input("lebih suka belajar pagi taua malam: ")

print("-----pilih hobi anda-----")
print("1. Gamer")
print("2. wibu")
print("3. k-popers")
print("4. anak konten")
print("5. anak nongki")
pilihan_hobi = input("masukan angka sebagai berikut: ")

hobi = ""
detail_hobi = ""

if pilihan_hobi == "1":
    hobi = "gamer"
    detail_hobi1 = input("game apa kesukaan mu?")
elif pilihan_hobi == "2":
    hobi = "wibu"
    detail_hobi2 = input("siapa waifumu?")
elif pilihan_hobi == "3":
    hobi = "K-popers"
    detail_hobi3 = input("siapa biasmu?")
elif pilihan_hobi == "4":
    hobi = "anak konten"
    detail_hobi4 = input("platform favoritmu? tiktok? youtube?")
elif pilihan_hobi == "5":
    hobi = "anak nongki"
    detail_hobi5 = input("nongkrong paling sering dimana??")
else:
    print("hobi tdk diketahui...")

tahun_sekarang = 2025
tahun_lahir = tahun_sekarang - umur

print("\n\t=======PROFIL DIGITAL OF ME==========")
print(f"\tNama: {nama}")
print(f"\tUmur: {umur} tahun")
print(f"\tkelas: {kelas}")
print(f"\tperkiraan tahun lahir {tahun_lahir}")
print(f"\tHobi: {hobi}")
print(f"\tdetail hobi: {detail_hobi} ")
print("\t=========SEKIAN DARI SAYA===========")

print("\n\t========TIPE DIGITAL============")

if pilihan_hobi == "1":
    print("\ttipe: gamer")
    print(f"\tgame kesukaanmu: {detail_hobi1}")
    print("komentar: waahh pasti pro player...")
elif pilihan_hobi == "2":
    print("\ttipe: wibu")
    print(f"\twaifu favorit: {detail_hobi2}")
    print("\tkomentar: keren lu kak kita satu bangsa!!!")
elif pilihan_hobi == "3":
    print("\ttipe: k-popers")
    print(f"\tbias kesukaan: {detail_hobi3}")
    print("\tkomentar: wah sorry ga minat....")
elif pilihan_hobi == "4":
    print("\ttipe: anak konten")
    print(f"\tplatform favorit: {detail_hobi4}")
    print("\tkomentar: yuk ngonten bareng...")
elif pilihan_hobi == "5":
    print("\ttipe: tukang nongki")
    print(f"\ttempat nongki favorit {detail_hobi5}")
    print("\tkomentar: nongki ae woi ngabisin uang tau....")


print("\n\t=======FUN CHECK=========")
teman_bau = input("\tteman sebelahmu bau ga?? \njawab iya/ga:")

if teman_bau == "iya":
    print("\tbeehhhhhh mau mati rasanya bangg...")
elif teman_bau == "ga":
    print("\tgatau nih tumben banget wangi hehe...")
