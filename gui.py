#simple window to enter in files

#imports
import tkinter as tk
import tkinter.filedialog as fd 
import main as m

#vars
rowfile = ""
colfile = ""
valsfile = ""
outputfile = ""

def getRowPath():
    global rowfile
    global row_entry
    rowfile = fd.askopenfilename()
    row_entry.insert(0, rowfile)
    return rowfile

def getColPath():
    global colfile
    global col_entry
    colfile = fd.askopenfilename()
    col_entry.insert(0, colfile)
    return colfile

def getValPath():
    global valsfile
    global val_entry
    valsfile = fd.askopenfilename()
    val_entry.insert(0, valsfile)
    return valsfile

def saveToPath():
    global outputfile
    global build_entry
    outputfile = fd.asksaveasfilename(filetypes=[("Excel Files", "*.xlsx")])
    outputfile += ".xlsx"
    build_entry.insert(0, outputfile)
    return outputfile

def clear_all():
    global row_entry, col_entry, val_entry, build_entry, rowfile, colfile, valsfile, outputfile
    row_entry.delete(0, tk.END)
    col_entry.delete(0, tk.END)
    val_entry.delete(0, tk.END)
    build_entry.delete(0, tk.END)
    rowfile = ""
    colfile = ""
    valsfile = ""
    outputfile = ""

#build GUI
root = tk.Tk()
frame = tk.Frame(root)
viewer_frame = tk.Frame(frame, padx=5, pady=10, bg="lightblue")
button_frame = tk.Frame(frame, height=25, padx=5, pady=10, bg = "blue")

row_lab = tk.Label(viewer_frame, text="Row Path:", bg="lightblue")
col_lab = tk.Label(viewer_frame, text="Column Path:", bg="lightblue")
val_lab = tk.Label(viewer_frame, text="Values Path:", bg="lightblue")
out_lab = tk.Label(viewer_frame, text="Output Path:", bg="lightblue")

row_entry = tk.Entry(viewer_frame, width= 60)
col_entry = tk.Entry(viewer_frame, width = 60)
val_entry = tk.Entry(viewer_frame, width = 60)
build_entry = tk.Entry(viewer_frame, width = 60)

rowfile_button = tk.Button(button_frame, text="Rows File", width=10, command=getRowPath)
colfile_button = tk.Button(button_frame, text="Column File", width=10, command=getColPath)
valsfile_button = tk.Button(button_frame, text= "Values File", width = 10, command=getValPath)
save_to_button = tk.Button(button_frame, text="Save To", width = 10, command= saveToPath)
tocsv_button = tk.Button(button_frame, text="Build", width=10, command=lambda:m.toCSV(rowfile, colfile, valsfile, outputfile))
clear_button = tk.Button(button_frame, text="Clear", width=10, command=clear_all)

#set basic window properties
root.geometry('600x400')
root.title('Text-To-CSV-Inator!')
icon = tk.PhotoImage(file="res/doof.png")
root.iconphoto(True, icon)


frame.grid(row=0, column=0, padx=10, pady=10, sticky=('NSEW'))
viewer_frame.grid(row=0, column=0, padx=10, pady=5, sticky=('NSEW'))
row_lab.grid(row=1, column=1, padx=5, pady=5)
col_lab.grid(row=2, column=1, padx=5, pady=5)
val_lab.grid(row=3, column=1, padx=5, pady=5)
out_lab.grid(row=4, column=1, padx=5, pady=5)
row_entry.grid(row=1, column=2, padx=5, pady=5)
col_entry.grid(row=2, column=2, padx=5, pady=5)
val_entry.grid(row=3, column=2, padx=5, pady=5)
build_entry.grid(row=4, column=2, padx=5, pady=5)

button_frame.grid(row=1, column=0, padx=10, pady=5, sticky=('NSEW'))
rowfile_button.grid(row=0,column=1, padx=5, pady=5)
colfile_button.grid(row=0,column=2, padx=5, pady=5)
valsfile_button.grid(row= 0, column=3, padx= 5, pady= 5)
save_to_button.grid(row=0, column=4, padx=5, pady= 5)
tocsv_button.grid(row=0, column=5, padx = 5, pady = 5)
clear_button.grid(row=0, column=6, padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

viewer_frame.columnconfigure(0, weight=1)
viewer_frame.rowconfigure(0, weight=1)

button_frame.columnconfigure(0, weight=1)
button_frame.rowconfigure(0, weight=1)
root.mainloop()