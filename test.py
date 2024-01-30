import tkinter as tk
from form import From  

class MainApplication(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.pack()

        # From クラスのインスタンスを作成
        self.id_form = From(root=self, checkbox_text="ID")

        # テキスト内容を取得するボタン
        self.get_text_button = tk.Button(self, text="テキスト取得", command=self.get_text)
        self.get_text_button.pack()

    def get_text(self):
        # From インスタンスからテキストエントリの内容を取得
        entry_value = self.id_form.get_entry_value()
        print("テキスト内容:", entry_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root=root)
    app.mainloop()