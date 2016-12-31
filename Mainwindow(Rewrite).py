#!/usr/bin/python
import Tkinter
import tkFileDialog
import tkColorChooser
from Tkinter import Toplevel
from Tkinter import Scrollbar
mainwindow = Tkinter.Tk()

Status = Tkinter.StringVar()
Status.set("Idle")

File_name_1 = Tkinter.StringVar()
File_name_1.set("No File Opened")

File_name_2 = Tkinter.StringVar()
File_name_2.set("No File Opened")

Author = Tkinter.StringVar()
Author.set("Tudor Teodorescu")

Version = Tkinter.StringVar()
Version.set("Version 0.60 ALPHA")

BuildDate = Tkinter.StringVar()
BuildDate.set("date goes here")

Color_name = Tkinter.StringVar()
Color_name.set("no color set")

Font_Color_name = Tkinter.StringVar()
Font_Color_name.set("no color set")

Cursor_color_name = Tkinter.StringVar()
Cursor_color_name.set("no color set")

mainwindow.geometry("")
mainwindow.title("T-Edit Python ALPHA")
mainwindow.minsize(width=1024, height=680,)
mainwindow.maxsize(width=1024, height=680,)
mainwindow.resizable(width=True, height=True,)
mainwindow.config(background="#383838")


def quit_app():
    mainwindow.destroy()
    pass


def close_window():
    # window goes here
    pass


def file_dialog_1():
    print "opening file dialog..."
    file = tkFileDialog.askopenfile(
        parent=mainwindow,
        mode="rb",
        title="Choose a file",
        filetypes=(
            ("All Files", "*.*"),
            ("Plain Text File", ".txt"),
            ("HTML File", ".html"),
            ("CSS File", ".css"),
            ("Stylus CSS Script", ".styl"),
            ("Extended Markup Language", ".xml"),
            ("PHP", ".php"),
            ("Python Script", ".py"),
            ("C++ File", ".cpp"),
            ("C++ Header File", ".h"),
            ("CSharp Source", ".cs"),
            ("Java Source", ".java"),
            ("Perl Script", ".prl"),
            ("JavaScript Object Notation File", ".json"),
            ("JavaScript Class Definition", ".cls"),
            ("Java Serverlet", ".do"),
            ("JavaScript Source", ".js"),
            ("Basic Source", ".bas"),
            ("Batch Script", ".bat"),
            ("Shell Script", ".sh"),
            ("Object File", ".o"),
        )
    )
    if file != "":
        contents = file.read()
        textfield_1.delete("0.0", "end")
        textfield_1.insert("1.0", contents)
        print ("file opened!")
        file.close()


def save_1():
    file = tkFileDialog.asksaveasfile(
        parent=mainwindow,
        mode='w',
        defaultextension=".txt",
        filetypes=(
            ("All Files", "*.*"),
            ("Plain Text File", ".txt"),
            ("Hyper Text Markup Language(HTML) File", ".html"),
            ("Cascade Syle Sheet(CSS) File", ".css"),
            ("Stylus CSS Script", ".styl"),
            ("Extended Markup Language(XML)", ".xml"),
            ("PHP", ".php"),
            ("Python Script", ".py"),
            ("C++ File", ".cpp"),
            ("C++ Header File", ".h"),
            ("CSharp(C#) Source", ".cs"),
            ("Java Source", ".java"),
            ("Perl Script", ".prl"),
            ("JavaScript Object Notation File", ".json"),
            ("JavaScript Class Definition", ".cls"),
            ("Java Serverlet", ".do"),
            ("JavaScript Source", ".js"),
            ("Basic Source", ".bas"),
            ("Batch Script", ".bat"),
            ("Shell Script", ".sh"),
            ("Object File", ".o"),
        )
    )
    if file != "":
        Status.set("Done!                           ")
        data = textfield_1.get('0.0', "end" + '-1c')
        file.write(data)
        file.close()


def clear_text():
    textfield_1.delete("0.0", "end")
    print ("Textfield Cleared!")


def undo_command():
    textfield_1.edit_modified()
    textfield_1.edit_undo()
    print "Undone!"


def redo_command():
    textfield_1.edit_modified()
    textfield_1.edit_redo()
    print "Redone!"
    
# ------------------------------------------------------------------------

def exit_dialog():
    exit_dialog_window = Toplevel()
    exit_dialog_window.geometry("300x200")
    exit_dialog_window.resizable(width=False, height=False,)
    exit_dialog_window.config(background="#383838")
    
    def exit_action():
        mainwindow.destroy()

    def cancel_action():
        exit_dialog_window.destroy()

    yes_btn = Tkinter.Button(
        exit_dialog_window,
        text="YES",
        command=exit_action,
        relief="flat",
        bg="#ff7b00",
        fg="white",
        padx="65",
        pady="5",
)
    no_btn = Tkinter.Button(
        exit_dialog_window,
        text="NO",
        command=cancel_action,
        relief="flat",
        bg="red",
        fg="white",
        padx="65",
        pady="5",
)
    dialog_lbl = Tkinter.Label(
        exit_dialog_window,
        text="Are You Sure?",
        fg="white",
        bg="#383838",
        padx="20",
        pady="0",
)
    dialog_lbl.config(font=("sans", 30))
    yes_btn.place(x="0", y="170")
    no_btn.place(x="150", y="170")
    dialog_lbl.place(x="0", y="20")

# -------------------------------------------------------------------------
    
def about_1():
    about = Tkinter.Toplevel()
    about.geometry("300x400")
    about.minsize(width=300, height=400,)
    about.maxsize(width=300, height=400,)
    about.resizable(width=False, height=False,)
    about.config(background="#383838")
    name_lbl = Tkinter.Label(
        about,
        text="T-EDIT TESTING BUILD",
        fg="white",
        bg="#ff7b00",
        font="sans",
        padx="20",
        pady="15",
    )
    name_lbl.config(font=("sans", 45))
    sub_name_lbl = Tkinter.Label(
        about,
        text="Bleeding Edge Version Of T-Edit",
        fg="white",
        bg="ffd400",
        font="sans",
        padx="",
        pady="",
    )
    version_lbl = Tkinter.Label(
        about,
        fg="white",
        bg="007fff",
        font="sans",
        textvariable=Version,
    )
    author_lbl = Tkinter.Label(
        about,
        fg="",
        bg="",
        font="sans",
        textvariable=Author,

    )
    author_lbl.place(x=0, y=0, )
    sub_name_lbl.place(x=0, y=30, )
    version_lbl.place(x=0, y=106, )
    name_lbl.place(x=0, y=0, )


# ----------------------------------------------------------------------


# MAIN UI Elements
textfield_1 = Tkinter.Text(
    mainwindow,
    width=114,
    height=40,
    bg="#262626",
    fg="white",
    relief="flat",
    font="sans",
    insertbackground="#006eff",
    yscrollcommand="textscroll_1.set",
    highlightthickness=0,
    bd=0,
    autoseparators=True,
    maxundo="-1",
    undo=True,
)
textscroll_1 = Scrollbar(
    mainwindow,
    command=textfield_1.yview(),
)
open_btn_1 = Tkinter.Button(
    mainwindow,
    text="OPEN",
    command=file_dialog_1,
    relief="flat",
    bg="#ff7b00",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="5",
)
save_btn_1 = Tkinter.Button(
    mainwindow,
    text="SAVE",
    command=save_1,
    relief="flat",
    bg="#ff7b00",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="5",
)
about_btn_1 = Tkinter.Button(
    mainwindow,
    text="ABOUT",
    command=about_1,
    relief="flat",
    bg="#ff7b00",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="15"
)
clear_text_btn = Tkinter.Button(
    mainwindow,
    text="CLEAR",
    command=clear_text,
    relief="flat",
    bg="#ff7b00",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="5"
)
undo_text_btn = Tkinter.Button(
    mainwindow,
    command=undo_command,
    text="UNDO",
    relief="flat",
    bg="#ff7b00",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="5",   
)
redo_text_btn = Tkinter.Button(
    mainwindow,
    command=redo_command,
    text="REDO",
    relief="flat",
    bg="#ff7b00",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="5", 
)
quit_btn_1 = Tkinter.Button(
    mainwindow,
    command=exit_dialog,
    text="EXIT",
    relief="flat",
    bg="red",
    fg="white",
    font="sans",
    highlightthickness="0",
    bd="0",
    padx="15"
)

# Keybindings
textfield_1.bind("<Control-1>", file_dialog_1)
textfield_1.bind("<Control-2>", save_1)
textfield_1.bind("<Control-3>", )
textfield_1.bind("<Control-4>", )
textfield_1.bind("<Control-5>", )

# UI Placement
open_btn_1.place(x=0, y=0, )
save_btn_1.place(x=61, y=0, )
clear_text_btn.place(x=120, y=0, )
undo_text_btn.place(x=190, y=0, )
redo_text_btn.place(x=250, y=0, )
about_btn_1.place(x=880, y=0, )
quit_btn_1.place(x=962, y=0, )
textfield_1.place(x=0, y=28, )

# The Mainloop (DO NOT DELETE!!!)
mainwindow.mainloop()
