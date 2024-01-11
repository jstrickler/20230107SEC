from tkinter import filedialog, Tk
root = Tk()
root.withdraw()

file_name = filedialog.askopenfilename()

print(f"file_name: {file_name}")

