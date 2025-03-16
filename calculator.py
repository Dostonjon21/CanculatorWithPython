from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def__init__(self,master):
    master.title("Calculator")  
    master.geometry('357x420+0+0')
    master.config(bg='gray')
    master.resizable(False,False)


    self.equation=StringVar()
    self.entry_value=''
    Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

    Button(width=11, height=4, text='', relief='flat', bg='#fff', command=lambda:self.show('')).place(x=, y=)

    def show(self, value):
        self.entry_value+=str(value)
        self.equation.set(self.entry_value)

        def clear(self):
            self.entry_value=''
            self.equation.set(self.entry_value)


            def solve(self):
                result=eval(self.entry-value)
                self.equation.set(result)

    root=Tk()
    calculator=Calculator(root)
    root.mainloop()