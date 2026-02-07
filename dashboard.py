from tkinter import *
from PIL import Image , ImageTk 
from datetime import datetime



class Clinic:
    def __init__( self , root ):
        self.root = root
        self.root.geometry("1200x650+50+20")
        self.root.resizable(False , False)
        self.root.title(" Heilpraxis")
        self.root.config(bg="#1C2541")

        self.create_widgets()
        self.update_datetime()
    def create_widgets(self):
        self.lbl_date = Label(
            self.root , font=("Poppins" , 28 , "bold"),
            bg="#1C2541" , fg="white", anchor = 'w' ,padx = 25 , pady=10
        )
        self.lbl_date.place(x=0 ,y=0 , width =1200 , height=80)
        sep = Frame(self.root , bg="#6faac4" , height=2)
        sep.place(x=0 , y=60 , width=1200)
       
        footer_height = 40 
        self.footer = Frame(self.root ,bg="#1c2541" , height = footer_height)
        self.footer.place(x=0 , y=650-footer_height , width = 1200)

        self.footer_sep = Frame(self.root, bg="#6faac4" , height=2)
        self.footer_sep.place(x=0 , y=650 - footer_height -2 , width=1200)

        self.footer_lbl = Label(self.footer ,text="© 2026 Heilpraxis | All Rights Reserved",
                                 font = ("Poppins" , 11),bg="#1c2541",fg="#EAF6ff")

        self.footer_lbl.pack(expand= True)
#------------------------ Frame for the Buttons -------------------------
        btn_frame = Frame(self.root ,bd=2,relief=RIDGE,
                        bg='#1C2541' )
        btn_frame.place(x=0 , y=77 , width=200 , height=531)

#----------------------- Image for the above frame -----------------------
        self.menu_img = Image.open("images/1.jpg")
        self.menu_img = self.menu_img.resize((200,230))
        self.menu_img = ImageTk.PhotoImage(self.menu_img)
        lbl_img = Label(btn_frame , image=(self.menu_img))
        lbl_img.pack(side=TOP , fill = X)

    def update_datetime(self):
        now = datetime.now()
        date = now.strftime("%d-%m-%Y")
        time = now.strftime("%H:%M:%S")

        self.lbl_date.config(
            text = f"Bayern Praxis     |     Date : {date}     |      Time : {time}"

        )
        self.lbl_date.after(1000 ,self.update_datetime)
        







if __name__ == "__main__":
    root = Tk()
    obj = Clinic(root)
    root.mainloop()