
# https://www.geogebra.org/calculator
# пропускаем первую строку

from  os import getcwd, path
import tkinter as tk

def on_entry1_paste(event):
    entry1.event_generate("<<Paste>>")

def on_button_click():
  file_n = str(entry1.get())
  full_p = path.join(getcwd(),file_n)
  with open(full_p, 'r') as input_file, open('geo_' + file_n, 'w') as output_file:
    next(input_file)  # пропускаем первую строку
    count = 1
    for line in input_file:
        parts = line.strip().split(',')
        output_line = f"{count},{parts[4]}\n"
        output_file.write(output_line)
        count += 1

root = tk.Tk()
root.title("To Geo...")
label1 = tk.Label(root, text="Set name file with '.csv':")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()
#entry1.bind("<Control-v>", on_entry1_paste)

button = tk.Button(root, text="Get data", command=on_button_click)
button.pack()
root.mainloop()
