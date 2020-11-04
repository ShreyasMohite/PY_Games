from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
import subprocess
import freegames
import threading



class Games:
    def __init__(self,root):
        self.root=root
        self.root.title("Games")
        self.root.geometry("400x300")
        self.root.iconbitmap("logo1064.ico")
        self.root.resizable(0,0)

        games=StringVar()




        def on_enter1(e):
            but_play['background']="black"
            but_play['foreground']="cyan"  
        def on_leave1(e):
            but_play['background']="SystemButtonFace"
            but_play['foreground']="SystemButtonText"
                           

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"


        def clear():
            games.set("Select Game")


        def play():
            try:
                if games.get()!="Select Game":
                    if games.get()=="Snake":
                        subprocess.call("python snakes.py 1", shell=True)
                    if games.get()=="Paint":
                        subprocess.call("python paint.py 1", shell=True)

                    if games.get()=="Maze Game":
                        subprocess.call("python mazegame.py 1", shell=True)

                    if games.get()=="Flappy":
                        subprocess.call("python flappy.py 1", shell=True)
                    

                    if games.get()=="Tic Tac Toe":
                        subprocess.call("python ticitactoe.py 1", shell=True)
                    
                    if games.get()=="Ant":
                        subprocess.call("python ant.py 1", shell=True)

                    if games.get()=="Simon Says":
                        subprocess.call("python simonsays.py 1", shell=True)

                    if games.get()=="Cannon":
                        subprocess.call("python canon.py 1", shell=True)

                    if games.get()=="Bounce":
                        subprocess.call("python bounce.py 1", shell=True)

                    if games.get()=="Pong":
                        subprocess.call("python pong.py 1", shell=True)

                    if games.get()=="Life":
                        subprocess.call("python life.py 1", shell=True)

                    if games.get()=="Tron":
                        subprocess.call("python tron.py 1", shell=True)

                    if games.get()=="Tiles":
                        subprocess.call("python tiles.py 1", shell=True)

                    if games.get()=="Connect Four":
                        subprocess.call("python connectfour.py 1", shell=True)

                    if games.get()=="Memory":
                        subprocess.call("python memory.py 1", shell=True)

                    if games.get()=="Pacman":
                        subprocess.call("python pacman.py 1", shell=True)

                    if games.get()=="Fidget":
                        subprocess.call("python fidget.py 1", shell=True)
                        
                else:
                    tkinter.messagebox.showerror("Error","Please Select Game")

            except Exception as e:
                print(e)

        def thread_play():
            t=threading.Thread(target=play)
            t.start()


#=============== frame ==============================#
        mainframe=Frame(self.root,width=400,height=300,relief="ridge",bd=3,bg="#2c286f")
        mainframe.place(x=0,y=0)

#=====================================================#
        lab_play=Label(mainframe,text="Please Select Game And Click Play Button",font=('times new roman',14),bg="#2c286f",fg="white")
        lab_play.place(x=30,y=10)



        select_game=["Snake","Paint","Maze Game","Flappy","Tic Tac Toe","Ant"\
                    ,"Simon Says","Cannon","Bounce","Pong","Life","Tron","Tiles",\
                      "Connect Four","Memory","Pacman","Fidget"]
        select_game=Combobox(mainframe,values=select_game,font=('arial',14),width=14,state="readonly",textvariable=games)
        select_game.set("Select Game")
        select_game.place(x=110,y=70)


#=====================================================#
        but_play=Button(mainframe,width=15,text="Play",font=('times new roman',12),cursor="hand2",command=thread_play)
        but_play.place(x=120,y=150)
        but_play.bind("<Enter>",on_enter1)
        but_play.bind("<Leave>",on_leave1)

        but_clear=Button(mainframe,width=15,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=120,y=200)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#================================================================#


if __name__ == "__main__":
    root=Tk()
    app=Games(root)
    root.mainloop()
