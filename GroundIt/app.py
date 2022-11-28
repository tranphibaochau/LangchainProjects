import tkinter as tk
import tkinter.messagebox
import customtkinter
from tkinter.filedialog import askopenfile


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()

        self.title("GroundIt - A tagging tool for quantitative researches")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.imported_text = "Please import text document(s)"

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_0 = customtkinter.CTkFrame(master=self,
                                              width=180,
                                              corner_radius=0)
        self.frame_0.grid(row=0, column=0, sticky="nswe")

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_0 ============

        # configure grid layout (1x11)
        self.frame_0.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_0.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_0.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_0.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_0,
                                              text="CustomTkinter",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_0,
                                                text="Import Text File",
                                                command=lambda:self.import_doc())
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_0, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_0,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_1 ============

        # configure grid layout (2x3)
        self.frame_1.rowconfigure(0, weight=1)
        self.frame_1.columnconfigure(0, weight=1)

        # Text Widget
        self.main_text = tk.Text(self.frame_1, foreground="white", bg="#212325", height=200)
        self.main_text.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        self.main_text.insert('1.0', self.imported_text)

        # Right-click Menu
        self.menu = tk.Menu(self.main_text, tearoff=True)
        self.menu.add_command(label="Cut")
        self.menu.add_command(label="Copy")
        self.menu.add_separator()
        self.menu.add_command(label="Rename")

        def do_popup(event):
            try:
                self.menu.tk_popup(event.x_root, event.y_root)
            finally:
                self.menu.grab_release()

        self.main_text.bind("<Button-3>", do_popup)

        # scroll bar for the text widget
        self.textbox_scrollbar = customtkinter.CTkScrollbar(self.main_text, command=self.main_text.yview)
        self.textbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.main_text.configure(yscrollcommand=self.textbox_scrollbar.set)  # make text scrollable by the scrollbar
    def import_doc(self):
        # ask for import file
        file = askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
        if file is not None:
            content = file.read()
            self.main_text.delete('1.0', 'end') # delete the previous text
            # paste imported document into the current Text Widget
            self.main_text.insert('1.0', content) # '1.0' means line 1, character 0
            self.main_text.configure(state='disabled') # read-only mode


    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()