from TugasOOP import produk

jumlah_produk = int(input("masukkan jumlah produk : "))

total_seluruh = 0
p_objek = None  

for i in range(jumlah_produk):
    print(f"\nProduk {i + 1}")
    nama = input("Nama : ")
    harga = int(input("Harga : "))
    jumlah = int(input("Jumlah : "))

    p_objek = produk(nama, harga)
    
    subtotal = p_objek.hitung_total(jumlah)
    total_seluruh += subtotal
    
    print("Total :", subtotal)

diskon = p_objek.hitung_diskon(total_seluruh) if p_objek else 0
total_bayar = total_seluruh - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian: Rp{int(total_seluruh)}")
print(f"Diskon 5%      : Rp{int(diskon)}")
print(f"Total Bayar    : Rp{int(total_bayar)}")