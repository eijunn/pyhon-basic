print("MATERI 8 - FUNCTION DASAR")
print("==========================")

#srtuktur fungsi dasar tanpa parameter
def halo_dunia():
    print("hello world")
    print("hallo dunia")

# cara akses function , sertakan nama dan () -nyaa
halo_dunia()
# fungsi dengan parameter (variabel fungsi)
def sapa_sapa_gan(nama):
    print("hallow", nama, "selamat datang di alam baka")

sapa_sapa_gan("yatno")

def siapa_waifumu(waifu):
    print("ini", waifu, "istri gweeehhh")
siapa_waifumu("mahiru-shinaa")



def rumus_luas_segi_tiga(alas, tinggi):
    print("alas", alas)
    print("tinggi", tinggi)
    rumusan = 1/2 * (alas * tinggi)
    print("hasil:", rumusan)

rumus_luas_segi_tiga(20, 30)

# SELAU PERHATIKAN JARAK INDESASI KARENA HAL ITU CUKUP KRUSIAL YG DAPAT MEMBUAT ERROR


def filter_teman_toxix(nama, sifat):
    #ciri-ciri toxic
    sifat_toxic = [
     "julid",
     "baperan",
     "manipulatif", 
     "drama",
     "sombong"   
    ]

    # deteksi parameter sifat toxic dari pada parameter sifat
    if any(kata in sifat for kata in sifat_toxic):
        print(nama, "itu org gabaek jgn ditemenin")
    else:
        print(nama, "oohhhh dia org baik kok gpp")



filter_teman_toxix("ali", "baek wae")
filter_teman_toxix("yatno", "julid baperan drama sombong")









