from tkinter import *
from PIL import ImageTk,Image
from GameControl import *
from ResizeImage import ResizeIMG
       
class StartGameGUI:
    def __init__(self,window):
        self.window=window
        self.PlayerNum=IntVar()
        self.namelist = []
        self.ContinueGame = False
        #set the background
        BackgroundIMG = ResizeIMG('background.jpg',1200, 800)
        SetBackground = Label(self.window,image=BackgroundIMG).place(x=0,y=0)    
        #Set the Initial Welcome Page   
        self.WelcomTXT=Label(self.window, text='Welcome to the Snake and Ladder!',
                              bg='red',height='2',width='26',font=("Times New Roman",35),
                              fg='white')
        self.WelcomTXT.place(x=265,y=150)
        
        self.StartBTN=Button(self.window,command=self.DestroyWelcomePage,text='START GAME',
                                 bg='lightblue',height='1',width='15',font=("Segoe Script",18))
        self.StartBTN.place(x=477,y=500)
        
        self.ExitBTN=Button(self.window,command=self.window.destroy,text='EXIT GAME',
                                 bg='lightblue',height='1',width='15',font=("Segoe Script",18))
        self.ExitBTN.place(x=477,y=600)
        self.window.mainloop()
        
    def DestroyWelcomePage(self):
        self.WelcomTXT.destroy()
        self.StartBTN.destroy()
        self.ExitBTN.destroy()
        self.ChooseNum()
        self.ContinueGame = True
   
    def ChooseNum(self):#Set the Player Number and Name   
        self.ChooseNumFrame=Frame(self.window) 
        self.ChooseNumFrame.place(x=380,y=180)     
        ChooseTXT=Label(self.ChooseNumFrame, text='Choose the number of players',height='2',
                        width='28',font=("Gabriola",30),fg='white',bg='black').pack()

        NumArray=[('Single Player',1),('Two Players',2),('Three Players',3),('Four Players',4)]
        self.PlayerNum.set(1)
        for number,num in NumArray:
            ChooseBTN = Radiobutton(self.ChooseNumFrame,text=number, variable=self.PlayerNum, 
                                    value=num,font=("Times New Roman",20),height=2).pack(anchor="w")
        
        ConfirmBTN=Button(self.ChooseNumFrame,command=self.DestroyChooseNumFrame,text='Confirm',
                          bg='lightblue',height='1',width='9',font=("Segoe Script",20)).place(x=240,y=270)
        
    def DestroyChooseNumFrame(self):
        self.ChooseNumFrame.destroy()
        self.EnterName(self.PlayerNum.get())

    def EnterName(self,PlayerNum):
        self.PlayerNum=PlayerNum
        self.EnterNameFrame=Frame(self.window) 
        self.EnterNameFrame.place(x=474,y=100) 
        
        EnterNameTXT=Label(self.EnterNameFrame, text='Enter the name',
                           height='1',width='16',font=("Gabriola",30),fg='white',bg='black').pack()
            
        self.namelist=[StringVar() for i in range(self.PlayerNum)]    
        for i in range(self.PlayerNum):
            Label(self.EnterNameFrame).pack() 
            PlayerTXT = Label(self.EnterNameFrame,text='Player '+str(i+1),height='1',
                                  font=("Times New Roman",18),bg='yellow').pack()
            Label(self.EnterNameFrame).pack()
            self.EnterPlayerName = Entry(self.EnterNameFrame,textvariable=self.namelist[i],
                                         width='18',font=("Times New Roman",16)).pack()
            
        Label(self.EnterNameFrame).pack()            
        ContinueBTN=Button(self.EnterNameFrame,command=self.SettingEnd,text='Continue',
                          bg='lightblue',height='1',width='8',font=("Segoe Script",15)).pack()
        Label(self.EnterNameFrame).pack()
        
    def SettingEnd(self):
        self.window.destroy()
    
class GameBoardGUI:
    def __init__(self,window,namelist):
        self.window=window
        self.namelist=namelist
        BackgroundIMG = ResizeIMG('background.jpg',1200, 800)
        SetBackground = Label(self.window,image=BackgroundIMG).place(x=0,y=0)       
        self.GameBoard()       
        
    def GameBoard(self):#load the board of the game
        self.GameBoardFrame=Frame(self.window)
        self.GameBoardFrame.place(x=100,y=100)
        BoardImg=ResizeIMG('picture.jpg',600,600)
        SetBoardImg=Label(self.GameBoardFrame,image=BoardImg).pack()
        
        self.Game=GameControl(self.window,self.GameBoardFrame,self.namelist)
        
    def BackOrAgain(self):
        return self.Game.BackOrAgain