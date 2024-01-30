import tkinter as tk
from api import NotionAPI
from form import From  


class Application(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=380, height=280, borderwidth=1, relief="flat")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        self.id_form = From(root=self, label_text='ID')
        self.id_form.grid(row=0, column=0, padx=10, pady=10)
        self.token_form = From(root=self, label_text="Token")
        self.token_form.grid(row=1, column=0, padx=10, pady=10)

        # 大きいテキストボックス
        self.text_output = tk.Text(self, height=10, width=40)
        self.text_output.grid(row=2, column=0, padx=10, pady=10)

        # ボタン
        self.submit_button = tk.Button(
            self, text="送信", command=self.submit, state=tk.DISABLED
        )
        self.submit_button.grid(row=3, column=0, padx=10, pady=10)

        # Textの変更を監視
        self.id_form.bind("<KeyRelease>", self.check_text_content)
        self.token_form.bind("<KeyRelease>", self.check_text_content)
        self.text_output.bind("<KeyRelease>", self.check_text_content)

    def check_text_content(self, event):
        # Textの内容が空でない場合、ボタンを活性化
        if (
            self.text_output.get("1.0", tk.END).strip()
            and self.id_form.get_entry_value().strip()
            and self.token_form.get_entry_value().strip()
        ):
            self.submit_button.config(state=tk.NORMAL)
        else:
            self.submit_button.config(state=tk.DISABLED)

    def submit(self):
        print("ボタンが押されました")
        id = str(self.id_form.get_entry_value())
        token = str(self.token_form.get_entry_value())
        content = str(self.text_output.get("1.0", tk.END + "-1c"))
        print(id, token, content)
        NotionAPI(id, token, content)
        self.text_output.delete(1.0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fast Notion")
    root.geometry("400x400")
    app = Application(root=root)
    app.mainloop()