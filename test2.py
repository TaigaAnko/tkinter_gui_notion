import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel, Label, Entry, Button, StringVar
import configparser
import os

FILE_PASS = 'config/config.ini'

# メインウィンドウの作成
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# ウィンドウを常に最前面に設定
root.attributes("-topmost", True)

save_shortcut = StringVar(value="<Control-Return>")

def open_settings_page():
    # 設定ページを新しいウィンドウで開く
    settings_window = Toplevel(root)
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

    def save_config():
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
    Button(settings_window, text="保存", command=save_config).pack(pady=20)
    # 現在のショートカットキーに基づいてバインディング設定
    settings_window.bind(save_shortcut.get(), lambda event: save_config())

# def open_shortcut_settings_page():
#     # ショートカット設定ページを新しいウィンドウで開く
#     shortcut_window = Toplevel(root)
#     shortcut_window.title("ショートカット設定")
#     shortcut_window.geometry("300x150")

#     # ショートカット入力ラベルとエントリーフィールド
#     Label(shortcut_window, text="保存ボタンのショートカット:").pack(pady=5)
#     shortcut_entry = Entry(shortcut_window, width=30)
#     shortcut_entry.insert(0, save_shortcut.get())  # 現在のショートカットを表示
#     shortcut_entry.pack(pady=5)

#     def apply_shortcut():
#         new_shortcut = shortcut_entry.get()
#         if new_shortcut:
#             save_shortcut.set(new_shortcut)
#             messagebox.showinfo("適用完了", f"ショートカットが{new_shortcut}に変更されました。")
#             shortcut_window.destroy()

#     # ショートカット適用ボタン
#     Button(shortcut_window, text="適用", command=apply_shortcut).pack(pady=20)

# メニューバーの作成
menubar = tk.Menu(root)
root.config(menu=menubar)

# 設定メニュー
settings_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="設定", menu=settings_menu)
settings_menu.add_command(label="IDとTokenの設定", command=open_settings_page)
# settings_menu.add_command(label="ショートカット設定", command=open_shortcut_settings_page)

root.mainloop()
