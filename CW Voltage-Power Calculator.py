# CW Voltage-Power Calculator
#
# This is a simple GUI application that allows the user to enter a value for either Vpp, Vrms, mW, or dBm
# and the program will calculate the other three values based on the entered value.
# The user may change any value after the initial calculation and the program will recalculate the other values
# without needing to clear the fields beforehand.
# The user may also enter an impedance value, which defaults to 50 Ohms.
# The application uses the tkinter and ttkbootstrap libraries for styling and layout.
# The math library is used for logarithmic and square root calculations.
# OS and sys libraries are used for packaging icons with auto-py-to-exe.
#
# 30 March 2024
# GS

import os
import sys
import math
import pywinstyles
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.vpp = ttk.StringVar(value="")
        self.vrms = ttk.StringVar(value="")
        self.mw = ttk.StringVar(value="")
        self.dbm = ttk.StringVar(value="")
        self.modified_field = None  # track which field was modified

        # add traces to detect changes in the fields
        self.vpp.trace_add("write", lambda *args: self.set_modified_field("vpp"))
        self.vrms.trace_add("write", lambda *args: self.set_modified_field("vrms"))
        self.mw.trace_add("write", lambda *args: self.set_modified_field("mw"))
        self.dbm.trace_add("write", lambda *args: self.set_modified_field("dbm"))

        # form header
        hdr_txt = "Enter a value to calculate the rest:"
        hdr = ttk.Label(master=self, text=hdr_txt, width=50)
        hdr.pack(fill=X, pady=10)

        # form entries
        self.create_form_entry("Vpp", self.vpp)
        self.create_form_entry("Vrms", self.vrms)
        self.create_form_entry("mW", self.mw)
        self.create_form_entry("dBm", self.dbm)
        self.create_buttonbox()

    def set_modified_field(self, field_name):
        # set the name of the field that was modified
        self.modified_field = field_name

    def create_form_entry(self, label, variable):
        # entry field with labels and validation
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=5)

        lbl = ttk.Label(master=container, text=label, width=10)
        lbl.pack(side=LEFT, padx=5)

        # validation function
        def validate_input(value):
            if value == "" or self.is_valid_number(value):
                ent.configure(bootstyle="default")  # reset to default style
                return True
            else:
                ent.configure(bootstyle="danger")  # set red outline
                return False

        # register the validation function
        validate_cmd = self.register(validate_input)

        # entry field with validation
        ent = ttk.Entry(
            master=container,
            textvariable=variable,
            validate="key",
            validatecommand=(validate_cmd, "%P"),  # %P passes the current value of the entry
        )
        ent.pack(side=LEFT, padx=5, fill=X, expand=YES)

    def is_valid_number(self, value):
        # check if the value is a valid number
        if value == "-": # ok to start with a minus sign
            return True
        elif value == ".": # ok to start with a decimal point 
            return True
        elif value == "-.": # ok to start with a minus sign and decimal point
            return True
        try:
            float(value)  # try converting to a float
            return True
        except ValueError:
            return False

    def create_buttonbox(self):
        # button box and impedance entry field
        container = ttk.Frame(self)
        container.pack(fill=X, expand=YES, pady=(15, 10))

        # label for the impedance entry field
        lbl_impedance = ttk.Label(master=container, text="Impedance", width=10)
        lbl_impedance.pack(side=LEFT, padx=5)

        # entry field to the left of the buttons
        self.impedance_var = ttk.StringVar(value="50")
        self.impedance = ttk.Entry(master=container, textvariable=self.impedance_var, width=10)
        self.impedance.pack(side=LEFT, padx=5)

        cnl_btn = ttk.Button(
            master=container,
            text="Clear",
            command=self.on_clear,
            bootstyle=DANGER,
            width=8,
        )
        cnl_btn.pack(side=RIGHT, padx=5)

        sub_btn = ttk.Button(
            master=container,
            text="Calculate",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=8,
        )
        sub_btn.pack(side=RIGHT, padx=5)

    def on_submit(self):
        # calculate the values based on which field is filled
        try:
            if self.modified_field == "vpp" and self.vpp.get():
                vpp = float(self.vpp.get())
                vrms = vpp / (2 * math.sqrt(2))  # Vpp to Vrms
                mw = (vrms ** 2 * 10 ** 3) / float(self.impedance_var.get())  # Vrms to mW
                dbm = 10 * math.log10(mw)  # mW to dBm

                self.vrms.set(f"{vrms:.6g}")
                self.mw.set(f"{mw:.6g}")
                self.dbm.set(f"{dbm:.6g}")

            elif self.modified_field == "vrms" and self.vrms.get():
                vrms = float(self.vrms.get())
                vpp = vrms * (2 * math.sqrt(2))  # Vrms to Vpp
                mw = (vrms ** 2 * 10 ** 3) / float(self.impedance_var.get())  # Vrms to mW
                dbm = 10 * math.log10(mw)  # mW to dBm

                self.vpp.set(f"{vpp:.6g}")
                self.mw.set(f"{mw:.6g}")
                self.dbm.set(f"{dbm:.6g}")

            elif self.modified_field == "mw" and self.mw.get():
                mw = float(self.mw.get())
                vrms = math.sqrt(mw / 10 ** 3 * float(self.impedance_var.get()))  # mW to Vrms
                vpp = vrms * (2 * math.sqrt(2))  # Vrms to Vpp
                dbm = 10 * math.log10(mw)  # mW to dBm

                self.vpp.set(f"{vpp:.6g}")
                self.vrms.set(f"{vrms:.6g}")
                self.dbm.set(f"{dbm:.6g}")

            elif self.modified_field == "dbm" and self.dbm.get():
                dbm = float(self.dbm.get())
                mw = 10 ** (dbm / 10)  # dBm to mW
                vrms = math.sqrt(mw / 10 ** 3 * float(self.impedance_var.get()))  # mW to Vrms
                vpp = vrms * (2 * math.sqrt(2))  # Vrms to Vpp

                self.vpp.set(f"{vpp:.6g}")
                self.vrms.set(f"{vrms:.6g}")
                self.mw.set(f"{mw:.6g}")

        except ValueError:
            pass # do nothing

    def on_clear(self):
        # clear all data entry fields 
        self.vpp.set("")
        self.vrms.set("")
        self.mw.set("")
        self.dbm.set("")
        self.modified_field = None  # reset the modified field

def resource_path(relative_path):
    # get absolute path to icon resource
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# sets the theme for the title bar
def apply_theme_to_titlebar(root):
    version = sys.getwindowsversion()

    # uncomment the lines below to set the title bar color to match the theme

    if version.major == 10 and version.build >= 22000:
        # set dark title bar
        pywinstyles.change_header_color(root, "#1c1c1c")
        # set light title bar
        #pywinstyles.change_header_color(root, "#fafafa")
    elif version.major == 10:
        # set dark title bar
        pywinstyles.apply_style(root, "dark")
        # set light title bar
        #pywinstyles.apply_style(root, "normal")

        # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
        root.wm_attributes("-alpha", 0.99)
        root.wm_attributes("-alpha", 1)

if __name__ == "__main__":
    app = ttk.Window("CW Voltage-Power Calculator", "darkly", resizable=(False, False))
    #icon = tk.PhotoImage(file="D:\Projects\CW-Voltage-Power-Calculator\icon.png") # use this if running as python script
    #app.iconphoto(False, icon) # use this if running as python script
    icon_path = resource_path("icon.png") # use this if running as .exe
    app.iconphoto(False, tk.PhotoImage(file=icon_path)) # use this if running as .exe
    ttk.Window.place_window_center(app) 
    DataEntryForm(app)

    # apply theme to the title bar
    apply_theme_to_titlebar(app)

    app.mainloop()
