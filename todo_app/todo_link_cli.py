# todo_link_cli.py
import json
import os
import webbrowser
from urllib.parse import urlparse
from colorama import init, Fore, Back, Style

import webbrowser

def open_link():
    webbrowser.open("index.html")  # bisa juga "http://localhost:5000"

init(autoreset=True)

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def valid_url(url: str) -> str:
    url = url.strip()
    if not url:
        return ""
    parsed = urlparse(url)
    if not parsed.scheme:
        # auto prepend http jika user lupa
        url = "https://" + url
    return url

def header(text):
    print(Back.BLUE + Fore.WHITE + " " + text + " " + Style.RESET_ALL)

def show_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "Belum ada tugas.")
        return
    header("Daftar Tugas")
    for i, t in enumerate(tasks, start=1):
        status = Fore.GREEN + "✓" if t.get("done") else Fore.RED + "•"
        title = (Style.BRIGHT + t["title"]) if not t.get("done") else (Style.DIM + t["title"])
        link = t["url"] or "-"
        link_color = Fore.CYAN if t["url"] else Fore.BLACK + Style.DIM
        print(f"{Fore.MAGENTA}{i:>2}. {status} {Style.RESET_ALL}{title}   {link_color}{link}{Style.RESET_ALL}")

def add_task(tasks):
    header("Tambah Tugas")
    title = input("Judul: ").strip()
    url = valid_url(input("Link (opsional): "))
    if not title:
        print(Fore.RED + "Judul tidak boleh kosong.")
        return
    tasks.append({"title": title, "url": url, "done": False})
    save_tasks(tasks)
    print(Fore.GREEN + "Tugas ditambahkan.")

def mark_done(tasks):
    if not tasks:
        print(Fore.YELLOW + "Tidak ada tugas.")
        return
    show_tasks(tasks)
    try:
        idx = int(input("Nomor tugas yang selesai: "))
        tasks[idx-1]["done"] = True
        save_tasks(tasks)
        print(Fore.GREEN + "Tugas ditandai selesai.")
    except Exception:
        print(Fore.RED + "Nomor tidak valid.")

def edit_task(tasks):
    if not tasks:
        print(Fore.YELLOW + "Tidak ada tugas.")
        return
    show_tasks(tasks)
    try:
        idx = int(input("Nomor tugas yang ingin diedit: "))
        t = tasks[idx-1]
        print(Fore.CYAN + f"Judul lama: {t['title']}")
        new_title = input("Judul baru (kosong = tetap): ").strip()
        print(Fore.CYAN + f"Link lama: {t['url'] or '-'}")
        new_url = input("Link baru (kosong = hapus/tetap kosong): ").strip()
        if new_title:
            t["title"] = new_title
        t["url"] = valid_url(new_url) if new_url else ""
        save_tasks(tasks)
        print(Fore.GREEN + "Tugas diperbarui.")
    except Exception:
        print(Fore.RED + "Nomor tidak valid.")

def delete_task(tasks):
    if not tasks:
        print(Fore.YELLOW + "Tidak ada tugas.")
        return
    show_tasks(tasks)
    try:
        idx = int(input("Nomor tugas yang dihapus: "))
        removed = tasks.pop(idx-1)
        save_tasks(tasks)
        print(Fore.GREEN + f"Menghapus: {removed['title']}")
    except Exception:
        print(Fore.RED + "Nomor tidak valid.")

def open_link(tasks):
    if not tasks:
        print(Fore.YELLOW + "Tidak ada tugas.")
        return
    show_tasks(tasks)
    try:
        idx = int(input("Nomor tugas yang link-nya ingin dibuka: "))
        url = tasks[idx-1].get("url", "")
        if not url:
            print(Fore.RED + "Tugas ini tidak punya link.")
            return
        print(Fore.BLUE + "Membuka link di browser...")
        webbrowser.open(url)
    except Exception:
        print(Fore.RED + "Nomor tidak valid.")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    print(Back.WHITE + Fore.BLACK + "  TO-DO LIST - Link & Color CLI  " + Style.RESET_ALL)
    print(Fore.CYAN + "1." + Style.RESET_ALL + " Lihat tugas")
    print(Fore.CYAN + "2." + Style.RESET_ALL + " Tambah tugas")
    print(Fore.CYAN + "3." + Style.RESET_ALL + " Tandai selesai")
    print(Fore.CYAN + "4." + Style.RESET_ALL + " Edit tugas")
    print(Fore.CYAN + "5." + Style.RESET_ALL + " Hapus tugas")
    print(Fore.CYAN + "6." + Style.RESET_ALL + " Open Link")
    print(Fore.CYAN + "7." + Style.RESET_ALL + " Keluar")

def main():
    tasks = load_tasks()
    while True:
        try:
            print()
            menu()
            choice = input(Fore.YELLOW + "Pilih menu (1-7): " + Style.RESET_ALL).strip()
            clear()
            if choice == "1":
                show_tasks(tasks)
            elif choice == "2":
                add_task(tasks); tasks = load_tasks()
            elif choice == "3":
                mark_done(tasks)
            elif choice == "4":
                edit_task(tasks); tasks = load_tasks()
            elif choice == "5":
                delete_task(tasks); tasks = load_tasks()
            elif choice == "6":
                open_link(tasks)
            elif choice == "7":
                print(Fore.GREEN + "Sampai jumpa!")
                break
            else:
                print(Fore.RED + "Menu tidak dikenal.")
        except KeyboardInterrupt:
            print("\n" + Fore.RED + "Dibatalkan. Tekan Enter untuk lanjut atau Ctrl+C lagi untuk keluar.")
            try:
                input()
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    clear()
    main()