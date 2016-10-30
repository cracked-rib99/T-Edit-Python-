#!/usr/bin/python
import Tkinter
import tkFileDialog
import tkColorChooser

window = Tkinter.Tk()

Status = Tkinter.StringVar()
Status.set('Status::                           ')

File_name = Tkinter.StringVar()
File_name.set("No File Opened...")

File_name2 = Tkinter.StringVar()
File_name2.set("No File Opened...")

Author = Tkinter.StringVar()
Author.set("Made By Teodorescu Tudor")

Version = Tkinter.StringVar()
Version.set("Version 0.60 ALPHA")

BuildDate = Tkinter.StringVar()
BuildDate.set('Build Date: October 03 21:45')

window.geometry("1024x680")
window.title("T-Edit Text Editor (Python) V0.60 ALPHA")
window.minsize(width=1024, height=680, )
window.maxsize(width=1024, height=680, )
window.resizable(width=False, height=False, )
window.config(background="#383838", )


def file_dialog():
    print "opening file dialog...."
    file = tkFileDialog.askopenfile(
        parent=window,
        mode='rb',
        title='Select a file',
        defaultextension=".txt",
        filetypes=(
            ("All Files", "*.*"),
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
        textfield.delete("0.0", "end")
        textfield.insert('1.0', contents + " ")
        file.close()
    Status.set("Done!                           ")
    File_name.set(file)


def options():
    option = Tkinter.Toplevel()
    option.geometry("300x400")
    option.config(background="#383838",)
    option.title("T-Edit -Options")
    option.resizable(width=False, height=False,)

    def close():
        option.destroy()

    def dark_theme_button_clicked():
        window.config(background="#383838",)
        textfield.config(
            bg="#262626",
            fg="white",
            insertbackground="#006eef",

        )

        new_btn.config(
            text="NEW",
            command=new_window,
            relief="flat",
            bg="#006EFF",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        open_btn.config(
            text="OPEN",
            command=file_dialog,
            relief="flat",
            bg="#006EFF",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        save_btn.config(
            text="SAVE",
            command=save_dialog,
            relief="flat",
            bg="#006EFF",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        save_as_btn.config(
            text="SAVE AS",
            command=save_as_dialog,
            relief="flat",
            bg="#006EFF",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        clear_btn.config(
            text="CLEAR",
            command=clear_text,
            relief="flat",
            bg="#006EFF",
            fg="white",
            highlightthickness=0,
            bd=0,
            padx=10,

        )

        color_btn.config(
            text="HEX COLOR CODES",
            command=color_dialog,
            relief="flat",
            bg="#006eef",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        info_btn.config(
            text="ABOUT",
            command=showinfo,
            relief="flat",
            bg="#006EFF",
            fg="white",
            anchor="e",
            highlightthickness=0,
            bd=0,

        )

        exit_btn.config(
            text="EXIT",
            command=exit_command,
            relief="flat",
            bg="#2F8F2F",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        undo_btn.config(
            text="UNDO",
            command=undo_command,
            relief="flat",
            bg="#006eef",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        redo_btn.config(
            text="REDO",
            command=redo_command,
            relief="flat",
            bg="#006eef",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        options_btn.config(
            text="OPTIONS",
            command=options,
            relief="flat",
            bg="#006eef",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        status_lbl.config(
            text=Status,
            relief="flat",
            bg="#006eef",
            fg="white",
            textvariable=Status,
            height=1,
            justify="center",

        )

        file_name_lbl.config(
            bg="#006EFF",
            fg="white",
            textvariable=File_name,
            height=1,
            justify="center",

        )

    def light_theme_button_clicked():
        window.config(background="#dedede",)
        textfield.config(
            fg="black",
            bg="white",
            insertbackground="black",

        )

        new_btn.config(
            bg="#00BFFF",
            fg="white",
            text="NEW",
            relief="flat",
            command=new_window,

        )

        open_btn.config(
            text="OPEN",
            command=file_dialog,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        save_btn.config(
            text="SAVE",
            command=save_dialog,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        save_as_btn.config(
            text="SAVE AS",
            command=save_as_dialog,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        clear_btn.config(
            text="CLEAR",
            command=clear_text,
            relief="flat",
            bg="#00BFFF",
            fg="white",
            padx=10,

        )

        color_btn.config(
            text="HEX COLOR CODES",
            command=color_dialog,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        info_btn.config(
            text="ABOUT",
            command=showinfo,
            relief="flat",
            bg="#00BFFF",
            fg="white",
            anchor="e",

        )

        exit_btn.config(
            text="EXIT",
            command=exit_command,
            relief="flat",
            bg="red",
            fg="white",

        )

        undo_btn.config(
            text="UNDO",
            command=undo_command,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        redo_btn.config(
            text="REDO",
            command=redo_command,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        options_btn.config(
            text="OPTIONS",
            command=options,
            relief="flat",
            bg="#00BFFF",
            fg="white",

        )

        status_lbl.config(
            text=Status,
            relief="flat",
            bg="#00BFFF",
            fg="white",
            textvariable=Status,
            height=1,
            justify="center",

        )

        file_name_lbl.config(
            bg="#00BFFF",
            fg="white",
            textvariable=File_name,
            height=1,
            justify="center",

        )

    def pastel_theme_button_clicked():
        window.config(background="hotpink",)
        textfield.config(
            bg="purple",
            fg="cyan",
            insertbackground="hotpink",

        )

        new_btn.config(
            text="NEW",
            command=new_window,
            relief="flat",
            bg="purple",
            fg="cyan",
            highlightthickness=0,
            bd=0,

        )

        open_btn.config(
            text="OPEN",
            command=file_dialog,
            relief="flat",
            bg="purple",
            fg="cyan",
            highlightthickness=0,
            bd=0,

        )

        save_btn.config(
            text="SAVE",
            command=save_dialog,
            relief="flat",
            bg="purple",
            fg="cyan",
            highlightthickness=0,
            bd=0,

        )

        save_as_btn.config(
            text="SAVE AS",
            command=save_as_dialog,
            relief="flat",
            bg="purple",
            fg="cyan",
            highlightthickness=0,
            bd=0,

        )

        clear_btn.config(
            text="CLEAR",
            command=clear_text,
            relief="flat",
            bg="purple",
            fg="cyan",
            highlightthickness=0,
            bd=0,
            padx=10,

        )

        color_btn.config(
            text="HEX COLOR CODES",
            command=color_dialog,
            relief="flat",
            bg="purple",
            fg="cyan",
            highlightthickness=0,
            bd=0,

        )

        info_btn.config(
            text="ABOUT",
            command=showinfo,
            relief="flat",
            bg="purple",
            fg="cyan",
            anchor="e",
            highlightthickness=0,
            bd=0,

        )

        exit_btn.config(
            text="EXIT",
            command=exit_command,
            relief="flat",
            bg="cyan",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        undo_btn.config(
            text="UNDO",
            command=undo_command,
            relief="flat",
            bg="purple",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        redo_btn.config(
            text="REDO",
            command=redo_command,
            relief="flat",
            bg="purple",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        options_btn.config(
            text="OPTIONS",
            command=options,
            relief="flat",
            bg="purple",
            fg="white",
            highlightthickness=0,
            bd=0,

        )

        status_lbl.config(
            text=Status,
            relief="flat",
            bg="purple",
            fg="cyan",
            textvariable=Status,
            height=1,
            justify="center",

        )

        file_name_lbl.config(
            bg="purple",
            fg="cyan",
            textvariable=File_name,
            height=1,
            justify="center",

        )

    def programmers_theme_clicked():
        window.config(background="#161616",)
        textfield.config(
            fg="#05fc09",
            bg="black",
            insertbackground="#05fc09",

        )

        new_btn.config(
            bg="black",
            fg="#05fc09",
            text="NEW",
            relief="flat",
            command=new_window,

        )

        open_btn.config(
            text="OPEN",
            command=file_dialog,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        save_btn.config(
            text="SAVE",
            command=save_dialog,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        save_as_btn.config(
            text="SAVE AS",
            command=save_as_dialog,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        clear_btn.config(
            text="CLEAR",
            command=clear_text,
            relief="flat",
            bg="black",
            fg="#05fc09",
            padx=10,

        )

        color_btn.config(
            text="HEX COLOR CODES",
            command=color_dialog,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        info_btn.config(
            text="ABOUT",
            command=showinfo,
            relief="flat",
            bg="black",
            fg="#05fc09",
            anchor="e",

        )

        exit_btn.config(
            text="EXIT",
            command=exit_command,
            relief="flat",
            bg="red",
            fg="white",

        )

        undo_btn.config(
            text="UNDO",
            command=undo_command,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        redo_btn.config(
            text="REDO",
            command=redo_command,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        options_btn.config(
            text="OPTIONS",
            command=options,
            relief="flat",
            bg="black",
            fg="#05fc09",

        )

        status_lbl.config(
            text=Status,
            relief="flat",
            bg="black",
            fg="#05fc09",
            textvariable=Status,
            height=1,
            justify="center",

        )

        file_name_lbl.config(
            bg="black",
            fg="#05fc09",
            textvariable=File_name,
            height=1,
            justify="center",

        )

    option_close = Tkinter.Button(
        option,
        text="Close",
        height="2",
        justify="center",
        padx="130",
        command=close,
        bg="#006EFF",
        fg="white",
        font="sans",
        relief="flat",
        highlightthickness=0,
        bd=0,
    )

    option_lbl = Tkinter.Label(
        option,
        padx="120",
        pady="10",
        fg="white",
        bg="#006eff",
        text="OPTIONS",
        font="sans",
    )

    dark_theme = Tkinter.Button(
        option,
        text="Dark-Blue(Default)",
        relief="flat",
        command=dark_theme_button_clicked,
        bg="#006eef",
        fg="white",
        font="sans",
        highlightthickness=0,
        bd=0,
        padx="90",
    )

    light_theme = Tkinter.Button(
        option,
        text="Light-Blue",
        relief="flat",
        bg="#00bfff",
        fg="white",
        font="sans",
        command=light_theme_button_clicked,
        highlightthickness=0,
        bd=0,
        padx="110",
    )

    pastel_theme = Tkinter.Button(
        option,
        text="Vapourwave Theme",
        relief="flat",
        bg="purple",
        fg="cyan",
        font="sans",
        command=pastel_theme_button_clicked,
        highlightthickness=0,
        bd=0,
        padx="80",
    )

    programmer_theme = Tkinter.Button(
        option,
        text="Programmers Theme",
        relief="flat",
        bg="black",
        fg="#05fc09",
        command=programmers_theme_clicked,
        font="monoscape",
        highlightthickness=0,
        bd=0,
        padx="70",

    )

    theme_label = Tkinter.Label(
        option,
        text="Themes",
        bg="#00BFFF",
        fg="white",
        font="sans",
        padx="120",

    )

    font_label = Tkinter.Label(
        option,
        text="Fonts",
        bg="#00BFFF",
        fg="white",
        font="sans",
        padx="130",

    )

    font_label.place(x=0, y=40,)
    theme_label.place(x=0, y=212,)
    option_lbl.place(x=0, y=0,)
    programmer_theme.place(x=0, y=235,)
    pastel_theme.place(x=0, y=265,)
    dark_theme.place(x=0, y=295)
    light_theme.place(x=0, y=324,)
    option_close.place(x=0, y=353,)

# ----------------------------------------------------------


def save_as_dialog():
    Status.set("Saving...                       ")
    file = tkFileDialog.asksaveasfile(
        parent=window,
        mode='w',
        defaultextension=".txt",
        filetypes=(
            ("All Files", "*.*"),
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
        data = textfield.get('0.0', "end" + '-1c')
        file.write(data)
        file.close()
    Status.set("Done!                           ")


def save_dialog():
    Status.set("Saving...                       ")
    file = tkFileDialog.asksaveasfile(
        parent=window,
        mode='w',
        title="Save",
        defaultextension=".txt",
        filetypes=(
            ("All Files", "*.*"),
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
        Status.set("Done!                           ")
        data = textfield.get('0.0', "end" + '-1c')
        file.write(data)
        file.close()
    Status.set("Done!                           ")


def color_dialog():
    tkColorChooser.askcolor()


def clear_text():
    print "Textfield Cleared!"
    Status.set('Cleared!                      ')
    window.update()
    File_name.set("No File Opened")
    textfield.delete("0.0", "end")


def undo_command():
    textfield.edit_modified()
    textfield.edit_undo()
    Status.set("Undoing...                    ")


def redo_command():
    textfield.edit_modified()
    textfield.edit_redo()
    Status.set("Redoing...                    ")


def exit_command():
    dialog = Tkinter.Toplevel()
    dialog.title("T-Edit -Exit")
    dialog.focus_set()
    dialog.config(background="#383838")
    dialog.geometry("456x200")
    dialog.resizable(width=False, height=False,)

    def close_dialog():
        dialog.destroy()

    def quit_application():
        window.destroy()

    exit_lbl = Tkinter.Label(
        dialog,
        text="Are You Sure?",
        font="sans",
        bg="#383838",
        fg="white",
        padx="0",
        pady="0",
    )

    exit_lbl.config(font=("sans", 29))
    yes_btn = Tkinter.Button(
        dialog,
        text="YES",
        bg="red",
        fg="white",
        font="sans",
        relief="flat",
        command=quit_application,
        height="3",
        width="15",
        highlightthickness="0",
        bd="0",
    )

    no_btn = Tkinter.Button(
        dialog,
        text="NO",
        bg="#006eef",
        fg="white",
        font="sans",
        relief="flat",
        command=close_dialog,
        height="3",
        width="15",
        highlightthickness="0",
        bd="0",
    )

    note_lbl = Tkinter.Label(
        dialog,
        text="Warning: The Documents Will NOT Be Saved Automatically!",
        height="5",
        width="57",
        fg="white",
        bg="#006eef",
        justify="left"
    )

    note_lbl.place(x=0, y=128,)
    no_btn.place(x=283, y=61,)
    yes_btn.place(x=283, y=0,)
    exit_lbl.place(x=5, y=50,)


def showinfo():

    info = Tkinter.Toplevel()
    info.title("About")
    info.focus_set()
    info.geometry("400x500")
    info.config(background="#383838",)
    info.resizable(width=False, height=False,)

    def close_dialog():
        info.destroy()
        Status.set("Closed...           ")

    name = Tkinter.Label(
        info,
        text="T-Edit",
        relief="flat",
        font="sans",
        bg="#006eef",
        fg="#383838",
        padx="120",
        pady="0",
    )

    name.config(font=("sans", 45))
    name.place(x=0, y=0,)

    sub_name = Tkinter.Label(
        info,
        text="Python Edition",
        relief="flat",
        font="sans",
        bg="#00BFFF",
        fg="#383838",
        padx="120",
        pady="0",
    )

    sub_name.place(x=0, y=72,)
    sub_name.config(font=("sans", 20))

    ver = Tkinter.Label(
        info,
        textvariable=Version,
        relief="flat",
        font="sans",
        bg="#006eef",
        fg="#383838",
        padx="68",
        pady="5",
    )

    ver.config(font=("sans", 20))

    date_lbl = Tkinter.Label(
        info,
        textvariable=BuildDate,
        relief="flat",
        font="sans",
        bg="#ff1a1a",
        fg="white",
        padx="90",
        pady="5",
    )

    author = Tkinter.Label(
        info,
        textvariable=Author,
        relief="flat",
        font="sans",
        bg="#00BFFF",
        fg="#383838",
        padx="18",
        pady="0",
    )

    close_btn = Tkinter.Button(
        info,
        text="Close",
        relief="flat",
        font="sans",
        fg="white",
        bg="#006eef",
        padx="0",
        pady="0",
        command=close_dialog,
        width="40",
        height="2",
        highlightthickness=0,
        bd=0,
    )

    author.place(x=0, y=150,)

    author.config(font=("sans", 20))

    ver.place(x=0, y=106, )

    close_btn.place(x=0, y=460,)

    date_lbl.place(x=0, y=429,)


def new_window():
    exwindow = Tkinter.Toplevel()
    exwindow.geometry("1024x680")
    exwindow.title("T-Edit Text Editor V0.60 ALPHA Python Edition (Extended Window)")
    exwindow.focus_set()
    exwindow.minsize(width=1024, height=680,)
    exwindow.maxsize(width=1024, height=680,)
    exwindow.resizable(width=False, height=False,)
    exwindow.config(bg="#383838")
    Status.set('New Window Created!    ')
    exwindow.update()

    def file_dialog2():
        print "opening file dialog...."
        file = tkFileDialog.askopenfile(
            parent=exwindow,
            mode='rb',
            title='Select a file',
            defaultextension=".txt",
            filetypes=(
                ("All Files", "*.*"),
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
            text_field2.delete("0.0", "end")
            text_field2.insert('1.0', contents + " ")
            file.close()
        Status.set("Done!                           ")
        File_name2.set(file)


    def options2():
        option2 = Tkinter.Toplevel()
        option2.geometry("300x400")
        option2.config(background="#383838", )
        option2.title("T-Edit -Options")
        option2.resizable(width=False, height=False, )

        def close():
            option2.destroy()

        def dark_theme_button_clicked():
            exwindow.config(background="#383838", )
            text_field2.config(
                bg="#262626",
                fg="white",
                insertbackground="#006eef",

            )

            open_btn.config(
                text="OPEN",
                command=file_dialog2,
                relief="flat",
                bg="#006EFF",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            save_btn.config(
                text="SAVE",
                command=save_dialog2,
                relief="flat",
                bg="#006EFF",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            save_as_btn.config(
                text="SAVE AS",
                command=save_as_dialog,
                relief="flat",
                bg="#006EFF",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            clear_btn.config(
                text="CLEAR",
                command=clear_text2,
                relief="flat",
                bg="#006EFF",
                fg="white",
                highlightthickness=0,
                bd=0,
                padx=10,

            )

            color_btn.config(
                text="HEX COLOR CODES",
                command=color_dialog2,
                relief="flat",
                bg="#006eef",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            info_btn.config(
                text="ABOUT",
                command=showinfo2,
                relief="flat",
                bg="#006EFF",
                fg="white",
                anchor="e",
                highlightthickness=0,
                bd=0,

            )

            exit_btn.config(
                text="EXIT",
                command=close_exwindow,
                relief="flat",
                bg="#2F8F2F",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            undo_btn.config(
                text="UNDO",
                command=undo_command2,
                relief="flat",
                bg="#006eef",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            redo_btn.config(
                text="REDO",
                command=redo_command2,
                relief="flat",
                bg="#006eef",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            options_btn.config(
                text="OPTIONS",
                command=options2,
                relief="flat",
                bg="#006eef",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            status_lbl.config(
                text=Status,
                relief="flat",
                bg="#006eef",
                fg="white",
                textvariable=Status,
                height=1,
                justify="center",

            )

            file_name_lbl.config(
                bg="#006EFF",
                fg="white",
                textvariable=File_name,
                height=1,
                justify="center",

            )

        def light_theme_button_clicked():
            window.config(background="#dedede", )
            textfield.config(
                fg="black",
                bg="white",
                insertbackground="black",

            )

            new_btn.config(
                bg="#00BFFF",
                fg="white",
                text="NEW",
                relief="flat",
                command=new_window,

            )

            open_btn.config(
                text="OPEN",
                command=file_dialog,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            save_btn.config(
                text="SAVE",
                command=save_dialog,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            save_as_btn.config(
                text="SAVE AS",
                command=save_as_dialog,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            clear_btn.config(
                text="CLEAR",
                command=clear_text,
                relief="flat",
                bg="#00BFFF",
                fg="white",
                padx=10,

            )

            color_btn.config(
                text="HEX COLOR CODES",
                command=color_dialog,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            info_btn.config(
                text="ABOUT",
                command=showinfo,
                relief="flat",
                bg="#00BFFF",
                fg="white",
                anchor="e",

            )

            exit_btn.config(
                text="EXIT",
                command=exit_command,
                relief="flat",
                bg="red",
                fg="white",

            )

            undo_btn.config(
                text="UNDO",
                command=undo_command,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            redo_btn.config(
                text="REDO",
                command=redo_command,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            options_btn.config(
                text="OPTIONS",
                command=options,
                relief="flat",
                bg="#00BFFF",
                fg="white",

            )

            status_lbl.config(
                text=Status,
                relief="flat",
                bg="#00BFFF",
                fg="white",
                textvariable=Status,
                height=1,
                justify="center",

            )

            file_name_lbl.config(
                bg="#00BFFF",
                fg="white",
                textvariable=File_name,
                height=1,
                justify="center",

            )

        def pastel_theme_button_clicked():
            window.config(background="hotpink", )
            textfield.config(
                bg="purple",
                fg="cyan",
                insertbackground="hotpink",

            )

            new_btn.config(
                text="NEW",
                command=new_window,
                relief="flat",
                bg="purple",
                fg="cyan",
                highlightthickness=0,
                bd=0,

            )

            open_btn.config(
                text="OPEN",
                command=file_dialog,
                relief="flat",
                bg="purple",
                fg="cyan",
                highlightthickness=0,
                bd=0,

            )

            save_btn.config(
                text="SAVE",
                command=save_dialog,
                relief="flat",
                bg="purple",
                fg="cyan",
                highlightthickness=0,
                bd=0,

            )

            save_as_btn.config(
                text="SAVE AS",
                command=save_as_dialog,
                relief="flat",
                bg="purple",
                fg="cyan",
                highlightthickness=0,
                bd=0,

            )

            clear_btn.config(
                text="CLEAR",
                command=clear_text,
                relief="flat",
                bg="purple",
                fg="cyan",
                highlightthickness=0,
                bd=0,
                padx=10,

            )

            color_btn.config(
                text="HEX COLOR CODES",
                command=color_dialog,
                relief="flat",
                bg="purple",
                fg="cyan",
                highlightthickness=0,
                bd=0,

            )

            info_btn.config(
                text="ABOUT",
                command=showinfo,
                relief="flat",
                bg="purple",
                fg="cyan",
                anchor="e",
                highlightthickness=0,
                bd=0,

            )

            exit_btn.config(
                text="EXIT",
                command=exit_command,
                relief="flat",
                bg="cyan",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            undo_btn.config(
                text="UNDO",
                command=undo_command,
                relief="flat",
                bg="purple",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            redo_btn.config(
                text="REDO",
                command=redo_command,
                relief="flat",
                bg="purple",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            options_btn.config(
                text="OPTIONS",
                command=options,
                relief="flat",
                bg="purple",
                fg="white",
                highlightthickness=0,
                bd=0,

            )

            status_lbl.config(
                text=Status,
                relief="flat",
                bg="purple",
                fg="cyan",
                textvariable=Status,
                height=1,
                justify="center",

            )

            file_name_lbl.config(
                bg="purple",
                fg="cyan",
                textvariable=File_name,
                height=1,
                justify="center",

            )

        def programmers_theme_clicked():
            window.config(background="#161616", )
            textfield.config(
                fg="#05fc09",
                bg="black",
                insertbackground="#05fc09",

            )

            new_btn.config(
                bg="black",
                fg="#05fc09",
                text="NEW",
                relief="flat",
                command=new_window,

            )

            open_btn.config(
                text="OPEN",
                command=file_dialog,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            save_btn.config(
                text="SAVE",
                command=save_dialog,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            save_as_btn.config(
                text="SAVE AS",
                command=save_as_dialog,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            clear_btn.config(
                text="CLEAR",
                command=clear_text,
                relief="flat",
                bg="black",
                fg="#05fc09",
                padx=10,

            )

            color_btn.config(
                text="HEX COLOR CODES",
                command=color_dialog,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            info_btn.config(
                text="ABOUT",
                command=showinfo,
                relief="flat",
                bg="black",
                fg="#05fc09",
                anchor="e",

            )

            exit_btn.config(
                text="EXIT",
                command=exit_command,
                relief="flat",
                bg="red",
                fg="white",

            )

            undo_btn.config(
                text="UNDO",
                command=undo_command,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            redo_btn.config(
                text="REDO",
                command=redo_command,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            options_btn.config(
                text="OPTIONS",
                command=options,
                relief="flat",
                bg="black",
                fg="#05fc09",

            )

            status_lbl.config(
                text=Status,
                relief="flat",
                bg="black",
                fg="#05fc09",
                textvariable=Status,
                height=1,
                justify="center",

            )

            file_name_lbl.config(
                bg="black",
                fg="#05fc09",
                textvariable=File_name,
                height=1,
                justify="center",

            )

        option_close = Tkinter.Button(
            option,
            text="Close",
            height="2",
            justify="center",
            padx="130",
            command=close,
            bg="#006EFF",
            fg="white",
            font="sans",
            relief="flat",
            highlightthickness=0,
            bd=0,
        )

        option_lbl = Tkinter.Label(
            option,
            padx="120",
            pady="10",
            fg="white",
            bg="#006eff",
            text="OPTIONS",
            font="sans",
        )

        dark_theme = Tkinter.Button(
            option,
            text="Dark-Blue(Default)",
            relief="flat",
            command=dark_theme_button_clicked,
            bg="#006eef",
            fg="white",
            font="sans",
            highlightthickness=0,
            bd=0,
            padx="90",
        )

        light_theme = Tkinter.Button(
            option,
            text="Light-Blue",
            relief="flat",
            bg="#00bfff",
            fg="white",
            font="sans",
            command=light_theme_button_clicked,
            highlightthickness=0,
            bd=0,
            padx="110",
        )

        pastel_theme = Tkinter.Button(
            option,
            text="Vapourwave Theme",
            relief="flat",
            bg="purple",
            fg="cyan",
            font="sans",
            command=pastel_theme_button_clicked,
            highlightthickness=0,
            bd=0,
            padx="80",
        )

        programmer_theme = Tkinter.Button(
            option,
            text="Programmers Theme",
            relief="flat",
            bg="black",
            fg="#05fc09",
            command=programmers_theme_clicked,
            font="monoscape",
            highlightthickness=0,
            bd=0,
            padx="70",

        )

        theme_label = Tkinter.Label(
            option,
            text="Themes",
            bg="#00BFFF",
            fg="white",
            font="sans",
            padx="120",

        )

        font_label = Tkinter.Label(
            option,
            text="Fonts",
            bg="#00BFFF",
            fg="white",
            font="sans",
            padx="130",

        )

        font_label.place(x=0, y=40, )
        theme_label.place(x=0, y=212, )
        option_lbl.place(x=0, y=0, )
        programmer_theme.place(x=0, y=235, )
        pastel_theme.place(x=0, y=265, )
        dark_theme.place(x=0, y=295)
        light_theme.place(x=0, y=324, )
        option_close.place(x=0, y=353, )

    # ----------------------------------------------------------

    def save_dialog2():
        print("Job:: Save")
        Status.set("Saving...                       ")
        file = tkFileDialog.asksaveasfile(
            parent=exwindow,
            mode='w',
            title="Save",
            defaultextension=".txt",
            filetypes=(
                ("All Files", "*.*"),
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
            data = text_field2.get('0.0', "end" + '-1c')
            file.write(data)
            file.close()
        Status.set("Done!                       ")
        pass

    def color_dialog2():
        color = tkColorChooser.askcolor(parent=exwindow)
        text_field2.insert(color)
        pass

    def clear_text2():
        print "Text Cleared!"
        Status.set('Status:: Cleared!   ')
        exwindow.update()
        text_field2.delete("0.0", "end")
        pass

    def showinfo2():
        info2 = Tkinter.Toplevel()
        info2.title("About")
        info2.focus_set()
        info2.geometry("400x500")
        info2.config(background="#383838",)
        info2.resizable(width=False, height=False,)
        pass

        def close_dialog2():
            info2.destroy()
            Status.set("Closed...")
            pass

        name = Tkinter.Label(
            info2,
            text="T-Edit",
            relief="flat",
            font="sans",
            bg="#006eef",
            fg="#383838",
            padx="120",
            pady="0",
        )

        name.config(font=("sans", 45))
        name.place(x=0, y=0,)

        sub_name = Tkinter.Label(
            info2,
            text="Python Edition",
            relief="flat",
            font="sans",
            bg="#3BBF3B",
            fg="#383838",
            padx="120",
            pady="0",
        )

        sub_name.place(x=0, y=72,)
        sub_name.config(font=("sans", 20))

        version = Tkinter.Label(
            info2,
            textvariable=Version,
            relief="flat",
            font="sans",
            bg="#006eef",
            fg="#383838",
            padx="68",
            pady="5",
        )

        date_lbl2 = Tkinter.Label(
            info2,
            textvariable=BuildDate,
            relief="flat",
            font="sans",
            bg="#ff1a1a",
            fg="white",
            padx="90",
            pady="5",

        )

        author_lbl2 = Tkinter.Label(
            info2,
            textvariable=Author,
            relief="flat",
            font="sans",
            bg="#00BFFF",
            fg="#383838",
            padx="18",
            pady="0",

        )

        close_info_btn2 = Tkinter.Button(
            info2,
            text="Close",
            relief="flat",
            font="sans",
            fg="white",
            bg="#006eef",
            padx="0",
            pady="0",
            command=close_dialog2,
            width="40",
            height="2",
            highlightthickness=0,
            bd=0,

        )

        author_lbl2.place(x=0, y=150)

        version.config(font=("sans", 20))

        author_lbl2.config(font=("sans", 20))

        close_info_btn2.place(x=0, y=460)

        date_lbl2.place(x=0, y=429)

        version.place(x=0, y=106)

    def undo_command2():
        text_field2.edit_modified()
        text_field2.edit_undo()

    def redo_command2():
        text_field2.edit_modified()
        text_field2.edit_redo()

    def close_exwindow():
        exwindow.destroy()

    open_btn2 = Tkinter.Button(
        exwindow,
        text="OPEN",
        command=file_dialog2,
        relief="flat",
        bg="#006EFF",
        fg="white",
        highlightthickness="0",
        bd="0",
    )

    save_btn2 = Tkinter.Button(
        exwindow,
        text="SAVE",
        command=save_dialog2,
        relief="flat",
        bg="#006EFF",
        fg="white",
        highlightthickness="0",
        bd="0",
    )

    color_btn2 = Tkinter.Button(
        exwindow,
        text="COLOR",
        command=color_dialog2,
        relief="flat",
        bg="#006eef",
        fg="white",
        highlightthickness="0",
        bd="0",
    )

    clear_btn2 = Tkinter.Button(
        exwindow,
        text="CLEAR",
        command=clear_text2,
        relief="flat",
        bg="#006EFF",
        fg="white",
        highlightthickness="0",
        bd="0",
        padx=15,
    )

    info_btn2 = Tkinter.Button(
        exwindow,
        text="ABOUT",
        command=showinfo2,
        relief="flat",
        bg="#006EFF",
        fg="white",
        anchor="e",
        highlightthickness="0",
        bd="0",
        padx=15,
    )

    undo_btn2 = Tkinter.Button(
        exwindow,
        text="UNDO",
        command=undo_command2,
        relief="flat",
        bg="#006eef",
        fg="white",
        highlightthickness="0",
        bd="0",
    )

    redo_btn2 = Tkinter.Button(
        exwindow,
        text="REDO",
        command=redo_command2,
        relief="flat",
        bg="#006eef",
        fg="white",
        highlightthickness="0",
        bd="0",
    )

    close_btn2 = Tkinter.Button(
        exwindow,
        text="CLOSE",
        command=close_exwindow,
        relief="flat",
        bg="#006eef",
        fg="white",
        highlightthickness="0",
        bd="0",
    )

    text_field2 = Tkinter.Text(
        exwindow,
        width=102,
        height=33,
        bg="#262626",
        fg="white",
        relief="flat",
        font="sans",
        insertbackground="#006eff",
        yscrollcommand="yscrollbar.set",
        undo=True,
        highlightthickness="0",
    )

    status_lbl2 = Tkinter.Label(
        exwindow,
        text=Status,
        relief="flat",
        bg="#006EFF",
        fg="white",
        textvariable=Status,
        height=1,
    )
    
    file_name_lbl2 = Tkinter.Label(
        exwindow,
        bg="#006eff",
        fg="white",
        textvariable=File_name2,
        height=1,
        justify="center",
    )

    y_scrollbar2 = Tkinter.Scrollbar(
        exwindow,
        orient="vertical",
        command=textfield.yview(),
        activebackground="#383838",
    )

    y_scrollbar2.config(
        relief="flat",
        command=textfield.yview,
    )

    textfield.config()

    open_btn2.place(x=0, y=0, )

    save_btn2.place(x=55, y=0, )

    clear_btn2.place(x=110, y=0, )

    info_btn2.place(x=893, y=0, )

    text_field2.place(x=0, y=26, )

    file_name_lbl2.place(x=160, y=658, )

    status_lbl2.place(x=0, y=658, )

    undo_btn2.place(x=240, y=0, )

    redo_btn2.place(x=300, y=0, )

    color_btn2.place(x=178, y=0, )

    close_btn2.place(x=960, y=0, )


new_btn = Tkinter.Button(
    window,
    text="NEW",
    command=new_window,
    relief="flat",
    bg="#006EFF",
    fg="white",
    highlightthickness=0,
    bd=0,
)

open_btn = Tkinter.Button(
    window,
    text="OPEN",
    command=file_dialog,
    relief="flat",
    bg="#006EFF",
    fg="white",
    highlightthickness=0,
    bd=0,
)

save_btn = Tkinter.Button(
    window,
    text="SAVE",
    command=save_dialog,
    relief="flat",
    bg="#006EFF",
    fg="white",
    highlightthickness=0,
    bd=0,
)

save_as_btn = Tkinter.Button(
    window,
    text="SAVE AS",
    command=save_as_dialog,
    relief="flat",
    bg="#006EFF",
    fg="white",
    highlightthickness=0,
    bd=0,
)

color_btn = Tkinter.Button(
    window,
    text="HEX COLOR CODES",
    command=color_dialog,
    relief="flat",
    bg="#006eef",
    fg="white",
    highlightthickness=0,
    bd=0,
)

clear_btn = Tkinter.Button(
    window,
    text="CLEAR",
    command=clear_text,
    relief="flat",
    bg="#006EFF",
    fg="white",
    highlightthickness=0,
    bd=0,
    padx=10,
)

info_btn = Tkinter.Button(
    window,
    text="ABOUT",
    command=showinfo,
    relief="flat",
    bg="#006EFF",
    fg="white",
    anchor="e",
    highlightthickness=0,
    bd=0,
)

undo_btn = Tkinter.Button(
    window,
    text="UNDO",
    command=undo_command,
    relief="flat",
    bg="#006eef",
    fg="white",
    highlightthickness=0,
    bd=0,
)

redo_btn = Tkinter.Button(
    window,
    text="REDO",
    command=redo_command,
    relief="flat",
    bg="#006eef",
    fg="white",
    highlightthickness=0,
    bd=0,
)

options_btn = Tkinter.Button(
    window,
    text="OPTIONS",
    command=options,
    relief="flat",
    bg="#006eef",
    fg="white",
    highlightthickness=0,
    bd=0,
)

exit_btn = Tkinter.Button(
    window,
    text="EXIT",
    command=exit_command,
    relief="flat",
    bg="#2F8F2F",
    fg="white",
    highlightthickness=0,
    bd=0,
)

textfield = Tkinter.Text(
    window,
    width=102,
    height=33,
    bg="#262626",
    fg="white",
    relief="flat",
    font="sans",
    insertbackground="#006eff",
    yscrollcommand="yscrollbar.set",
    highlightthickness=0,
    bd=0,
    autoseparators=True,
    maxundo="-1",
    undo=True,
)

# ~Keybindings~
'''
textfield.bind("<Control-z>", undo_command)
textfield.bind("<Control-y>", redo_command)
'''

status_lbl = Tkinter.Label(
    window,
    text=Status,
    relief="flat",
    bg="#006EFF",
    fg="white",
    textvariable=Status,
    height=1,
    justify="center",
)

file_name_lbl = Tkinter.Label(
    window,
    relief="flat",
    bg="#006EFF",
    fg="white",
    textvariable=File_name,
    height=1,
    justify="center",
)

y_scrollbar = Tkinter.Scrollbar(
    window,
    orient="vertical",
    command=textfield.yview(),
    activebackground="#383838",
    bg="#006eef",
    troughcolor="#006eef"
)

y_scrollbar.config(
    relief="flat",
    command=textfield.yview,
)

textfield.config()

new_btn.place(x=0, y=0,)

open_btn.place(x=53, y=0,)

save_btn.place(x=110, y=0,)

save_as_btn.place(x=165, y=0,)

clear_btn.place(x=235, y=0,)

color_btn.place(x=295, y=0,)

info_btn.place(x=908, y=0,)

exit_btn.place(x=973, y=0,)

undo_btn.place(x=430, y=0,)

redo_btn.place(x=490, y=0,)

options_btn.place(x=548, y=0,)

textfield.place(x=0, y=26,)

status_lbl.place(x=0, y=658,)

file_name_lbl.place(x=160, y=658,)

window.mainloop()
