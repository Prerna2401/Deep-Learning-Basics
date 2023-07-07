from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Amount: ')
        self.btn1 = Button(win, text='Convert')
        self.lbl2=Label(win, text='Converted Amount: ')
        
        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=250, y=50)
        self.lbl2.place(x=100, y=150)
        self.t2.place(x=250, y=150)
        self.b1=Button(win, text='Rupee to Euro', command=self.convert)
        self.b2=Button(win,text='Euro to Rupee', command=self.convertr)

        self.b1.place(x=100, y=100)
        self.b2.place(x=300, y=100)
        
    def convert(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result = num1 * 0.011
        self.t2.insert(END, str(result)+' Euros')
        
    def convertr(self):
        self.t2.delete(0, 'end')
        num1=int(self.t1.get())
        result = num1 * 86.63
        self.t2.insert(END, str(result)+' Rupees')
    
window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("500x500")
window.mainloop()