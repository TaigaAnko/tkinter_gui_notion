import tkinter as tk
from api import NotionAPI


class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280, borderwidth=1, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        self.var_checkbox = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            self, text="編集", variable=self.var_checkbox, command=self.toggle_editability
        )
        checkbox.pack(side=tk.LEFT)

        # テキストボックス1
        text_var1 = tk.StringVar()
        self.entry1 = tk.Entry(
            self, width=40, state=tk.DISABLED, textvariable=text_var1
        )
        self.entry1.pack(pady=10)

        # テキストボックス2
        text_var2 = tk.StringVar()
        self.entry2 = tk.Entry(
            self, width=40, state=tk.DISABLED, textvariable=text_var2
        )
        self.entry2.pack(pady=10)

        # 大きいテキストボックス
        self.text_output = tk.Text(self, height=10, width=40)
        self.text_output.pack(pady=10)

        # ボタン
        button = tk.Button(self, text="送信", command=self.submit)
        button.pack()

        # Textの変更を監視
        self.text_output.bind("<KeyRelease>", self.check_text_content)

    def toggle_editability(self):
        # チェックボックスの状態に応じてテキストボックスの編集を有効または無効にする
        state = tk.NORMAL if self.var_checkbox.get() else tk.DISABLED
        self.entry1.config(state=state)
        self.entry2.config(state=state)

    def submit(self):
        print("ボタンが押されました")
        id = self.entry1.get()
        token = self.entry2.get()
        content = self.text_output.get("1.0", tk.END + "-1c")
        NotionAPI(id, token, content)
        self.text_output.delete(1.0, tk.END)
        print(id, token, content)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fast Notion")
    root.geometry("400x300")
    app = Application(root=root)
    app.mainloop()
