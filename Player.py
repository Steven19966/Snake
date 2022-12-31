from tkinter import *
from PIL import ImageTk,Image
import time

class Player:
    def __init__(self, GameBoardFrame, PlayerIMG, playernum, namelist):
        self.totalscore = 0
        self.PlayerIMG = PlayerIMG
        self.PlayerLabel = Label(GameBoardFrame, image=self.PlayerIMG, width=20, height=20)
        self.playernum = playernum
        self.name = namelist
        
        self.mapList={}
        for i in range(10):
            for j in range(10):
                self.mapList[i*10+j+1] = [20+60*j,560-60*i] 

        self.UpAndDownDir = {3: 51, 6: 27, 20: 70, 36: 55, 63: 95, 68: 98, 25: 5, 34: 1, 47: 19, 65: 52,
                                       87: 57, 91: 61, 99: 69}

    def addscore(self, DiceNumber):
        if self.totalscore+DiceNumber <= 100:
            self.totalscore += DiceNumber
        else:
            self.totalscore = self.totalscore

    def move(self):
        self.PlayerLabel.place(x=self.mapList[self.totalscore][0],y=self.mapList[self.totalscore][1])
        if self.totalscore in self.UpAndDownDir.keys():
            time.sleep(0.5)
            self.totalscore = self.UpAndDownDir[self.totalscore]
            self.PlayerLabel.place(x=self.mapList[self.totalscore][0],y=self.mapList[self.totalscore][1])