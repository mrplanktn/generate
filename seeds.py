import random

# Baca kata dari file txt
with open("kata.txt", "r") as file:
    kumpulan_kata = [line.strip() for line in file if line.strip()]

# Jumlah seed phrase yang ingin digenerate
jumlah_generate = 10
jumlah_kata_per_seed = 12

# Validasi
if len(kumpulan_kata) < jumlah_kata_per_seed:
    raise ValueError("Jumlah kata dalam kata.txt kurang dari 12.")

# Proses generate
print(f"Menghasilkan {jumlah_generate} seed phrase, masing-masing 12 kata:\n")

for i in range(jumlah_generate):
    hasil_kata = random.sample(kumpulan_kata, jumlah_kata_per_seed)
    print(f"{i + 1}. {' '.join(hasil_kata)}")
