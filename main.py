"""
Shell command for disable context menu:
reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve

Shell command for enable context menu:
reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f
"""

from tkinter import *
import tkinter.messagebox as msg
import os
import time
import webbrowser

def callback(event):
    webbrowser.open_new("https://github.com/sametKaplan0")
def classicmenu():
    os.popen('reg.exe add "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /f /ve')
    msg.showinfo(title="Succesfully", message="Don't forget to press the apply button for the changes to be applied!")

def modernmenu():
    os.popen('reg.exe delete "HKCU\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}" /f')
    msg.showinfo(title="Succesfully", message="Don't forget to press the apply button for the changes to be applied!")

def restart():
    os.popen('taskkill /f /im explorer.exe')
    time.sleep(1)
    os.popen('explorer.exe')
    time.sleep(1)
    msg.showinfo(title="Succesfully", message="Changes applied successfully!")

window = Tk()
window.title("W11 Context Menu Editor by Samet Kaplan")
window.geometry("420x100")
classic = Button(text="Classic Menu Design", command=classicmenu)
classic.pack()
modern = Button(text="Modern Menu Design", command=modernmenu)
modern.pack()
rexpl = Button(text="Apply Changes", command=restart)
rexpl.pack()
lbl = Label(window, text="GitHub", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
window.mainloop()
