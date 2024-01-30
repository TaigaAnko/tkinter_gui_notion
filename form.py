import tkinter as tk


class From(tk.Frame):
    def __init__(self, root=None, checkbox_text=None):
        super().__init__(root, width=30, height=20, borderwidth=1, relief="groove")

        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.form_widgets(checkbox_text)

    def form_widgets(self, checkbox_text=None):
        self.var_checkbox = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            self,
            text=checkbox_text,
            variable=self.var_checkbox,
            command=self.change_editability,
        )
        checkbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # テキストボックス1
        text_var = tk.StringVar()
        self.entry = tk.Entry(self, width=40, state=tk.DISABLED, textvariable=text_var)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

    def change_editability(self):
        # チェックボックスの状態に応じてテキストボックスの編集を有効または無効にする
        state = tk.NORMAL if self.var_checkbox.get() else tk.DISABLED
        self.entry.config(state=state)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fast Notion")
    root.geometry("400x300")
    app = From(root=root)
    app.mainloop()
