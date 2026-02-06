from tkinter import *
from PIL import Image , ImageTk 



class Clinic:
    def __init__( self , root ):
        self.root = root
        self.root.geometry("1200x650+50+20")
        self.root.resizable(False , False)
        self.root.title(" Bayern Praxis")
        self.root.config(bg="green")

if __name__ == "__main__":
    root = Tk()
    obj = Clinic(root)
    root.mainloop()