import tkinter as tk
from tkinter import Text
from tkinter import Scrollbar

class Menubar:
    def __init__(self,parent):
        font_menu = ("arial", 15)
        menubar = tk.Menu(parent.window)
        parent.window.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_menu, tearoff=0)
        file_dropdown.add_command(label="Novo arquivo",command=parent.novo_arquivo)
        file_dropdown.add_command(label="Abrir aquivo",command=parent.abrir_arquivo)
        file_dropdown.add_command(label="Salvar", command=parent.salvar)
        file_dropdown.add_command(label='Salvar em ', command=parent.salvar_em)
        file_dropdown.add_separator()
        file_dropdown.add_command(label ='Sair', command=parent.window.destroy)

        menubar.add_cascade(label = "Arquivo", menu=file_dropdown)


class Pythontext:

    def __init__(self, window):# o conteúdo de inicialização precisa tá presente aqui por completo
        window.title("Untitled - Pythontext")
        window.geometry("700x700")


        self.window = window
        self.textarea = tk.Text(window)
        self.scroll = tk.Scrollbar(window,command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.menubar = Menubar(self)

    def nome_do_arquivo(self):
        pass
    def novo_arquivo(self):
        pass
    def abrir_arquivo(self):
        pass
    def salvar(self):
        pass
    def salvar_em(self):
        pass

if __name__ == "__main__":
    window = tk.Tk()
    projeto = Pythontext(window)
    window.mainloop()