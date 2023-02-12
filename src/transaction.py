try:
    # Import CSV untuk transfer order history ke text file .csv
    import csv
    # Import time untuk waktu transaksi
    import time
    # Import tabulate untuk mengindahkan format tampilan tabel
    from tabulate import tabulate
except ImportError:
    print("Module csv, time, and tabulate are required to run this program. Please install them and try again.")
    exit()


class Transaction:
    '''
    Class untuk melakukan transaksi dan menyimpan informasi transaksi.
    Attributes
    ---------------------------------------------------
    trnsct_id : int
        ID transaksi
    items : list
        Daftar item-item yang dibeli dalam suatu transaksi
    '''

    def __init__(self, trnsct_id):
        '''
       Constructor untuk membuat objek Transaction.
       Parameters
       ---------------------------------------------------
       trnsct_id : int
           ID transaksi
       '''
        self.trnsct_id = trnsct_id
        self.items = [ ]

    def add_item(self, item):
        '''
        Function add_item() merupakan function dari class Transaction yang berfungsi untuk menambahkan item/barang pada daftar item transaksi.
        function ini akan memeriksa apakah item tersebut sudah ada dalam daftar item transaksi, jika sudah maka jumlah item tersebut akan ditambah.
        Jika item tersebut belum ada dalam daftar item transaksi, maka item tersebut akan ditambahkan ke daftar item transaksi.

        Parameters
        ---------------------------------------------------
        item: list
            Berisi informasi mengenai item, yaitu nama item (item_name) dan jumlah item (item_quantity)

        '''
        item_name = item[ 0 ]
        item_exists = False
        for existing_item in self.items:
            if existing_item[ 0 ] == item_name:
                existing_item[ 1 ] += item[ 1 ]
                item_exists = True
                break

        if not item_exists:
            self.items.append(item)

    def update_item_name(self, item_name, new_item_name):
        '''
        Function untuk mengubah nama item dalam transaksi
        Parameters
        ---------------------------------------------------
        item_name: str
            Nama item yang ingin diubah

        new_item_name: str
            Nama baru yang akan diterapkan pada item
        '''
        for item in self.items:
            if item[ 0 ] == item_name:
                item[ 0 ] = new_item_name

    def update_item_qty(self, item_name, new_qty):
        '''
        Function update_item_qty dalam class Transaction berfungsi untuk meng-update
        jumlah/kuantitas item yang ada di dalam list 'items' dari transaksi.

        Parameters:
        ---------------------------------------------------
        item_name: str
            Nama item yang akan di-update

        new_qty: int
            Jumlah baru yang akan di-update
        '''
        for item in self.items:
            if item[ 0 ] == item_name:
                item[ 1 ] = new_qty

    def update_item_price(self, item_name, new_price):
        '''
        Function untuk meng-update harga barang pada transaksi
        Parameters
        ---------------------------------------------------
        item_name: str
            Nama barang yang akan di-update harganya

        new_price: int
            Harga baru dari barang yang akan di-update
        '''
        for item in self.items:
            if item[ 0 ] == item_name:
                item[ 2 ] = new_price

    def delete_item(self, item_name):
        '''
       Function untuk meng-hapus item dari transaksi
       Parameters
       ---------------------------------------------------
       item_name: str
           Nama item yang ingin dihapus dari transaksi
       '''
        for item in self.items:
            if item[ 0 ] == item_name:
                self.items.remove(item)

    def reset_transaction(self):
        '''
        Function untuk mengosongkan daftar item yang ada pada transaksi.
        '''
        self.items = [ ]

    def check_order(self):
        '''
        Function untuk memeriksa kevalidan pesanan yang dibuat.
        Jika data pesanan memiliki kekurangan informasi (None), maka akan muncul pesan
        "Terdapat kesalahan input data"
        Jika semua data pesanan sudah benar, maka akan menampilkan tabel pesanan beserta
        informasi jumlah barang, harga, dan total harga yang harus dibayar.
        '''
        for item in self.items:
            if None in item:
                print("Terdapat kesalahan input data")
                return
            else:
                print("Pemesanan sudah benar")

        total_price = 0
        order_table = [ ]
        for i, item in enumerate(self.items):
            item_price = item[ 1 ] * item[ 2 ]
            total_price += item_price
            order_table.append([ i + 1, item[ 0 ], item[ 1 ], item[ 2 ], item_price ])

        order_table.append([ "Total", "", "", "", total_price ])
        print(tabulate(order_table, headers = [ "No.", "Nama Item", "Jumlah", "Harga", "Total" ]))

    def total_price(self):
        '''
        Function untuk menghitung harga total pembelian barang berdasarkan item yang dibeli oleh user.
        Jika total pembelian melebihi batas diskon maka user akan mendapatkan diskon.
        Diskon yang didapatkan berbeda-beda tergantung dari jumlah total pembelian barang.
        '''
        total_price = 0
        for item in self.items:
            total_price += item[ 1 ] * item[ 2 ]

        discount = 0
        if total_price > 500000:
            discount = 0.9
            print("Anda berhak mendapatkan diskon sebesar 10%")
        elif total_price > 300000:
            discount = 0.92
            print("Anda berhak mendapatkan diskon sebesar 8%")
        elif total_price > 200000:
            discount = 0.95
            print("Anda berhak mendapatkan diskon sebesar 5%")
        else:
            print(
                "Anda belum berhak mendapatkan diskon, silakan cek informasi toko kami untuk melihat syarat mendapatkan diskon. Terima kasih")

        if discount != 0:
            print("Diskon: {}".format(total_price))
            total_price = total_price * discount

        return total_price

    def checkout_and_pay(self):
        '''
        Function untuk melakukan checkout dan pembayaran dari barang-barang
        yang dibeli oleh pelanggan.
        Melakukan print harga total, meminta konfirmasi pembayaran dari
        pelanggan, mengecek nominal pembayaran dan memberikan kembalian
        jika pembayaran berhasil. Jika pembayaran gagal, akan dicetak
        pesan pembayaran kurang. Selain itu, jika pembayaran dibatalkan,
        akan dicetak pesan pembayaran dibatalkan.
        '''
        total_price = self.total_price()
        print("Harga total: {}".format(total_price))

        confirmation = input("Apakah Anda ingin melakukan pembayaran? (y/n) ")
        if confirmation.lower() == "y":
            try:
                payment = int(input("Masukkan nominal pembayaran: "))
            except ValueError:
                print("Input harus angka.")
                return
            change = payment - total_price
            if change < 0:
                print("Pembayaran kurang.")
                return
            with open("order_history.csv", "a", newline = '') as csvfile:
                writer = csv.writer(csvfile)
                for item in self.items:
                    writer.writerow(
                        [ time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), item[ 0 ], item[ 1 ], item[ 2 ],
                          item[ 1 ] * item[ 2 ] ])
            print("Pembayaran berhasil dilakukan. Kembalian Anda: {}".format(change))
            self.reset_transaction()
        else:
            print("Pembayaran dibatalkan.")
