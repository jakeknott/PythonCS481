from tkinter import *
from string import ascii_lowercase

class Cell(Label):
    """
    Cell class is an extension of a tk label that adds an
    expression, a value, and the name of the cell.
    """

    def __init__(self, parent, expression, value, name):
        """
        Initializes a tk label with height=1, width=15, bg="white", and relief='sunken'.
        :param parent: label parent
        :param expression: Cell's expression
        :param value: Cell's Value
        :param name: Cell's Name
        """
        super().__init__(parent, height=1, width=15, bg="white", bd=1, relief='sunken')


        self.expression = expression
        self.value = value
        self.name = name

class FocusLabel(Label):
    """
    Focus Label is a class that extends tk label and adds a set lable method.
    """
    def __init__(self, parent):
        """
        Initializes a tk label with the defult text of 'a0'.
        :param parent: Parent of the Label
        """
        super().__init__(parent, text='a0:')

    def setLabel(self, label):
        """
        Sets the internal label text.
        :param label: String to set the label text to.
        :return: None
        """
        self.config(text=label)


class Spreadsheet(Frame):
    """
    Spreadsheet class, represents a spread sheet and can update the view.
    And extends the tk Frame.
    """

    def __init__(self, parent, nr=4, nc=4):
        """
        Initializes a spreadsheet with default values of 4 for both the nr and nc.
        :param parent: Parent of the Frame.
        :param nr: Number of rows to add to the spread sheet, default is 4.
        :param nc: Number of columns to add to the spread sheet, default is 4
        """
        super().__init__(parent)
        self.f = Frame(parent)

        parent.bind('<Return>', self.doEval)
        parent.bind('<Tab>', self.doEval)

        self.Cells = list()
        self.SymbolTable = dict()

        self.focusLabel = FocusLabel(parent)
        self.focusEntry = Entry(parent)

        for r in range(0, nr):
            Label(self.f, text=ascii_lowercase[r]).grid(row=r+1, column=0)

            for c in range(0, nc):
                Label(self.f, text=str(c)).grid(row=0, column=c+1, rowspan=1, columnspan=1)

                cell = Cell(self.f, "", None, '{}{}'.format(ascii_lowercase[r], c))
                cell.bind("<ButtonRelease-1>", self.cellClicked)
                cell.grid(row=r + 1, column=c + 1)

                self.Cells.append(cell)

        self.f.grid(row=0, column=0, columnspan=nc+1)

        self.Cells[0].config(bg='yellow')

    def cellClicked(self, event):
        """
        The function that is called when a cell is clicked.
        This will update the background colors of the cells
        and update the label and clear/enter text into the focuse entry.
        :param event:
        :return: None
        """
        for c in self.Cells:
            c.config(bg='white')
        cell = event.widget
        cell.config(bg='yellow')

        self.focusLabel.setLabel("{}:".format(cell.name))

        self.focusEntry.delete(0, END)
        self.focusEntry.insert(0, str(cell.expression))

    def doEval(self, event):
        """
        Will do the evaluation of the cell and update the cells view.
        :param event:
        :return: None
        """
        if self.updateSheet():
            # Update all values
            children = self.f.children
            for key in children:
                child = children[key]
                if type(child) is Cell:
                    child.config(text=child.value)
        else:
            for c in self.Cells:
                if c.name == self.focusLabel.cget("text")[0:-1]:
                    print("error: unable to evaluate cell {} ({})".format(c.name, self.focusEntry.get()))
                    return


    def updateSheet(self):
        """
        Updates the spread sheet's internal values if possible.
        :return: Boolean based on if the values in the cell where updated.
        """

        cell = None

        for c in self.Cells:
            if c.name == self.focusLabel.cget("text")[0:-1]:
                cell = c
                break

        if Cell == None:
            return False

        oldExpr = cell.expression
        oldVal = cell.value


        copySym = dict()

        #Make Copy
        for k in self.SymbolTable:
            copySym[k] = self.SymbolTable[k]

        if copySym.get(cell.name, False):
            del copySym[cell.name]

        while True:
            clean = True
            for c in self.Cells:
                if c is not cell:
                    try:
                        s = eval(c.expression, {}, copySym)

                    except:
                        # failed
                        if copySym.get(c.name, False):
                            del copySym[c.name]
                            clean = False

            if clean:
                break

        try:
            v = eval(self.focusEntry.get(), {}, copySym)
        except:
            return False

        cell.expression = self.focusEntry.get()
        cell.value = v
        self.SymbolTable[cell.name] = v
        self.SymbolTable[cell.name.upper()] = v

        okay = True

        while True:
            done = True
            for c in self.Cells:
                if c is not cell and c.expression is not "":
                    try:
                        v = eval(c.expression, {}, self.SymbolTable)

                        if c.value != v:
                            c.value = v
                            self.SymbolTable[c.name] = v
                            self.SymbolTable[c.name.upper()] = v
                            done = False
                    except:
                        cell.expression = oldExpr
                        cell.value = oldVal
                        self.SymbolTable[c.name] = oldVal
                        self.SymbolTable[c.name.upper()] = oldVal
                        okay = False

            if done:
                break

        return okay


if __name__ == '__main__':
    root = Tk ()
    spreadsheet = Spreadsheet (root)
    spreadsheet.grid(row=0, column =0, columnspan=4)
    spreadsheet.focusLabel.grid ( row =1 , column =0)
    spreadsheet.focusEntry.grid ( row =1 , column =1)
    root.mainloop ()