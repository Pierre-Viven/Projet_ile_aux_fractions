from random import shuffle
from tkinter import Button, Canvas, IntVar, LEFT, Label, PhotoImage, TOP, Tk
import pygame

PICT_SIZE=120
PAD=10
SIDE=PICT_SIZE+PAD

NB_LINES=4
NB_COLS=5
WIDTH=SIDE*NB_COLS
HEIGHT=SIDE*NB_LINES
X0=Y0=SIDE//2
NB_PICT=NB_LINES*NB_COLS//2
LANG=['1sur1', '1sur2', '1sur3', '1sur4', '1sur6', '1sur12', 
      '2sur3', '3sur4', '5sur6', '5sur12']

LANG1=['2', '3', '4', '5', '6', '7', 
      '8', '9', '10', '12']

def make_board(n, p):
    P=n*p
    N=P//2
    L=[v % N for v in range(P)]
    shuffle(L)
    board=[[L[line*p+col] for col in range(p)] for line in range(n)]
    return board

class Memory:

    def __init__(self):
        root=Tk()
        root.resizable(False, False)
        root.title("Jeu Memory")
        self.cnv=Canvas(root, width=WIDTH, height=HEIGHT, bg='#0080ff')
        self.cnv.pack(side=LEFT)
        self.cnv.bind("<Button>", self.clic)

        self.btn=Button(root, text="Nouvelle\npartie", 
                        font="Arial 12", command=self.new_game)
        self.btn.pack(side=TOP, padx=20, pady=20)

        self.cpt = IntVar()
        self.lbl=Label(root, textvariable=self.cpt, font="courier 20 bold")
        self.lbl.pack()
        
        pygame.mixer.init()
        pygame.mixer.music.load("son/clap.wav")        

        self.cover = PhotoImage(file="./images/dos.gif")
        self.images=[PhotoImage(file="./images/%s.gif" %filename) 
                     for filename in LANG]
        
        self.new_game()
        
        root.mainloop()

    def fill(self):
        for line in range(NB_LINES):
            for col in range(NB_COLS):
                center=(X0+col*SIDE, Y0+line*SIDE)
                k=self.board[line][col]
                self.cnv.create_image(center, image=self.images[k])
                self.ids_cover[line][col]=self.cnv.create_image(center, 
                                                                image=self.cover)

    def hide(self, i, j, line,col):
        self.ids_cover[i][j]=self.cnv.create_image(X0+j*SIDE, Y0+i*SIDE, 
                                                   image=self.cover)
        self.ids_cover[line][col]=self.cnv.create_image(X0+col*SIDE, 
                                                        Y0+line*SIDE, image=self.cover)
        self.move[0]=self.move[1]=None

    def handle_move(self, line, col):
        item=self.ids_cover[line][col]
        self.cnv.delete(item)
        if self.move[0] is None :
            self.move[0]=(line, col)
        else:
            if self.move[0]==(line, col):
                return
            self.cpt.set(self.cpt.get() + 1)
            self.move[1]=(line, col)
            i, j=self.move[0]
            if self.board[i][j]==self.board[line][col]!=-1:
                self.board[i][j]=self.board[line][col]=-1
                self.move[0]=self.move[1]=None
                self.couples=self.couples+1
                if self.couples==NB_PICT:
                    pygame.mixer.music.play(1)                
            else:
                self.cnv.after(400, self.hide, i, j, line, col)

    def clic(self, event):
        if self.move[1] is not None:
            return
        col, line=event.x//SIDE, event.y//SIDE
        if self.board[line][col]!=-1:
            self.handle_move(line, col)

    def new_game(self):
        self.ids_cover=[[None for j in range(NB_COLS)] for i in range(NB_LINES)]
        self.board=make_board(NB_LINES, NB_COLS)
        self.fill() 
        self.move=[None, None]
        self.couples=0
        self.cpt.set(0)
        pygame.mixer.music.stop()


