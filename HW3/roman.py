from collections import OrderedDict

# ordered so we can tranverse down it to take out the bigger numbers first
# I added some combos to make it easier when changing into roman.
romanDict = OrderedDict()
romanDict[1000000] = "(M)"
romanDict[900000] = "(C)(M)"
romanDict[500000] = "(D)"
romanDict[400000] = "(C)(D)"
romanDict[100000] = "(C)"
romanDict[90000] = "(X)(C)"
romanDict[50000] = "(L)"
romanDict[40000] = "(X)(L)"
romanDict[10000] = "(X)"
romanDict[9000] = "(I)(X)"
romanDict[5000] = "(V)"
romanDict[4000] = "(I)(V)"
romanDict[1000] = "M"
romanDict[900] = "CM"
romanDict[500] = "D"
romanDict[400] = "CD"
romanDict[100] = "C"
romanDict[90] = "XC"
romanDict[50] = "L"
romanDict[40] = "XL"
romanDict[10] = "X"
romanDict[9] = "IX"
romanDict[5] = "V"
romanDict[4] = "IV"
romanDict[1] = "I"
romanDict[0] = "N"

class Roman:


    def __init__(self, number):
        if number >= 2000000:
            raise ValueError
        self.romNum = number

    def __add__(self, other):
        try:
            return Roman(self.romNum + other.romNum)
        except:
            return Roman(self.romNum + other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Roman(self.romNum - other.romNum)

    def __floordiv__(self, other):
        return Roman(self.romNum // other.romNum)

    def __truediv__(self, other):
        return Roman(self.romNum // other.romNum), Roman(self.romNum % other.romNum)

    def __mul__(self, other):
        return Roman(self.romNum * other.romNum)

    def __pow__(self, power, modulo=None):
        return  Roman(self.romNum**power)

    def __eq__(self, other):
        return self.romNum == other.romNum

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.romNum < other.romNum

    def __le__(self, other):
        return self.romNum <= other.romNum

    def __gt__(self, other):
        return self.romNum > other.romNum

    def __ge__(self, other):
        return self.romNum >= other.romNum

    def __neg__(self):
        return Roman(-self.romNum)

    def intToRoman(inum):
        if inum <= 0:
            return ""

        romanString = ""
        for r in romanDict.keys():
            x, y = divmod(inum, r)

            # if we can divide by r, add that roman num to our string
            if x > 0:
                romanString += romanDict[r]
                # decremend our number by the amount we have added to our roman string
                inum -= r
                return romanString + Roman.intToRoman(inum)
        return ""

    def __str__(self):
        return Roman.intToRoman(self.romNum)



for num in range(0, 1001):
    globals().setdefault(Roman.intToRoman(num), Roman(num))
