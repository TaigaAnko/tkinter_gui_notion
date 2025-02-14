import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel, Label, Entry, Button, StringVar
import configparser
import os

#Version Infomation
Version = "1.0"

FILE_PASS = 'config/config.ini'

class NormalMenu(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        master.config(menu=self)

    def setting_menu(self):
        setting_menu = tk.Menu(self, tearoff=0)
        setting_menu.add_command(label="IDとToken", command=self.open_settings_page)
        self.add_cascade(label="設定", menu=setting_menu)

    def version_menu(self):
        def push():
            tk.messagebox.showinfo("バージョン", Version)
        ver_menu = tk.Menu(self, tearoff=0)
        ver_menu.add_command(label="バージョンについて", command=push)
        self.add_cascade(label="バージョン", menu=ver_menu)
    
    def open_settings_page(self):
        # 設定ページを新しいウィンドウで開く
        settings_window = Toplevel(self)
        settings_window.title("IDとTokenの設定")
        settings_window.geometry("300x200")

        # config.iniから設定を読み込む
        config = configparser.ConfigParser()
        if os.path.exists(FILE_PASS):
            config.read(FILE_PASS)
            saved_id = config.get('SETTINGS', 'ID', fallback="")
            saved_token = config.get('SETTINGS', 'Token', fallback="")
        else:
            saved_id = ""
            saved_token = ""

        # IDラベルとエントリーフィールド
        Label(settings_window, text="ID").pack(pady=5)
        id_entry = Entry(settings_window, width=30)
        id_entry.insert(0, saved_id)  # 保存されたIDを表示
        id_entry.pack(pady=5)

        # Tokenラベルとエントリーフィールド
        Label(settings_window, text="Token").pack(pady=5)
        token_entry = Entry(settings_window, width=30)
        token_entry.insert(0, saved_token)  # 保存されたTokenを表示
        token_entry.pack(pady=5)

        def _save_config():
            config = configparser.ConfigParser()
            if not os.path.exists(FILE_PASS):
                # config.iniが存在しない場合、作成する
                with open(FILE_PASS, 'w') as configfile:
                    config.write(configfile)

            # IDとTokenをconfig.iniに保存
            config.read(FILE_PASS)
            if 'SETTINGS' not in config.sections():
                config.add_section('SETTINGS')
            config.set('SETTINGS', 'ID', id_entry.get())
            config.set('SETTINGS', 'Token', token_entry.get())

            with open(FILE_PASS, 'w') as configfile:
                config.write(configfile)
            
            messagebox.showinfo("保存完了", "IDとTokenが保存されました。")
            settings_window.destroy()

        # 保存ボタン
        Button(settings_window, text="保存", command=_save_config).pack(pady=20)

        



if __name__ == '__main__':

    win = tk.Tk()
    menu_bar=NormalMenu(win)
    menu_bar.setting_menu()
    menu_bar.version_menu()
    win.mainloop()
