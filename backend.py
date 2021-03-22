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
        except ZeroDivisionError:
            return "Division by 0"
        except TypeError:
            return self.numerator
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
        if self.decimal:
            self.denominator /= 10
        self.numerator -= self.numerator % 10
        self.numerator /= 10


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
        self.final = None
        self.mem = Num()

    def __type(self, data):
        """
        returns the type of data;
        a redundant method that could be
        incorporated into newdigit, but
        I hate overly long functions.
        """
        data = str(data) # data should already be a string, but better safe than sorry...
        if data in "1234567890":  # for digits
            return "n"
        elif data in "+-*/":  # for two-number operations
            return "o"
        elif data == ".":  # for the decimal point
            return "d"
        elif data == "enter":  # for enter/equal sign
            return "e"
        elif data == "c": # for clear or reset
            return "c"
        elif data == "backspace": # for backspace or delete
            return "b"
        elif data == "sqrt": # for the square root
            return "r"
        elif data == "i": # for inversion
            return "i"
        elif data == "m": # for memory
            return "m"
        elif data == "r": # for reading memory
            return "mr"
        else:  # maybe an exception should be raised or idk
            pass

    def newdigit(self, new):
        """
        receives new input, identifies it
        and performs the appropriate operation
        """
        print("numerator1", self.n1.numerator)
        print("denominator1", self.n1.denominator)
        print("value1", self.n1.value())
        print("isDecimal1", self.n1.decimal)
        print("numerator2", self.n2.numerator)
        print("denominator2", self.n2.denominator)
        print("value2", self.n2.value())
        print("isDecimal2", self.n2.decimal)

        new_t = self.__type(new)
        if new_t == "n":  # if new is a digit, appends to the operand
            self.__append(new)
        elif new_t == "o":  # sets operation& switches to next number
            self.__operate(new)
        elif new_t == "d":  # triggers self.__decimal
            self.__decimal()
        elif new_t == "e":  # executes the binomial opeation
            self.__execute()
        elif new_t == "c": # clears/resets the calculator
            self.reinit()
        elif new_t == "b": # retracts the last digit
            self.active.delete()
        elif new_t == "r": # takes the square root of the input
            self.__operate(new)
            self.__execute()
        elif new_t == "i":
            self.active.denominator *= -1
        elif new_t == "m": # writes to memory
            if self.final is None:
                self.__memorise(self.active) # memorises the active user input
            else:
                self.__memorise(self.final) # memorises the result of the previous operation
        elif new_t == "mr": # reads from memory
            self.__recall(self.mem)
        else:   # more can come in the future (exponents, trigonometry, logarithm, etc.)
            pass

    def __append(self, num):
        """appends num to the active operand"""
        if self.final is not None:
            self.reinit()
        if self.active.value() != int(self.active.value()):
            self.active.decimal = True
        else:
            self.decimal = False
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
                self.final.numerator = "No real root"
        else:  # should be elaborated on further
            self.final.numerator = self.n1.numerator
            self.final.denominator = self.n1.denominator
        if self.final.value() >= 0:
            self.final.numerator = abs(self.final.numerator)
            self.final.denominator = abs(self.final.denominator)
        print("numerator1", self.n1.numerator)
        print("denominator1", self.n1.denominator)
        print("value1", self.n1.value())
        print("isDecimal1", self.n1.decimal)
        print("numerator2", self.n2.numerator)
        print("denominator2", self.n2.denominator)
        print("value2", self.n2.value())
        print("isDecimal2", self.n2.decimal)
        print(self.final.value())

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
