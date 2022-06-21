from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def change(text="type",src="english",dest="hindi"):
     txt1=text
     src1=src
     dest1=dest
     trans=Translator()
     trans1=trans.translate(text,src=src1,dest=dest1)
     return trans1.text

def data():
     s=combo_sor.get()
     d=combo_dest.get()
     msg=sor_txt.get(1.0,END)
     textget=change(text=msg,src=s,dest=d)
     dest_txt.delete(1.0,END)
     dest_txt.insert(END,textget)     


























root=Tk()
root.title("Translator")
root.geometry('500x700+300+250')
root.config(bg="Blue")

lab_text=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="Blue")
lab_text.place(x=80,y=40,width=400,height=50)

frame=Frame(root).pack(side=BOTTOM)
lab_text=Label(root,text="source text",font=("Time New Roman",20,"bold"),bg="Blue",fg="white")
lab_text.place(x=100,y=100,width=300,height=20)

sor_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=120,height=100,width=480)


list_text=list(LANGUAGES.values())


combo_sor=ttk.Combobox(frame,value=list_text)
combo_sor.place(x=10,y=300,height=40,width=100)
combo_sor.set("english")

button_change=Button(frame,text="translate",relief=RAISED,command=data)
button_change.place(x=120,y=300,height=40,width=100)

combo_dest=ttk.Combobox(frame,value=list_text)
combo_dest.place(x=230,y=300,height=40,width=100)
combo_dest.set("english")

lab_text=Label(root,text="dest text",font=("Time New Roman",20,"bold"),bg="Blue",fg="white")
lab_text.place(x=100,y=360,width=480,height=150)
dest_txt=Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=360,height=150,width=480)

root.mainloop()