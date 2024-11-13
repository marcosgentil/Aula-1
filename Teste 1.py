import tkinter as tk
from datetime import datetime

def atualizar_hora():
    agora = datetime.now().strftime("%H:%M:%S")
    label_hora.config(text=agora)
    label_hora.after(1000, atualizar_hora)


janela = tk.Tk()
janela.title("Relógio atual")


label_hora = tk.Label(janela, font=("Helvetica", 48), fg="black")
label_hora.pack()

atualizar_hora()

janela.mainloop()