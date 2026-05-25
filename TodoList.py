todo_list = []

def display_menu():
    print("\nMenu:")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Tandai tugas selesai")
    print("5. Keluar")


def tambah_tugas():
    tugas = input("Masukkan tugas baru: ")
    todo_list.append({'tugas': tugas, 'selesai': False})
    print(f"Tugas '{tugas}' berhasil ditambahkan.")


def lihat_tugas():
    if not todo_list:
        print("Tidak ada tugas dalam daftar.")
        return
    
    print("\nDaftar Tugas:")
    for idx, item in enumerate(todo_list, start=1):
        status = "Selesai" if item['selesai'] else "Belum selesai"
        print(f"{idx}. {item['tugas']} - {status}")


def hapus_tugas():
    lihat_tugas()
    if not todo_list:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        if 1 <= nomor <= len(todo_list):
            tugas_dihapus = todo_list.pop(nomor - 1)
            print(f"Tugas '{tugas_dihapus['tugas']}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")


def tandai_selesai():
    lihat_tugas()

    if not todo_list:
        return

    try:
        nomor = int(input("Masukkan nomor tugas yang sudah selesai: "))

        if 1 <= nomor <= len(todo_list):
            todo_list[nomor - 1]["selesai"] = True
            print(
                f"Tugas '{todo_list[nomor - 1]['tugas']}' "
                "telah ditandai sebagai selesai."
            )
        else:
            print("Nomor tugas tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")


def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-5): ")
        
        if choice == '1':
            tambah_tugas()
        elif choice == '2':
            lihat_tugas()
        elif choice == '3':
            hapus_tugas()
        elif choice == '4':
            tandai_selesai()
        elif choice == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()