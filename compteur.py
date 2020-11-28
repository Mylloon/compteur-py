from tkinter import *
import tkinter.font as tkfont

class Compteur:

    def __init__(self):
        self.n = 0
        self.continuer = True
        self.x_n = 0
        self.y_n = 0

    def set_taille(self):
        self.taille = tkfont.Font(size=30)

    def compteur(self):
        self.printN = Label(self.fenetre, text=str(self.n)+"  ", font=self.taille)
        self.printN.place(x=self.x_n, y=self.y_n)
        self.n += 1
        if self.n == 11:
            self.n = 0
        if self.continuer == True:
            self.fenetre.after(100, self.compteur)

    def stop(self):
        if self.continuer == False:
            self.continuer = True
            self.compteur()
            self.stopN = Button(self.fenetre, text="Stop", command=self.stop)
            self.stopN.place(x=100, y=0)
        elif self.continuer == True:
            self.continuer = False
            self.stopN = Button(self.fenetre, text="Start", command=self.stop)
            self.stopN.place(x=100, y=0)

    def start(self):
        self.fenetre = Tk()
        self.fenetre.title("")
        self.fenetre.geometry("150x50")

        self.set_taille()

        self.printN = Label(self.fenetre, text=self.n, font=self.taille)
        self.printN.place(x=self.x_n, y=self.y_n)

        self.stopN = Button(self.fenetre, text="Stop", command=self.stop)
        self.stopN.place(x=100, y=0)

        self.compteur()

        self.fenetre.mainloop()

if __name__ == '__main__':
    Compteur().start()
