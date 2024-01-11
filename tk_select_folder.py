from tkinter import filedialog, Tk  # import GUI module
root = Tk()  # start the GUI
root.withdraw()  # skip the main window

folder_name = filedialog.askdirectory()  # pop up dialog
# also filedialog.askfilename(), etc.

print(f"folder_name: {folder_name}")

