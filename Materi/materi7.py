# set -> {} -> tidak berurutan, berubah, tidak duplikat
print("=======MATERI KELAS 7B============")
print("==============================")
game_azka = {"valorant", "dark soul", "genshin impact"}
game_evan = {"genshin impact", "mlbb"}
print("evans game: ", game_evan)
print("azuka games: ", game_azka)
# add untuk menambah item baru 
game_azka.add("zzz")
game_evan.add("gta 6")
# len () untuk mengitung jumlah item
print("azka ada: ", len(game_azka),"games:", game_azka)
print("evan ganteng ada: ", len(game_evan),"games:", game_evan)

# untuk menggabungkan 2 set berbeda  ----->>  union()
game_berdua = game_azka.union(game_evan)
total_game = len(game_berdua)
print("semua game ada:", total_game, "games: ", game_berdua)

# intersection () -> mencari yg kembar 
# difference () --> mencari yg beda 

game_kembar = game_azka.intersection(game_evan)
game_beda = game_azka.difference(game_evan)
total_game_kembar = len(game_kembar)
total_game_beda = len(game_beda)
print("game yg kembar: ", total_game_kembar, "games: ", game_kembar)
print("game yg beda: ", total_game_beda, "games: ", game_beda)


 # dictionary
 # beruruta sesuai key, berubah,  key tdk boleh duplikat!!

koleksi_anime = {
   "roshidere": "alya-kujou",
   "otonari": "mahiru",
   "waifu": {
      "gotoubun": "miku",
      "tonikaku": "stukasa"
   }
}

print("koleksi anime ku: ", koleksi_anime)
print("mc dan istri ku: ", koleksi_anime["roshidere"])

# menambah atau mengbah data dict
koleksi_anime["jujutsu"] = "yantoo"
koleksi_anime["tonikaku"] = "haru"
print("koleksi anime skrg:", koleksi_anime)


#














