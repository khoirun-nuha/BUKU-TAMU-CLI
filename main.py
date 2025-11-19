import service
import style

def menu():
    while True:
        style.clear()

        print(style.BOX_TOP)
        print("│{:^30}│".format(style.BOLD + "Buku Tamu CLI" + style.RESET))
        print(style.BOX_BOTTOM)

        print(f"""
{style.CYAN}1.{style.RESET} Tambah Tamu
{style.CYAN}2.{style.RESET} Lihat Semua Tamu
{style.CYAN}3.{style.RESET} Cari Tamu
{style.CYAN}4.{style.RESET} Edit Tamu
{style.CYAN}5.{style.RESET} Hapus Tamu
{style.CYAN}6.{style.RESET} Keluar
""")

        pilihan = input(f"{style.YELLOW}Pilih menu: {style.RESET}")

        if pilihan == "1":
            nama = input("Nama: ")
            alamat = input("Alamat: ")
            keperluan = input("Keperluan: ")

            service.tambah_tamu(nama, alamat, keperluan)
            print(f"{style.GREEN}✔ Tamu ditambahkan!{style.RESET}\n")
            input("Tekan Enter untuk lanjut...")

        elif pilihan == "2":
            data = service.list_tamu()
            if not data:
                print(style.RED + "Belum ada tamu." + style.RESET)
                input("Enter...")
                continue

            print(style.BOX_TOP)
            print("│{:^30}│".format("DAFTAR TAMU"))
            print(style.BOX_BOTTOM)

            for t in data:
                print(f"{style.BLUE}[{t['id']}]{style.RESET} {t['nama']} - {t['keperluan']} ({t['waktu']})")

            print()
            input("Enter...")

        elif pilihan == "3":
            key = input("Cari nama/keperluan: ")
            hasil = service.cari_tamu(key)

            if not hasil:
                print(style.RED + "Tidak ditemukan." + style.RESET)
                input("Enter...")
                continue

            for t in hasil:
                print(f"{style.GREEN}[{t['id']}]{style.RESET} {t['nama']} - {t['keperluan']} ({t['waktu']})")

            input("Enter...")

        elif pilihan == "4":
            id_edit = input("ID yang diedit: ")
            nama = input("Nama baru (kosongkan jika tdk ingin ubah): ") or None
            alamat = input("Alamat baru: ") or None
            keperluan = input("Keperluan baru: ") or None

            hasil = service.edit_tamu(id_edit, nama, alamat, keperluan)
            if hasil:
                print(style.GREEN + "✔ Data diperbarui!" + style.RESET)
            else:
                print(style.RED + "ID tidak ditemukan." + style.RESET)

            input("Enter...")

        elif pilihan == "5":
            id_hapus = input("ID yang dihapus: ")
            if service.hapus_tamu(id_hapus):
                print(style.GREEN + "✔ Tamu dihapus!" + style.RESET)
            else:
                print(style.RED + "ID tidak ditemukan." + style.RESET)

            input("Enter...")

        elif pilihan == "6":
            print(style.YELLOW + "Sampai jumpa!" + style.RESET)
            break

        else:
            print(style.RED + "❌ Pilihan tidak valid." + style.RESET)
            input("Enter...")


if __name__ == "__main__":
    menu()
