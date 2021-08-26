print("=======================*===================*======================")
print("Pengelompokan Usia Menggunakan System Fuzzy dari Nilai Keanggotaan")
print("--------------------Jenyta Primaranti 2020080381------------------")
print("=======================*===================*======================")

# Array dua dimensi
kelompok_umur = [[25,35,45,55,65],['MUDA','MUDA 0.5 & SETENGAH BAYA 0.5','SETENGAH BAYA','SETENGAH BAYA 0.5 & TUA 0.5','TUA ']]

umur = int(input("Masukkan umur anda : "))

if (umur in kelompok_umur[0]):
  # Pengulangan / loop
  for i in range(len(kelompok_umur[0])):
    if (umur==kelompok_umur[0][i]):
      print(f"\nAnda berusia {kelompok_umur[0][i]} tahun termasuk {kelompok_umur[1][i]}")
else:
  print("Umur yang anda masukan tidak ada dalam data")

