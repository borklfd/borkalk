import tkinter
import tkinter.font
import backend
import keyboard
import time
import threading


class CGui:
    def __init__(self):
        self.cwindow = tkinter.Tk()
        self.cwindow.title("borKalk")
        self.cwindow.resizable(False, False)
        self.cwindow.iconphoto(False, tkinter.PhotoImage(file="./icon.png"))
        self.calc = backend.Calc()
        self.btnH = 1
        self.btnW = 3
        self.font = tkinter.font.Font(font=["Franklin Gothic Medium", 15])
        self.labelfont = tkinter.font.Font(font=["Franklin Gothic Medium", 15])
        self.resVar = tkinter.StringVar()
        self.errortext = tkinter.StringVar()
        self.errortext.set("errors here")
        self.resVar.set(0)
        self.keyer = threading.Thread(target=self.keywatcher, daemon=True)
        self.__buildgui()

    def __buildgui(self):
        """creates the buttons& labels. not pretty but works"""
        self.btn1 = tkinter.Button(self.cwindow, text="1", command=lambda: self.on_press(1),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn2 = tkinter.Button(self.cwindow, text="2", command=lambda: self.on_press(2),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn3 = tkinter.Button(self.cwindow, text="3", command=lambda: self.on_press(3),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn4 = tkinter.Button(self.cwindow, text="4", command=lambda: self.on_press(4),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn5 = tkinter.Button(self.cwindow, text="5", command=lambda: self.on_press(5),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn6 = tkinter.Button(self.cwindow, text="6", command=lambda: self.on_press(6),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn7 = tkinter.Button(self.cwindow, text="7", command=lambda: self.on_press(7),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn8 = tkinter.Button(self.cwindow, text="8", command=lambda: self.on_press(8),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btn9 = tkinter.Button(self.cwindow, text="9", command=lambda: self.on_press(9),
                                   height=self.btnH, width=self.btnW, font=self.font)

        self.btnC = tkinter.Button(self.cwindow, text="C", command=lambda: self.on_press("c"),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btnDel = tkinter.Button(self.cwindow, text="DEL", command=lambda: self.on_press("backspace"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnSqrt = tkinter.Button(self.cwindow, text="√", command=lambda: self.on_press("sqrt"),
                                      height=self.btnH, width=self.btnW, font=self.font)

        self.btnDiv = tkinter.Button(self.cwindow, text="/", command=lambda: self.on_press("/"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnMul = tkinter.Button(self.cwindow, text="*", command=lambda: self.on_press("*"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnSub = tkinter.Button(self.cwindow, text="-", command=lambda: self.on_press("-"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnAdd = tkinter.Button(self.cwindow, text="+", command=lambda: self.on_press("+"),
                                     height=self.btnH, width=self.btnW, font=self.font)

        self.btn0 = tkinter.Button(self.cwindow, text="0", command=lambda: self.on_press(0),
                                   height=self.btnH, width=self.btnW, font=self.font)
        self.btnDec = tkinter.Button(self.cwindow, text=".", command=lambda: self.on_press("."),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnInv = tkinter.Button(self.cwindow, text="±", command=lambda: self.on_press("i"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnEnt = tkinter.Button(self.cwindow, text="ENTER", command=lambda: self.on_press("enter"),
                                     height=self.btnH, width=self.btnW*2, font=self.font)

        self.btnMem = tkinter.Button(self.cwindow, text="M", command=lambda: self.on_press("m"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.btnMre = tkinter.Button(self.cwindow, text="MR", command=lambda: self.on_press("r"),
                                     height=self.btnH, width=self.btnW, font=self.font)
        self.console = tkinter.Label(self.cwindow, textvariable=self.resVar, font=self.labelfont,
                                     height=self.btnH, width=self.btnW*5, anchor="e", relief="sunken", bg="ivory4", fg="honeydew2")
        self.__arrange()

    def __arrange(self):
        self.btn1.grid(row=4, column=0)
        self.btn2.grid(row=4, column=1)
        self.btn3.grid(row=4, column=2)
        self.btn4.grid(row=3, column=0)
        self.btn5.grid(row=3, column=1)
        self.btn6.grid(row=3, column=2)
        self.btn7.grid(row=2, column=0)
        self.btn8.grid(row=2, column=1)
        self.btn9.grid(row=2, column=2)
        self.btnC.grid(row=1, column=0)
        self.btnDel.grid(row=1, column=1)
        self.btnSqrt.grid(row=1, column=2)
        self.btnDiv.grid(row=1, column=3)
        self.btnMul.grid(row=2, column=3)
        self.btnSub.grid(row=3, column=3)
        self.btnAdd.grid(row=4, column=3)
        self.btn0.grid(row=5, column=0)
        self.btnDec.grid(row=5, column=1)
        self.btnInv.grid(row=5, column=2)
        self.btnEnt.grid(row=5, column=3, columnspan=3, sticky="e"+"w")
        self.btnMem.grid(row=1, column=5)
        self.btnMre.grid(row=2, column=5)
        self.console.grid(row=0, column=0, columnspan=6, sticky="e"+"w")

    def on_press(self, press):
        self.calc.newdigit(press)
        self.console["font"] = self.labelfont
        if self.calc.final is not None:
            self.resVar.set(self.calc.final.value())
            finalstr = str(self.calc.final.value())
            if len(finalstr) < 15:
                self.labelfont.config(size=self.font.cget("size"))
            else:
                self.labelfont.config(size=self.font.cget("size")**2//len(finalstr)+1)

        else:
            self.resVar.set(self.calc.active.value())

    def keywatcher(self):
        while True:
            time.sleep(0.15)
            self.on_press(keyboard.read_key())

    def output(self, number):
        if number == int(number):
            number = int(number)
        if len(str(number)) > 14:
            return "%.14f" % number
        else:
            return number

    def loop(self):
        self.keyer.start()
        self.cwindow.mainloop()
