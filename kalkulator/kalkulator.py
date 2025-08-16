import tkinter as tk
from tkinter import messagebox

# Warna pastel
BACKGROUND_COLOR = "#FFF1F8"
BUTTON_COLOR = "#FADADD"
DISPLAY_COLOR = "#FFF0F5"
TEXT_COLOR = "#444444"

# Fungsi logika kalkulator
def klik(tombol):
    if tombol == "=":
        try:
            hasil = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))
        except:
            messagebox.showerror("Error", "Perhitungan tidak valid!")
    elif tombol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, tombol)

# Membuat jendela utama
window = tk.Tk()
window.title("Kalkulator Pastel")
window.geometry("320x420")
window.config(bg=BACKGROUND_COLOR)
window.resizable(False, False)

# Entry/tampilan hasil
entry = tk.Entry(window, font=("Helvetica", 20), bg=DISPLAY_COLOR, fg=TEXT_COLOR, borderwidth=5, relief="groove", justify="right")
entry.pack(padx=10, pady=20, fill="both")

# Tombol-tombol kalkulator
tombol_list = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["Clear"]
]

# Menambahkan tombol ke jendela
for baris in tombol_list:
    frame = tk.Frame(window, bg=BACKGROUND_COLOR)
    frame.pack(expand=True, fill="both")
    for tombol in baris:
        btn = tk.Button(frame, text=tombol, font=("Helvetica", 18), bg=BUTTON_COLOR, fg=TEXT_COLOR,
                        relief="ridge", borderwidth=2,
                        command=lambda t=tombol: klik(t))
        btn.pack(side="left", expand=True, fill="both", padx=5, pady=5)

# Menjalankan aplikasi
window.mainloop()
