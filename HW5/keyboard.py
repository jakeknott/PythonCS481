qwertyLayout = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
topRow = ["~`", "!1", "@2", "#3", "$4", "%5", "^6", "&7", "*8", "(9", ")0", "_-", "+="]
doubleWidthButtons = {"tab": (1, 0), "caps": (2, 0), "shift": (3,0), "enter": (2,13), "bakspace": (0, 13)}
bottomRow = ["ctrl", "alt", "space", "alt", "ctr"]

import layout

class Keyboard:
    def a(self):
        self.printNormalChar('a')

    def b(self):
        self.printNormalChar('b')

    def c(self):
        self.printNormalChar('c')

    def d(self):
        self.printNormalChar('d')

    def e(self):
        self.printNormalChar('e')

    def f(self):
        self.printNormalChar('f')

    def g(self):
        self.printNormalChar('g')

    def h(self):
        self.printNormalChar('h')

    def i(self):
        self.printNormalChar('i')

    def j(self):
        self.printNormalChar('j')

    def k(self):
        self.printNormalChar('k')

    def l(self):
        self.printNormalChar('l')

    def m(self):
        self.printNormalChar('m')

    def n(self):
        self.printNormalChar('n')

    def o(self):
        self.printNormalChar('o')

    def p(self):
        self.printNormalChar('p')

    def q(self):
        self.printNormalChar('q')

    def r(self):
        self.printNormalChar('r')

    def s(self):
        self.printNormalChar('s')

    def t(self):
        self.printNormalChar('t')

    def u(self):
        self.printNormalChar('u')

    def v(self):
        self.printNormalChar('v')

    def w(self):
        self.printNormalChar('w')

    def x(self):
        self.printNormalChar('x')

    def y(self):
        self.printNormalChar('y')

    def z(self):
        self.printNormalChar('z')

    def openTick(self):
        self.printSpecialChar('`', '~')

    def one(self):
        self.printSpecialChar('1', '!')

    def two(self):
        self.printSpecialChar('2', '@')

    def three(self):
        self.printSpecialChar('3', '#')

    def four(self):
        self.printSpecialChar('4', '$')

    def five(self):
        self.printSpecialChar('5', '%')

    def six(self):
        self.printSpecialChar('6', '^')

    def seven(self):
        self.printSpecialChar('7', '&')

    def eight(self):
        self.printSpecialChar('8', '*')

    def nine(self):
        self.printSpecialChar('9', '(')

    def zero(self):
        self.printSpecialChar('0', ')')

    def minus(self):
        self.printSpecialChar('-', '_')

    def plus(self):
        self.printSpecialChar('=', '+')

    def backspace(self):
        self.callback("\b")

    def tab(self):
        self.callback("\t")

    def openBracket(self):
        self.printSpecialChar('[', '{')

    def closeBracket(self):
        self.printSpecialChar(']', '}')

    def bakSlash(self):
        self.printSpecialChar('\\', '|')

    def cap(self):
        self.isCap = not self.isCap

    def shift(self):
        self.isShifted = not self.isShifted

    def colen(self):
        self.printSpecialChar(';', ':')

    def quote(self):
        self.printSpecialChar('\'', '"')

    def enter(self):
        self.callback('\n')

    def lessthan(self):
        self.printSpecialChar(',', '<')

    def greaterThan(self):
        self.printSpecialChar('.', '>')

    def question(self):
        self.printSpecialChar('/', '?')

    def ctrl(self):
        self.callback("Ctrl")

    def alt(self):
        self.callback("Alt")

    def space(self):
        self.callback(" ")

    def printSpecialChar (self, nocapChar, capChar):
        if self.isShifted:
            self.isShifted = False
            self.callback(capChar)
        else:
            self.callback(nocapChar)

    def printNormalChar(self, char):
        if self.shouldCap():
            return self.callback(char.upper())

        return self.callback(char)

    def shouldCap(self):
        shouldCap = False
        if self.isCap and not self.isShifted:
            # if we are caps and not shifted then we print capital char
            shouldCap = True
        if not self.isCap and self.isShifted:
            shouldCap = True

        if self.isShifted:
            self.isShifted = False

        return shouldCap


    def __init__(self, parent, callback):
        self.options = {'A': self.a, 'B': self.b, 'C': self.c, 'D': self.d, 'E': self.e,
                        'F': self.f, 'G': self.g, 'H': self.h, 'I': self.i, 'J': self.j, 'K': self.k,
                        'L': self.l, 'M': self.m, 'N': self.n, 'O': self.o, 'P': self.p, 'Q': self.q,
                        'R': self.r, 'S': self.s, 'T': self.t, 'U': self.u, 'V': self.v, 'W': self.w,
                        'X': self.x, 'Y': self.y, 'Z': self.z,
                        '~\n`': self.openTick, '!\n1': self.one, '@\n2': self.two, '#\n3': self.three,
                        '$\n4': self.four, '%\n5': self.five, '^\n6': self.six, '&\n7': self.seven, '*\n8': self.eight,
                        '(\n9': self.nine, ')\n0': self.zero, '_\n-': self.minus, '+\n=': self.plus, "Backspace": self.backspace,
                        'Tab': self.tab, '{\n[': self.openBracket, '}\n]': self.closeBracket, '|\n\\': self.bakSlash,
                        'CapsLock': self.cap, ':\n;': self.colen, '"\n\'': self.quote, 'Enter': self.enter, 'Shift': self.shift,
                        '<\n,': self.lessthan, '>\n.': self.greaterThan, '?\n/': self.question, 'Ctrl': self.ctrl,
                        'Alt': self.alt, 'Space': self.space
               }

        self.isShifted = False
        self.isCap = False
        self.callback = callback

        rowNum = 0
        columnNum = 0

        for row in layout.layout:
            for button in row:
                if button[1] is 1:
                    self.b = Button(parent, height=2, width=2)
                else:
                    self.b = Button(parent, height=2, width=button[1] *4)

                self.b.grid(row=rowNum, column=columnNum, columnspan=button[1])
                self.b["text"] = button[0]
                self.b["command"] = self.options[button[0]]

                columnNum += button[1]
            rowNum += 1
            columnNum = 0


if __name__ == "__main__":
    from tkinter import *


    def press(key):
        print(key)

    root = Tk()
    root.title("Keyboard Module Self - Test")
    kbd = Keyboard(root, press)
    root.grid()
    root.mainloop()