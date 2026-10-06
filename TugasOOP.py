class produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info(self):
        print('nama :', self.nama)
        print('harga :', self.harga)

    def hitung_total(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total_seluruh):
        if total_seluruh > 5000:
            return total_seluruh * 0.05
        return 0