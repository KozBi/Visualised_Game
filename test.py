import tkinter as tk

def generuj_guziki():
    # Tworzenie trzech nowych guzików
    for i in range(1, 4):
        new_button = tk.Button(root, text=f'Button {i}')
        new_button.pack()

# Tworzenie okna głównego
root = tk.Tk()
root.title('Generowanie guzików')

# Tworzenie guzika "Generuj"
generuj_button = tk.Button(root, text='Generuj', command=generuj_guziki)
generuj_button.pack()

# Rozpoczęcie pętli głównej
root.mainloop()