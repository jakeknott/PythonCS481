from tkinter import *

class CellArray:

    def __init__(self):
        self.w, self.h = 20, 20
        self.array = [[0 for x in range(self.w)] for y in range(self.h)]

        for i in range(0, self.w):
            for j in range(0, self.h):
                self.array[i][j] = 0

    def step(self):
        copyArray = [[0 for x in range(self.w)] for y in range(self.h)]

        for x in range(0, self.w):
            for y in range(0, self.h):
                if self.array[x][y] == 1:
                    copyArray[x][y] = 1
                else:
                    copyArray[x][y] = 0

        for x in range(0, self.w):
            for y in range(0, self.h):
                neighbors = self.checkNeighbors(x,y)

                if self.array[x][y] == 1:
                    if neighbors < 2 or neighbors > 3:
                        copyArray[x][y] = 0
                else:
                    #cell is alive
                    if neighbors == 3:
                        copyArray[x][y] = 1

        for x in range(0, self.w):
            for y in range(0, self.h):
                if copyArray[x][y] == 1:
                    self.array[x][y] = 1
                else:
                    self.array[x][y] = 0

    def checkNeighbors(self, x, y):
        totalNeightbors = 0

        #first row, cannot go back
        if x != 0:
            if y != 0:
                if self.array[x - 1][y - 1] == 1:
                    totalNeightbors = totalNeightbors + 1

            if self.array[x - 1][y] == 1:
                totalNeightbors = totalNeightbors + 1

            if y != 19:
                if self.array[x - 1][y + 1] == 1:
                    totalNeightbors = totalNeightbors + 1

        # the end cannot go forward
        if x != 19:
            if y != 19:
                if self.array[x + 1][y + 1] == 1:
                    totalNeightbors = totalNeightbors + 1

            if self.array[x + 1][y] == 1:
                totalNeightbors = totalNeightbors + 1

            if y != 0:
                if self.array[x + 1][y - 1] == 1:
                    totalNeightbors = totalNeightbors + 1

        if y != 19:
            if self.array[x][y + 1] == 1:
                totalNeightbors = totalNeightbors + 1

        if y != 0:
            if self.array[x][y - 1] == 1:
                totalNeightbors = totalNeightbors + 1

        if wrapparound.get() and (x == 0 or x == 19 or y == 0 or y == 19):
            # only do checks if something is on the edges
            totalNeightbors += self.checkNeighborsWrap(x, y)

        return totalNeightbors

    def checkNeighborsWrap(self, x, y):
        totalNeightbors = 0

        # first row, cannot go back
        if x == 0:
            if self.array[19][y] == 1:
                totalNeightbors = totalNeightbors + 1

            if y == 19:
                if self.array[19][0] == 1:
                    totalNeightbors = totalNeightbors + 1
            else:
                if self.array[19][y + 1] == 1:
                    totalNeightbors = totalNeightbors + 1

            if y == 0:
                if self.array[19][19] == 1:
                    totalNeightbors = totalNeightbors + 1
            else:
                if self.array[19][y - 1] == 1:
                    totalNeightbors = totalNeightbors + 1


        # the end cannot go forward
        if x == 19:
            if self.array[0][y] == 1:
                totalNeightbors = totalNeightbors + 1

            if y == 19:
                if self.array[0][0] == 1:
                    totalNeightbors = totalNeightbors + 1
            else:
                if self.array[0][y + 1] == 1:
                    totalNeightbors = totalNeightbors + 1

            if y == 0:
                if self.array[0][19] == 1:
                    totalNeightbors = totalNeightbors + 1
            else:
                if self.array[0][y - 1] == 1:
                    totalNeightbors = totalNeightbors + 1

        if y == 0:
            if self.array[x][19] == 1:
                totalNeightbors = totalNeightbors + 1

            if x != 19:
                if self.array[x + 1][19] == 1:
                    totalNeightbors = totalNeightbors + 1

            if x != 0:
                if self.array[x - 1][19] == 1:
                    totalNeightbors = totalNeightbors + 1


        if y == 19:
            if self.array[x][0] == 1:
                totalNeightbors = totalNeightbors + 1

            if x != 19:
                if self.array[x + 1][0] == 1:
                    totalNeightbors = totalNeightbors + 1

            if x != 0:
                if self.array[x - 1][0] == 1:
                    totalNeightbors = totalNeightbors + 1

        return totalNeightbors

    def reset(self):
        for x in range(0, self.w):
            for y in range(0, self.h):
                self.array[x][y] = 0

class pylife:

    def __init__(self, parent):
        self.cellCanvas = CellCanvas()
        self.cellCanvas.grid(row=0, column=0, columnspan=4)

        self.run = Button(parent)
        self.run["text"] = "Run"
        self.run["command"] = self.doRun
        self.run.grid(row=1, column=0)

        self.step = Button(parent)
        self.step["text"] = "Step"
        self.step["command"] = self.takeStep
        self.step.grid(row=1, column=1)

        self.clear = Button(parent)
        self.clear["text"] = "Clear"
        self.clear["command"] = self.clearCells
        self.clear.grid(row=1, column=2)

        self.exit = Button(parent)
        self.exit["text"] = "Exit"
        self.exit["command"] = self.exitApp
        self.exit.grid(row=1, column=3)

        global wrapparound
        wrapparound = IntVar()
        c = Checkbutton(parent, text="Wrap Around", variable=wrapparound)
        c.grid(row=2, column=1, columnspan=2)

    def doRun(self):
        origArray = [[0 for x in range(self.cellCanvas.array.w)] for y in range(self.cellCanvas.array.h)]

        while True:
            for x in range(0, self.cellCanvas.array.w):
                for y in range(0, self.cellCanvas.array.h):
                    if self.cellCanvas.array.array[x][y] == 1:
                        origArray[x][y] = 1
                    else:
                        origArray[x][y] = 0

            root.after(10, self.takeStep())
            self.cellCanvas.updateView()

            if origArray == self.cellCanvas.array.array:
                break



    def doRunStep(self):



        self.takeStep()
        self.cellCanvas.updateView()



        return True


    def takeStep(self):
        self.cellCanvas.step()

    def clearCells(self):
        self.cellCanvas.array.reset()
        self.cellCanvas.updateView()

    def exitApp(self):
        root.quit()

class CellCanvas(Canvas):
    def __init__(self):
        self.canvas = None

        Canvas.__init__(self, width=200, height=200)
        self.bind("<Button-1>", self.change)

        for i in range(0, 20):
            i = i * 10

            for j in range(0, 20):
                j = j * 10
                self.create_rectangle(j, i, j + 10, i + 10, fill="white")


        self.grid(row = 0, column = 0)
        self.array = CellArray()

    def change(self, event):
        self.canvas = event.widget
        x = self.canvas.canvasx(event.x)
        x = int((x + 10) / 10) - 1
        y = self.canvas.canvasy(event.y)
        y = int((y +10 ) / 10) - 1

        if self.array.array[x][y] == 0:
            self.array.array[x][y] = 1
        else:
            self.array.array[x][y] = 0

        self.updateView()

    def step(self):
        self.array.step()
        self.updateView()

    def updateView(self):
        if self.canvas is None:
            return

        for x in range(0, self.array.w):
            for y in range(0, self.array.h):

                current = self.canvas.find_closest(x * 10, y * 10)[0]

                if self.array.array[x][y] == 1:
                    self.itemconfig(current, fill="black")
                    self.update_idletasks()
                else:
                    self.itemconfig(current, fill="white")
                    self.update_idletasks()


root = Tk()
root.title("Pylife")
pylife = pylife(root)
root.grid()
root.mainloop()