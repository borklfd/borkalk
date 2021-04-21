import math


class Num:

    def __init__(self, numerator=0, denominator=1, decimal=False):
        """sets up a new rational number with the value of 0."""
        self.numerator = numerator
        self.denominator = denominator
        self.decimal = decimal

    def value(self):
        """
        returns the ratio of the numerator and the denominator
        of the object as floating-point number.
        """
        try:
            value = self.numerator / self.denominator
        except:
            return "Error"
        else:
            return value

    def reinit(self):
        """
        the exact same as __init__;
        resets all instance variables.
        """
        self.numerator = 0
        self.denominator = 1
        self.decimal = False

    def toolong(self):
        if len(str(self.value())) > 16:
            self.delete()
            return True
        else:
            return False

    def delete(self):
        self.normalise()
        if self.decimal:
            self.denominator /= 10
        self.numerator -= self.numerator % 10
        self.numerator /= 10

    def normalise(self):
        while self.numerator != round(self.numerator):
            self.numerator *= 10
            self.denominator *= 10
        if self.value() != round(self.value()):
            self.decimal = True
        else:
            self.decimal = False

class Calc:
    """
    the main backend for the calculator;
    normally only one instance should be used per program.
    """
    def __init__(self):
        """
        creates the necessary objects needed for the
        program. The calculator currently can work with 1 or 2
        numbers at a time, these are rational instances of the
        Num class.
        """
        self.n1 = Num()
        self.n2 = Num()
        # more n-s may be included in the future
        self.active = self.n1
        self.operation = ""
        self.const = ("Pi", "euler")
        self.final = None
        self.mem = Num()


    def newdigit(self, new):
        """
        receives new input, identifies it
        and performs the appropriate operation
        """

        new = str(new)
        if new in "1234567890":  # if new is a digit, appends to the operand
            self.__append(new)
        elif new in("+", "-", "*", "/", "exp", "log", "sqrt"):
            self.__operate(new)
            if new is "sqrt":
                self.__execute()
        elif new is "enter":  # executes the binomial opeation
            self.__execute()
        elif new is ".":  # triggers self.__decimal
            self.__decimal()
        elif new is "c": # clears/resets the calculator
            self.reinit()
        elif new is "backspace": # retracts the last digit
            self.active.delete()
        elif new is "i":
            self.active.denominator *= -1
        elif new is "m": # writes to memory
            if self.final is None:
                self.__memorise(self.active) # memorises the active user input
            else:
                self.__memorise(self.final) # memorises the result of the previous operation
        elif new is "r": # reads from memory
            self.__recall(self.mem)
        elif new in self.const:
            self.active.reinit()
            if new is "Pi":
                self.active.numerator = math.pi
            elif new is "euler":
                self.active.numerator = math.e
        elif new in ("sin", "cos", "tan", "asin", "acos", "atan"):
            self.final = Num()
            if new is "sin":
                self.final.numerator = math.sin(self.active.value())
            elif new is "cos":
                self.final.numerator = math.cos(self.active.value())
            elif new is "tan":
                self.final.numerator = math.tan(self.active.value())
            elif new is "asin":
                self.final.numerator = math.asin(self.active.value())
            elif new is "acos":
                self.final.numerator = math.acos(self.active.value())
            elif new is "atan":
                self.final.numerator = math.atan(self.active.value())
        else:   # more can come in the future (exponents, trigonometry, logarithm, etc.)
            pass

    def __append(self, num):
        """appends num to the active operand"""
        self.active.normalise()
        if self.final is not None:
            self.reinit()
        num = int(num)
        if self.active.decimal:
            self.active.denominator *= 10
        self.active.numerator = self.active.numerator*10 + num
        self.active.toolong()


    def __operate(self, operation):
        """stores the operation and prepares for the next input"""
        self.operation = operation
        self.active = self.n2

    def __decimal(self):
        """decimal trigger"""
        self.active.decimal = True

    def __execute(self):
        """returns the result of the operation"""
        self.final = Num()
        try:
            for i in (self.n1, self.n2):
                if i.value() >= 0:
                    i.numerator = abs(i.numerator)
                    i.denominator = abs(i.denominator)
                else:
                    i.numerator = 0 - abs(i.numerator)
                    i.denominator = abs(i.denominator)
        except:
            pass
        if self.operation == "+":
            self.final.numerator = (self.n1.numerator*self.n2.denominator) + (self.n2.numerator*self.n1.denominator)
            self.final.denominator = self.n1.denominator*self.n2.denominator
        elif self.operation == "-":
            self.final.numerator = (self.n1.numerator*self.n2.denominator) - (self.n2.numerator*self.n1.denominator)
            self.final.denominator = self.n1.denominator*self.n2.denominator
        elif self.operation == "*":
            self.final.numerator = self.n1.numerator*self.n2.numerator
            self.final.denominator = self.n1.denominator*self.n2.denominator
        elif self.operation == "/":
            self.final.numerator = self.n1.numerator*self.n2.denominator
            self.final.denominator = self.n1.denominator*self.n2.numerator
        elif self.operation == "sqrt":
            try:
                self.final.numerator = math.sqrt(self.n1.numerator)
                self.final.denominator = math.sqrt(self.n1.denominator)
            except ValueError:
                self.final.numerator = "nope"
        elif self.operation == "log":
            self.final.numerator = math.log(self.n2.value(), self.n1.value())
        elif self.operation == "exp":
            self.final.numerator = self.n1.numerator**self.n2.value()
            self.final.denominator = self.n1.denominator**self.n2.value()
        else:  # should be elaborated on further
            self.final.numerator = self.n1.numerator
            self.final.denominator = self.n1.denominator

    def reinit(self):
        """resets to the starting values"""
        self.active = self.n1  # whether the first operand is active (or the second)
        self.n1.reinit()
        self.n2.reinit()
        self.operation = ""
        self.final = None



    def __memorise(self, memo):
        """sets all variables of the
        self.mem object to those of memo
        (which should be an instance of the Num class)"""
        self.mem.numerator = memo.numerator
        self.mem.denominator = memo.denominator
        self.mem.decimal = memo.decimal

    def __recall(self, memo):
        """sets the active Num object to be
        equal to memo (normally )"""
        self.active.numerator = memo.numerator
        self.active.denominator = memo.denominator
        self.active.decimal = memo.decimal
        self.active.toolong()
        self.active.normalise()
