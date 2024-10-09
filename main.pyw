import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import os

root = tk.Tk()
root.iconbitmap("data\\Icon.ico")
root.title("Hebereke 2 Save Maker")
root.geometry("300x400")

def print_language(language):
    print(f"Selected language: {language}")
def launch_hebereke():
    if hebereke_var.get() == 1:
        messagebox.showinfo("Launching", "Hebereke 2 is launching...")
        subprocess.run(["start", "steam://rungameid/2685090"], shell=True)
    else:
        messagebox.showinfo("Launching", "Hebereke 2 cannot launch. Is it in your Steam library?")
def show_about():
    messagebox.showinfo("About", "Hebereke 2 Save Maker is a tool for Hebereke 2/Ufouria the Saga 2 that allows you to quickly create a save file and launch the game. Intended for those looking to speedrun the game.")
def open_github():
    webbrowser.open_new("https://github.com/MHFsilver")
def hebe_save_path():
    # Find Hebereke 2 save path
    appdata_path = os.getenv('APPDATA')
    target_path = os.path.join(appdata_path, "..", "LocalLow", "SUNSOFT", "HEBEREKE 2")
    # Open File Explorer
    os.startfile(target_path)
def create_file():
    try:
        file_name = "rw.dat"
        appdata_path = os.getenv('APPDATA')
        target_path = os.path.join(appdata_path, "..", "LocalLow", "SUNSOFT", "HEBEREKE 2")
        file_path = os.path.join(target_path, file_name)
        with open(file_path, 'w'):
            pass
        messagebox.showinfo("Complete", f"Your new save has been created!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

languages = ["English", "Japanese", "Spanish", "French", "Italian", "German", "Chinese (Simplified)", "Chinese (Traditional)"]

buttons = []
for language in languages:
    button = tk.Button(root, text=language, command=create_file)
    button.pack(pady=5)
    buttons.append(button)

menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open Save Folder", command=hebe_save_path)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
help_menu.add_command(label="Github",command=open_github)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Checkbox
hebereke_var = tk.IntVar()
hebereke_checkbox = tk.Checkbutton(root, text="Launch Hebereke 2", variable=hebereke_var)
hebereke_checkbox.pack(pady=5)

# Launch button
launch_button = tk.Button(root, text="Launch", command=launch_hebereke)
launch_button.pack(pady=5)

root.mainloop()
