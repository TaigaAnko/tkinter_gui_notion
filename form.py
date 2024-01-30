import tkinter as tk


class From(tk.Frame):
    def __init__(self, root=None, checkbox_text=None, label_text=None):
        super().__init__(root, width=30, height=20, borderwidth=1, relief="flat")

        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.form_widgets(checkbox_text, label_text)

    def form_widgets(self, checkbox_text=None, label_text=None):
        # ラベルの配置
        label_font = ("Arial", 12) 
        label = tk.Label(self, text=label_text, font=label_font)
        label.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.var_checkbox = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            self,
            text=checkbox_text,
            variable=self.var_checkbox,
            command=self.change_editability,
        )
        checkbox.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        # テキストボックス
        text_var = tk.StringVar()
        self.entry = tk.Entry(self, width=40, state=tk.DISABLED, textvariable=text_var)
        self.entry.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        return self.entry

    def change_editability(self):
        # チェックボックスの状態に応じてテキストボックスの編集を有効または無効にする
        state = tk.NORMAL if self.var_checkbox.get() else tk.DISABLED
        self.entry.config(state=state)
    
    def get_entry_value(self):
        # テキストボックスの内容を取得
        return self.entry.get()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fast Notion")
    root.geometry("400x300")
    app = From(root=root)
    app.mainloop()
