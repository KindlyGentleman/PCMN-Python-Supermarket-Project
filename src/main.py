# Import kelas Transaction dari modul transaction
from transaction import Transaction

# Menampilkan pesan selamat datang dan ASCII art
ascii_art = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢻⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡏⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⣹⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣀⣀⣀⣸⣧⣀⣀⣀⣀⣿⣄⣀⣀⣀⣠⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣤⣼⣧⣤⣤⣤⣤⣿⣤⣤⣤⣼⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠤⠼⠷⠤⠤⠤⠤⠿⠦⠤⠾⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⢶⣶⠶⠶⠶⠶⠶⠶⣶⠶⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣠⡿⠀⠀⠀⠀⠀⠀⢷⣄⣼⠇⠀⠀⠀
"""
print(ascii_art)
print("SELAMAT DATANG DI SISTEM KASIR SUPERMARKET")

# Membuat objek transaksi dengan ID transaksi 123
trnsct = Transaction(123)

# Loop program utama
while True:

    # Menampilkan menu utama
    print("\n1. Tambah item")
    print("2. Update item")
    print("3. Hapus item")
    print("4. Reset transaksi")
    print("5. Cek pemesanan")
    print("6. Hitung total belanja")
    print("7. Bayar")
    print("8. Keluar\n")

    # Mengambil input dari pengguna
    try:
        choice = int(input("Masukkan pilihan Anda (1-8): "))
    except ValueError:
        # Jika input bukan angka, tampilkan pesan error
        print("Input yang dimasukan harus berupa angka, silakan coba lagi")
        continue

    # Melakukan aksi sesuai dengan pilihan pengguna
    if choice == 1:
        # Tambah item
        # Mengambil input nama item, jumlah item, dan harga item
        try:
            item_name = input("Masukkan nama item: ")
            item_qty = int(input("Masukkan jumlah item: "))
            item_price = int(input("Masukkan harga item: "))
        except ValueError:
            # Jika input jumlah item atau harga item bukan angka, tampilkan pesan error
            print("Input jumlah item dan harga item harus angka")
            continue
        # Menambah item ke transaksi
        trnsct.add_item([ item_name, item_qty, item_price ])
        # Tampilkan pesan sukses
        print(f"Item {item_name} telah ditambahkan")
    elif choice == 2:
        # Update item
        # Mengambil input nama item dan pilihan data yang ingin di-update
        try:
            item_name = input("Masukkan nama item: ")
            update_choice = int(input("Pilih data yang ingin diupdate (1. Nama item, 2. Jumlah item, 3. Harga item): "))
        except ValueError:
            # Jika input bukan angka, tampilkan pesan error
            print("Input pilihan harus angka")
            continue

        # Melakukan update sesuai dengan pilihan
        if update_choice == 1:
            new_item_name = input("Masukkan nama baru: ")
            trnsct.update_item_name(item_name, new_item_name)
            print(f"Nama item {item_name} telah diubah menjadi {new_item_name}")
        elif update_choice == 2:
            try:
                new_qty = int(input("Masukkan jumlah baru: "))
            except ValueError:
                print("Input jumlah item harus angka")
                continue
            trnsct.update_item_qty(item_name, new_qty)
            print(f"Jumlah item {item_name} telah diubah menjadi {new_qty}")
        elif update_choice == 3:
            try:
                new_price = int(input("Masukkan harga baru: "))
            except ValueError:
                print("Input harga item harus angka")
                continue
            trnsct.update_item_price(item_name, new_price)
            print(f"Harga item {item_name} telah diubah menjadi {new_price}")
        else:
            print("Pilihan tidak tersedia")
    elif choice == 3:
        # Hapus item
        # Mengambil input nama item yang ingin dihapus
        item_name = input("Masukkan nama item: ")
        trnsct.delete_item(item_name)
        print(f"Item {item_name} telah dihapus")
    elif choice == 4:
        # Menghapus item secara keseluruhan
        trnsct.reset_transaction()
        # Tampilkan pesan sukses
        print("Transaksi telah di-reset")
    elif choice == 5:
        # Cek pemesanan
        # Menampilkan rincian pemesanan dan cek input data
        trnsct.check_order()
    elif choice == 6:
        # Hitung total belanja
        # Menampilkan total belanja
        total_price = trnsct.total_price()
        print(f"Total belanja: {total_price}")
    elif choice == 7:
        # Bayar
        trnsct.checkout_and_pay()
    elif choice == 8:
        # Tampilkan pesan selamat tinggal dan keluar dari loop program utama
        print("Terima kasih telah menggunakan sistem ini, selamat tinggal!")
        break
    else:
        # Jika pilihan tidak valid, tampilkan pesan error
        print("Pilihan tidak tersedia")
