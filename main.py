import tkinter as tk
from tkinter import ttk, messagebox
from user import User
from lib import isValid
import db, traceback, datetime
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("User admin interface demo")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="User admin", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.table_button_event, text="View users")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.form_button_event, text="Add user")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")

        # table
        cols = ('ID', 'Nombre', 'Email')
        self.table = ttk.Treeview(columns=cols, show='headings')
        self.table.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.5']]

        for i, (name, score) in enumerate(tempList, start=1):
            self.table.insert("", "end", values=(i, name, score))

        for col in cols:
            self.table.heading(col, text=col)

        self.form = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.name = customtkinter.CTkLabel(self.form, text="Name")
        self.name.grid(row=2, column=0)

        self.name_field = customtkinter.CTkEntry(self.form)
        self.name_field.grid(row=2, column=1, ipadx=100, pady=5)

        self.email = customtkinter.CTkLabel(self.form, text="E-mail")
        self.email.grid(row=1, column=0)

        self.email_field = customtkinter.CTkEntry(self.form)
        self.email_field.bind("<Return>", command=self.validate_create_user_form)
        self.email_field.grid(row=1, column=1, ipadx=100, pady=5)

        self.submit_button = customtkinter.CTkButton(self.form, command=self.validate_create_user_form, text="Create user")
        self.submit_button.grid(row=3, column=1, padx=20, pady=10)



    def validate_create_user_form(self):
        if (self.email_field.get() != "" and self.name_field.get() != "" and isValid(self.email_field.get())):
            usr = User(id=db.getNewId(), email=self.email_field.get(), name=self.name_field.get(), created_at=datetime.datetime.now())
            # print('new user added: ', usr.serialize())
            db.insert(usr)

            self.email_field.delete(0, tk.END)
            self.email_field.insert(0, "")
            self.name_field.delete(0, tk.END)
            self.name_field.insert(0, "")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def select_frame_by_name(self, name):
        if name == "table":
            self.table.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        else:
            self.table.grid_forget()
        if name == "form":
            self.form.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        else:
            self.form.grid_forget()

    def table_button_event(self):
        self.select_frame_by_name("table")

    def form_button_event(self):
        self.select_frame_by_name("form")

if __name__ == "__main__":
    app = App()
    app.mainloop()
