import datetime
import glob
import os
import os.path
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


folder_to_track = os.path.expanduser("~/Desktop")
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        file_type = '/*png'
        files = glob.glob(folder_to_track + file_type)
        for filename in files:
            i = 1
            if filename != game_name:
                new_name = folder_destination + '/' + tag +'.png'
                file_exists = os.path.isfile(new_name)
                while file_exists:
                    i += 1
                    new_name = folder_destination+'/'+tag + str(i) +'.png'
                    file_exists = os.path.isfile(new_name)
                os.rename(filename, new_name)

class game:
    def __init__(self, name):
        self.name = name
        self.time_played = 0
        self.start_time = datetime.time(0,0,0)
        self.end_time = datetime.time(0,0,0)
        self.desktop_path = folder_to_track
        self.game_path = self.desktop_path + '/' + self.name
        os.chdir(self.desktop_path)

    def new_game(self):
        os.mkdir(self.game_path)

    def start_session(self):
        self.start_time = datetime.datetime.now()


class App:
    def __init__(self, root):
        #setting title
        root.title("Hermit Purple")
        #setting window size
        width=1016
        height=300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_60=tk.Label(root)
        GLabel_60["activebackground"] = "#94d4d0"
        GLabel_60["activeforeground"] = "#94d4d0"
        GLabel_60["anchor"] = "center"
        GLabel_60["bg"] = "#94d4d0"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_60["font"] = ft
        GLabel_60["fg"] = "#94d4d0"
        GLabel_60["justify"] = "center"
        GLabel_60["text"] = "background"
        GLabel_60.place(x=0,y=0,width=1015,height=570)
    #Game Name Entry
        self.game_name_var = tk.StringVar(value='')
        self.GLineEdit_534=tk.Entry(root, textvariable=self.game_name_var, font=13, justify=tk.CENTER)
        self.GLineEdit_534["bg"] = "#ffffff"
        self.GLineEdit_534["borderwidth"] = "1px"
        self.GLineEdit_534["cursor"] = "cross"
        ft = tkFont.Font(family='Times',size=22)
        self.GLineEdit_534["font"] = ft
        self.GLineEdit_534["fg"] = "#393d49"
        self.GLineEdit_534["justify"] = "center"
        self.GLineEdit_534["text"] = "Enter Game Name"
        self.GLineEdit_534.place(x=40,y=60,width=277,height=83)
    # New Game
        GButton_202=tk.Button(root)
        GButton_202["activebackground"] = "#fad400"
        GButton_202["activeforeground"] = "#ffffff"
        GButton_202["bg"] = "#ffb800"
        GButton_202["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=16)
        GButton_202["font"] = ft
        GButton_202["fg"] = "#393d49"
        GButton_202["justify"] = "center"
        GButton_202["text"] = "New Game"
        GButton_202.place(x=80,y=170,width=200,height=50)
        GButton_202["command"] = self.GButton_202_command
    # Load Game
        GButton_823=tk.Button(root)
        GButton_823["activebackground"] = "#fad400"
        GButton_823["bg"] = "#ffb800"
        GButton_823["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=16)
        GButton_823["font"] = ft
        GButton_823["fg"] = "#393d49"
        GButton_823["justify"] = "center"
        GButton_823["text"] = "Load Game"
        GButton_823.place(x=80,y=240,width=200,height=50)
        GButton_823["command"] = self.GButton_823_command
    # Tag Name Entry
        self.tag_name_var = tk.StringVar(value='')
        self.GLineEdit_583=tk.Entry(root, textvariable=self.tag_name_var, font=13, justify=tk.CENTER)
        self.GLineEdit_583["bg"] = "#ffffff"
        self.GLineEdit_583["borderwidth"] = "1px"
        self.GLineEdit_583["cursor"] = "cross"
        ft = tkFont.Font(family='Times',size=22)
        self.GLineEdit_583["font"] = ft
        self.GLineEdit_583["fg"] = "#393d49"
        self.GLineEdit_583["justify"] = "center"
        self.GLineEdit_583["text"] = "Enter Tag Name"
        self.GLineEdit_583.place(x=640,y=60,width=350,height=89)
    # Add
        GButton_680=tk.Button(root)
        GButton_680["bg"] = "#fad400"
        GButton_680["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=22)
        GButton_680["font"] = ft
        GButton_680["fg"] = "#393d49"
        GButton_680["justify"] = "center"
        GButton_680["text"] = "Add"
        GButton_680.place(x=770,y=190,width=100,height=60)
        GButton_680["command"] = self.GButton_680_command

        GLabel_34=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_34["font"] = ft
        GLabel_34["fg"] = "#333333"
        GLabel_34["justify"] = "center"
        GLabel_34["text"] = "Enter Game Name"
        GLabel_34.place(x=50,y=20,width=210,height=30)

        GLabel_482=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        GLabel_482["font"] = ft
        GLabel_482["fg"] = "#333333"
        GLabel_482["justify"] = "center"
        GLabel_482["text"] = "Enter Tag Name"
        GLabel_482.place(x=650,y=20,width=220,height=31)
    # New Game
    def GButton_202_command(self):
        global folder_to_track
        folder_to_track = os.path.expanduser("~/Desktop")
        global game_name
        game_name = self.GLineEdit_534.get()
        global folder_destination
        folder_destination = folder_to_track + '/' + game_name
        global app
        app = game(self.GLineEdit_534.get())
        app.new_game()
        app.start_session()
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, folder_to_track, recursive=True)
        observer.start()

    # Load Game
    def GButton_823_command(self):
        global folder_to_track
        folder_to_track = os.path.expanduser("~/Desktop")
        global folder_destination
        folder_destination = filedialog.askdirectory()
        global game_name
        game_name = folder_destination.split('/')[-1]
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, folder_to_track, recursive=True)
        observer.start()

    # Add
    def GButton_680_command(self):
        global tag
        tag = self.GLineEdit_583.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

