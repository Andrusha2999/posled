from module1 import *
from tkinter import*

root=Tk()
root.title("reg")
root.geometry('1000x500')
root.configure(bg="thistle")
root.grab_set()

dobavka=Button(root,text="Dobavka",width=10,height=3,font="malo_zp",relief="ridge",bg="#00FFFF",command=lambda:dobavka())
udalenie=Button(root,text="Udalenie",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:udalenie())
mnogo=Button(root,text="Mnogo_zp",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:mnogo_zp())
malo=Button(root,text="Malo_zp",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:malo_zp())
sred=Button(root,text="Sred",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:sred())
nalog=Button(root,text="Nalog",width=10,height=3,font="Times_New_Roman 15",relief="ridge",bg="#00FFFF",command=lambda:nalog())






dobavka.pack()
udalenie.pack()
mnogo.pack()
malo.pack()
sred.pack()
nalog.pack()

root.mainloop()