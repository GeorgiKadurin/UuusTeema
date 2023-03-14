from tkinter import*

k=0
def klikker():
    global k 
    k+=1
    nupp.configure(text=k)
    if k%2==0:
       raam.itemconfig(pildid,image=pilt1)
       
    else:
       raam.itemconfig(pildid,image=pilt2)
       
def text_to_lbl(event):
    text=tekst_kast.get()
    pealkiri.configure(text=text)
    tekst_kast.delete(0,END)

tekst="Aken"
aken=Tk()
aken.geometry("500x700")
aken.title(tekst)
aken.iconbitmap("One-Piece-anime.ico")






pealkiri=Label(aken,
               text="Tkinter põhi elemendid",
               bg="red",
               fg="#6932a8",
               font="Broadway 25",
               height=3,
               width=25)

nupp=Button(aken,
            text="Vajuta mind",
            bg="purple",
            fg="#326ba8",
            font="Broadway 25",
            activebackground="blue",
            activeforeground="black",
            height=3,
            width=20,
            command=klikker)

raam=Canvas(aken,
            width=1000,
            height=800,
            bg="purple")
pilt1=PhotoImage(file="quality.png")
pilt2=PhotoImage(file="quality3.png")
pildid=raam.create_image(2,2,image=pilt1,anchor=NW)

tekst_kast=Entry(aken,
                fg="lightblue",
                bg="grey",
                font="Broadway 25",
                width=20,
                justify=CENTER)
tekst_kast.bind("<Return>",text_to_lbl) #Enter

 
pealkiri.pack()
tekst_kast.pack()
nupp.pack()
raam.pack()

aken.mainloop()













































































