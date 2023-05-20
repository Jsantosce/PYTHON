import os
import urllib.request
from urllib.parse import urlparse
from tkinter import *
from tkinter import filedialog
import time
import tkinter as tk


def download_files():
    api_key = api_key_entry.get()
    download_folder = folder_entry.get()
    if not api_key or not download_folder:
        return
    files_list = text_area.get("1.0", END).split("\n")
    files_list = [file.strip() for file in files_list if file]
    files_downloaded = False
    # download each file
    for file in files_list:
        file_url = server+"xml/"+file+"?apiKey="+api_key
        # extract the file name from the server address
        parsed_url = urlparse(file_url)
        file_name = os.path.basename(parsed_url.path) + '.xml'
        # create the full file path
        file_path = os.path.join(download_folder, file_name)
        #logica para verificar se o arquivo ja existe continuar o loop sem tenta baixar o arquivo
        if os.path.exists(file_path):
            continue

        try:
            urllib.request.urlretrieve(file_url, file_path)
            files_downloaded = True
        except:
            #aqui a logica para tentar novamente
            #apos 5 sgundos
            time.sleep(5)
            urllib.request.urlretrieve(file_url, file_path)
            files_downloaded = True
        print("chave: " + file_name + " baixada com sucesso")
    
    if not files_downloaded:
        import tkinter as tk
        from tkinter import messagebox

        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Todos os xml foram baixados com sucesso!")


def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, END)
    folder_entry.insert(0, folder_path)



#codigo senha
import sys
from tkinter import simpledialog


def ask_password():   
    password = "@1234"
    entered_password = simpledialog.askstring("Tela login:usuario teste", "Senha:",show="*")
    if entered_password != password:
        tk.messagebox.showerror("Erro", "Senha incorreta. Saindo do sistema.")
        sys.exit()

ask_password()




root = Tk()
root.title("Download Cf-e por JannioFSantos")

server = "https://cfe.sefaz.ce.gov.br:8443/portalcfews/mfe/fiscal-coupons/"

api_key_label = Label(root, text="Apikey=")
api_key_label.pack()

api_key_entry = Entry(root,width=70)
api_key_entry.pack()

folder_label = Label(root, text="Caminho pasta download")
folder_label.pack()

folder_entry = Entry(root,width=70)
folder_entry.pack()

folder_button = Button(root, text="Selecionar pasta", command=select_folder)
folder_button.pack()

text_area = Text(root, height=30, width=70)
text_area.pack()

download_button = Button(root, text="Iniciar download", command=download_files)
download_button.pack(padx=10, pady=10)

root.mainloop()



