from tkinter import *
win=Tk()

def check1():
  ''' print("first",check_1.get())
   print("first",check_2.get())'''
  l1.config(text=check_1.get()+" "+check_2.get())
   
    
    
check_1=StringVar()
check_2=StringVar()
    
c1=Checkbutton(win,text="dancing",variable=check_1,onvalue="dancing",offvalue="",command=check1)
c1.grid(row=5,column=1)
c2=Checkbutton(win,text="learning",variable=check_2,onvalue="learning",offvalue="",command=check1)
c2.grid(row=5,column=2)
l1=Label(win)
l1.grid(row=6,column=0)
