from module1 import *
from tkinter import*

root=Tk()
root.title("reg")
root.geometry('1000x500')
root.configure(bg="thistle")
root.grab_set()

dobavka1=Button(root,text="Dobavka",width=10,height=3,font="malo_zp",relief="ridge",bg="#00FFFF",command=lambda:dobavka())
udalenie2=Button(root,text="Udalenie",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:udalenie())
mnogo3=Button(root,text="Mnogo_zp",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:mnogozp())
malo4=Button(root,text="Malo_zp",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:malozp())
nalog6=Button(root,text="Nalog",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:nalog())






dobavka1.pack()
udalenie2.pack()
mnogo3.pack()
malo4.pack()
nalog6.pack()

root.mainloop()