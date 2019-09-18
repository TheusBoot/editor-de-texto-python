import tkinter as tk
from tkinter import Text
from tkinter import Scrollbar
from tkinter import filedialog

class Menubar:
    def __init__(self,parent):
        font_menu = ("arial", 15)
        menubar = tk.Menu(parent.window)
        parent.window.config(menu=menubar)
        file_dropdown = tk.Menu(menubar, font=font_menu, tearoff=0)
        file_dropdown.add_command(label="Novo arquivo",
        accelerator="Ctrl+N",
        command=parent.novo_arquivo)
        file_dropdown.add_command(label="Abrir aquivo",accelerator="Ctrl+o",
        command=parent.abrir_arquivo)
        file_dropdown.add_command(label="Salvar", accelerator="Ctrl+S", 
        command=parent.salvar)
        file_dropdown.add_command(label='Salvar em ', accelerator="Ctrl+Shilf+S", 
        command=parent.salvar_em)
        file_dropdown.add_separator()
        file_dropdown.add_command(label ='Sair', command=parent.window.destroy)
        menubar.add_cascade(label = "Arquivo", menu=file_dropdown)

class Statusbar:
    def __init__(self, parent):
        font_menu = ("arial", 12)
        self.status = tk.StringVar()
        self.status.set("Pythontext - 0.1 *Theuskillbr*")
        label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
        bg="lightgrey", anchor="sw", font= font_menu)
        label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def atualizar_statusbar(self, *args):
        if isinstance(args[0], bool):
            self.status.set("Arquivo Salvo!")
        else:
            self.status.set("Pythontext - 0.1 *Theuskillbr*")


class Pythontext:

    def __init__(self, window):# o conteúdo de inicialização precisa tá presente aqui por completo
        window.title("Untitled - Pythontext")
        window.geometry("700x700")
        self.window = window
        self.aquivo_nome = None
        self.textarea = tk.Text(window)
        self.scroll = tk.Scrollbar(window,command=self.textarea.yview)
        self.textarea.configure(yscrollcommand=self.scroll.set)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.pack(side=tk.RIGHT,fill=tk.Y)
        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)
        self.bind_teclas()

    def nome_do_arquivo(self, name=None):
        if name:
            self.window.title(name + "-Pythontext")
        else:
            self.window.title("Untiled - Pythontext")

    def novo_arquivo(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.arquivo_nome = None
        self.nome_do_arquivo()

    def abrir_arquivo(self,*args):
        self.aquivo_nome = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Todos os Arquivos", "*.*"),
            ("Arquivo de texto", "*.txt"),
            ("Python Scripts", "*.py"),
            ("Documentos de remarcação", "*.md"),
            ("Java-Script Arquivos", "*.js"),
            ("HTML Arquivo", "*.html"),
            ("CSS Arquivo", "*.css"),
            ("PDF Aquivos", "*.pdf")])
        if self.aquivo_nome:
            self.textarea.delete(1.0, tk.END)
            with open(self.aquivo_nome, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.nome_do_arquivo(self.aquivo_nome)

    def salvar(self,*args):
        if self.nome_do_arquivo:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.arquivo_nome, "w") as f:
                    f.write(textarea_content)
                self.statusbar.atualizar_statusbar(True)
            except Exception as Error:
                print(Error)

    def salvar_em(self,*args):
        try:
            novo_arquivo = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("Todos os Arquivos", "*.*"),
                ("Arquivo de texto", "*.txt"),
                ("Python Scripts", "*.py"),
                ("Documentos de remarcação", "*.md"),
                ("Java-Script Arquivos", "*.js"),
                ("HTML Arquivo", "*.html"),
                ("CSS Arquivo", "*.css"),
                ("PDF Aquivos", "*.pdf")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(novo_arquivo, "w") as f:
                f.write(textarea_content)
            self.arquivo_nome = novo_arquivo
            self.nome_do_arquivo(self.arquivo_nome)
            self.statusbar.atualizar_statusbar(True)
        except Exception as Error:
            print(Error)

    def bind_teclas(self):
        self.textarea.bind('<Control-n>',self.novo_arquivo)
        self.textarea.bind('<Control-o>',self.abrir_arquivo)
        self.textarea.bind('<Control-s>',self.salvar)
        self.textarea.bind('<Control-S>',self.salvar_em)
        self.textarea.bind('<Key>',self.statusbar.atualizar_statusbar)

if __name__ == "__main__":
    window = tk.Tk()
    projeto = Pythontext(window)
    window.mainloop()