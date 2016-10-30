#!/usr/bin/python

import Tkinter
from Tkinter import *
from ScrolledText import *
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className=" T-Edit S")
root.geometry("1280x600")
root.minsize(width=640, height=480,)
textPad = ScrolledText(root, width=100, height=80, bg="#383838", fg="white", font="sans", insertbackground="#006eef",)


def open_command():
    file = tkFileDialog.askopenfile(parent=root, mode='rb', title='Select a file')
    if file != "":
        contents = file.read()
        textPad.insert('1.0', contents)
        file.close()


def save_command(*arga):
    file = tkFileDialog.asksaveasfile(mode='w',)
    if file != "":
        data = textPad.get('1.0', END + '-1c')
        file.write(data)
        file.close()


def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def about_command():
    label = tkMessageBox.showinfo("About", "T-Edit \n An Even Lighter Version Of T-Edit \n Made By:: Tudor Teodorescu")


def clear():
    textPad.delete("0.0", "end")


def undo():
    textPad.edit_modified()
    textPad.edit_undo()


def redo():
    textPad.edit_modified()
    textPad.edit_redo()


def new():
    newwindow = Tkinter.Toplevel()
    newwindow.geometry("1280x600")
    newwindow.title("T-Edit S")
    textPad2 = ScrolledText(newwindow, width=100, height=80, bg="#383838", fg="white", font="sans", insertbackground="#006eef", )

    def open_command2():
        file = tkFileDialog.askopenfile(parent=newwindow, mode='rb', title='Select a file')
        if file != "":
            contents = file.read()
            textPad.insert('1.0', contents)
            file.close()

    def save_command2(*arga):
        file = tkFileDialog.asksaveasfile(mode='w', )
        if file != "":
            data = textPad.get('1.0', END + '-1c')
            file.write(data)
            file.close()

    def exit_command2():
        if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
            root.destroy()

    def about_command2():
        label = tkMessageBox.showinfo("About", "T-Edit Slim\nMadeBy:TudorTeodorescu")

    def clear2():
        textPad2.delete("0.0", "end")

    def undo2():
        textPad2.edit_modified()
        textPad2.edit_undo()

    def redo2():
        textPad2.edit_modified()
        textPad2.edit_redo()

    newwindow.bind("<Control-s>", save_command2)
    newwindow.bind("<Control-c>", clear2)
    newwindow.bind("<Control-k>", )
    newwindow.bind("<Control-i>", )
    newwindow.bind("<Control-x>", exit_command2)
    newwindow.bind("<Control-z>", undo2)
    newwindow.bind("<Control-y>", redo2)

    textPad2.pack(fill="both")

menu = Menu(root)
root.config(menu=menu,)
filemenu = Menu(menu, tearoff="0")
editmenu = Menu(menu, tearoff="0")
menu.add_cascade(label="File", menu=filemenu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Undo", command=undo, )
editmenu.add_command(label="Redo", command=redo, )
editmenu.add_separator()
editmenu.add_command(label="Clear Text Field", command=clear, )
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu, tearoff="0")
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)

textPad.pack(fill="both")

root.mainloop()
