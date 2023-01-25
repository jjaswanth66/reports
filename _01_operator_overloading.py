# this is not a complete implementation
# only for demo, just to see which method will be called
# Arithmetic Operators
class Demo:
    def __add__(self, other):               # +
        print("You are in __add__() method.")

    def __sub__(self, other):               # -
        print("You are in __sub__() method.")

    def __mul__(self, other):               # *
        print("You are in __mul__() method.")

    def __matmul__(self, other):            # @
        print("You are in __matmul__() method.")

    def __truediv__(self, other):           # /
        print("You are in __truediv__() method.")

    def __div__(self, other):           # for Python 2
        print("You are in __div__() method.")

    def __floordiv__(self, other):          # //
        print("You are in __floordiv__() method.")

    def __mod__(self, other):               # %
        print("You are in __mod__() method.")

    def __pow__(self, other):               # **
        print("You are in __pow__() method")


x = Demo()
y = Demo()

x + y       # left_operand -> self, right_operand -> other
            # left_operand -> self -> current object
x.__add__(y)

x - y       # x.__sub__(y)
x.__sub__(y)

x * y       # x.__mul__(y)

x @ y       # x.__matmul__(y)

x / y

x // y

x % y

x ** y