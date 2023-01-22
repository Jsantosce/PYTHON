import os
import urllib.request
from urllib.parse import urlparse
from tkinter import *
from tkinter import filedialog


def download_files():
    api_key = api_key_entry.get()
    download_folder = folder_entry.get()
    if not api_key or not download_folder:
        return
    files_list = text_area.get("1.0", END).split("\n")
    files_list = [file.strip() for file in files_list if file]
    # download each file
    for file in files_list:
        file_url = server+"xml/"+file+"?apiKey="+api_key
        # extract the file name from the server address
        parsed_url = urlparse(file_url)
        file_name = os.path.basename(parsed_url.path) + '.xml'
        # create the full file path
        file_path = os.path.join(download_folder, file_name)
        urllib.request.urlretrieve(file_url, file_path)


def select_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, END)
    folder_entry.insert(0, folder_path)


root = Tk()
root.title("Download xml por JannioFSantos https://github.com/Jsantosce ")

server = "https://cfe.sefaz.ce.gov.br:8443/portalcfews/mfe/fiscal-coupons/"

api_key_label = Label(root, text="API Key:")
api_key_label.pack()

api_key_entry = Entry(root,width=70)
api_key_entry.pack()

folder_label = Label(root, text="Download :")
folder_label.pack()

folder_entry = Entry(root,width=70)
folder_entry.pack()

folder_button = Button(root, text="Selecionar pasta", command=select_folder)
folder_button.pack()

text_area = Text(root, height=30, width=70)
text_area.pack()

download_button = Button(root, text="Iniciar download: MAX 400 xml", command=download_files)
download_button.pack()

root.mainloop()

#salvar arquivo vomo executavel
#pyinstaller -F -w sabadotestetrim.py
