import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

# GUI
window = Tk()
window.title("Simple Backup app")
label1 = Label(window, text="Επιλέξτε φακέλους πηγής και προορισμού:", font=('Arial Bold', 15))
label1.grid(column=0, row=0)


def set_source():
    global source
    source = askdirectory(title='Select Source Directory')
    source_input.insert(END, source)


def set_dest():
    global destination
    destination = askdirectory(title='Select Destination Directory')
    dest_input.insert(END, destination)


def xcopy_backup():
    src = source.replace("/", "\\")
    dst = destination.replace("/", "\\")
    print(src)
    print(dst)
    print("Starting copy... ")
    os.system(f"\"xcopy \"{src}\" \"{dst}\" /v /f /d /i /e /r /h /j /y > logfile.txt\"")
    messagebox.showinfo("Backup Complete", "Μπορείτε να δείτε τα αποτελέσματα στο logfile.txt")


label2 = Label(window, text="Αντέγραψε τα αρχεία από:")
label2.grid(column=1, row=1)
label3 = Label(window, text="Στον προορισμό:")
label3.grid(column=1, row=2)
source_input = Entry(window, width=30)
dest_input = Entry(window, width=30)
source_input.grid(column=2, row=1)
dest_input.grid(column=2, row=2)
button_source = Button(window, text="Browse", command=set_source)
button_dest = Button(window, text="Browse", command=set_dest)
button_source.grid(column=3, row=1)
button_dest.grid(column=3, row=2)

button_do = Button(window, text="GO", command=xcopy_backup)
button_do.grid(column=2, row=3)

window.mainloop()
