import tkinter as tk
from tkinter import Text
from tkinter import Scrollbar

class Pythontext:

    def __init__(self, window):# o conteúdo de inicialização precisa tá presente aqui por completo
        window.title("Untitled - Pythontext")
        window.geometry("700x700")

        self.textarea = tk.Text(window)
        self.scroll = tk.Scrollbar(window,command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
    
if __name__ == "__main__":
    window = tk.Tk()
    projeto = Pythontext(window)
    window.mainloop()