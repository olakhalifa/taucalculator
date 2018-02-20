from tkinter import *
import math


master = Tk()
display = Entry(master, width = 12 ,justify = 'right', bd=0, bg= 'lightgray', font = ('Verdana',30))

master.title("Calculator")

class Calculator:
    def __init__(self):
        """
        This method is called when we create our calculator object.
        This will create five variables.
        var1 is the first variable of the calculator.
        result is the result of the last equation
        current is the variable you're on
        operator is the number of the operator (0 is +, 1 is -, 2 is *, 3 is /)
        """
        self.var1 = ""
        self.var2 = ""
        self.result = 0
        self.current = 0
        self.operator = 0

    def num_buttons(self, index):
        """
        This method will take index as a parameter and it will add it to the proper variable.
        So, if current is 0 it will add it to the first variable, otherwide it will just add it to the second variable.
        """
        if self.current is 0:
            display.delete(0, END)
            self.var1 = str(self.var1) + str(index)
            display.delete(0, END)
            display.insert(0, string = self.var1)
        else:
            self.var2 = str(self.var2) + str(index)
            display.delete(0, END)
            display.insert(0, string = self.var2)

    def equate(self):
        """
        This method willl find what operator we're using and it will add, subtract, multiply or divide based off that.
        It will then update the display.
        """
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)
        elif self.operator is 1:
            self.result = float(self.var1) - float(self.var2)
        elif self.operator is 2:
            self.result = float(self.var1) * float(self.var2)
        elif self.operator is 3:
            self.result = float(self.var1) / float(self.var2)
        display.delete(0, END)
        display.insert(0, string = self.result)

    def set_op(self, op):
        """
        This method will set the operator equal to the input and then it will clear the screen.
        It will then set current to the right variable.
        """
        self.operator = op
        if self.current is 0:
            self.current = 1
        else:
            self.equate()
            self.var2 = ""

    def clear(self):
        """
        This method will clear everything and reset the screen and variables.
        """
        self.__init__()
        display.delete(0, END)

calc = Calculator()

b0 = Button(master, text="0", command= lambda: calc.num_buttons(0), width = 4, height= 1,font = ('Comic Sans MS',30))
b1 = Button(master, text="1", command= lambda: calc.num_buttons(1), width = 4, height= 1,font = ('Comic Sans MS',30))
b2 = Button(master, text="2", command= lambda: calc.num_buttons(2), width = 4, height= 1,font = ('Comic Sans MS',30))
b3 = Button(master, text="3", command= lambda: calc.num_buttons(3), width = 4, height= 1,font = ('Comic Sans MS',30))
b4 = Button(master, text="4", command= lambda: calc.num_buttons(4), width = 4, height= 1,font = ('Comic Sans MS',30))
b5 = Button(master, text="5", command= lambda: calc.num_buttons(5), width = 4, height= 1,font = ('Comic Sans MS',30))
b6 = Button(master, text="6", command= lambda: calc.num_buttons(6), width = 4, height= 1,font = ('Comic Sans MS',30))
b7 = Button(master, text="7", command= lambda: calc.num_buttons(7), width = 4, height= 1,font = ('Comic Sans MS',30))
b8 = Button(master, text="8", command= lambda: calc.num_buttons(8), width = 4, height= 1,font = ('Comic Sans MS',30))
b9 = Button(master, text="9", command= lambda: calc.num_buttons(9), width = 4, height= 1,font = ('Comic Sans MS',30))
pi = Button(master, text="π", command= lambda: calc.num_buttons(math.pi), width = 4, height= 1,font = ('Comic Sans MS',30))
tau = Button(master, text="tau", command= lambda: calc.num_buttons(2*math.pi), width = 4, height= 1,font = ('Comic Sans MS',30))
b_dot = Button(master, text=".", command= lambda: calc.num_buttons("."), width = 4, height= 1,font = ('Comic Sans MS',30))
fix = Button(master, text="", width = 4, height= 1,font = ('Comic Sans MS',30))
fix2 = Button(master, text="", width = 4, height= 1,font = ('Comic Sans MS',30))

plus = Button(master, text="+", command= lambda: calc.set_op(0), width = 4, height= 1,font = ('Comic Sans MS',30))
minus = Button(master, text="-", command= lambda: calc.set_op(1), width = 4, height= 1,font = ('Comic Sans MS',30))
times = Button(master, text="x", command= lambda: calc.set_op(2), width = 4, height= 1,font = ('Comic Sans MS',30))
divide = Button(master, text="÷", command= lambda: calc.set_op(3), width = 4, height= 1,font = ('Comic Sans MS',30))

equals = Button(master, text="=", command= calc.equate, width = 4, height= 1,font = ('Comic Sans MS',30))
clear = Button(master, text="c", command= calc.clear, width = 4, height= 1,font = ('Comic Sans MS',30))

# -- Positioning -- #

display.place(x=2, y=2)
fix.grid(row=5, column=2)
fix2.grid(row=6, column=2)
b7.grid(row=2, column=0) 
b8.grid(row=2, column=1) 
b9.grid(row=2, column=2) 
b4.grid(row=3, column=0) 
b5.grid(row=3, column=1) 
b6.grid(row=3, column=2) 
b1.grid(row=4, column=0) 
b2.grid(row=4, column=1) 
b3.grid(row=4, column=2)
b0.grid(row=5, column=0) 
b_dot.grid(row=5, column=1)
clear.grid(row=1, column=3) 
plus.grid(row=2, column=3) 
minus.grid(row=3, column=3) 
times.grid(row=4, column=3) 
divide.grid(row=5, column=3) 
equals.grid(row=6, column=3)
pi.grid(row=6, column=0)
tau.grid(row=6, column=1) 

master.mainloop()


