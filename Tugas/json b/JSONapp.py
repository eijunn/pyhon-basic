import json

with open("JSON/tugasJSON.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("<<BUKU STORE OJO SAK PENAK dwe>>")
print("(udu warung e mbah mu)\n")
print("yg belum dikembaliin\n")

total_pinjam = 0
belum_kembali = 0


for anggota in data['anggota']:
    for buku in anggota['pinjam']:
        total_pinjam += 1 
        if not buku['kembali']:
            belum_kembali += 1
            print(f"->>{anggota['nama']:7} : {buku['judul']} ({buku['tanggal']})")

print(f"\nTotal yg njileh : {total_pinjam} | seng nyolong : {belum_kembali}")
























