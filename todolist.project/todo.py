# todo.py
tasks = []

def show_menu():
    print("\n=== To Do List ===")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

while True:
    show_menu()
    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        if not tasks:
            print("Belum ada tugas.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        new_task = input("Masukkan tugas baru: ")
        tasks.append(new_task)
        print("Tugas ditambahkan!")

    elif choice == "3":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        delete_index = int(input("Pilih nomor tugas yang mau dihapus: "))
        if 0 < delete_index <= len(tasks):
            removed = tasks.pop(delete_index - 1)
            print(f"Tugas '{removed}' sudah dihapus.")
        else:
            print("Nomor tidak valid.")

    elif choice == "4":
        print("Keluar... sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
