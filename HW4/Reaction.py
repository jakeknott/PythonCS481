class Particle:
    def __init__(self, sym, chg, massNumber):
        self.sym = sym
        self.chg = chg
        self.massNumber = massNumber

    def __add__(self, other):
        return self, other

    def __str__(self):
        return self.sym

    def __repr__(self):
        className = self.__class__.__name__
        return "{}({!r}, {!r}, {!r})".format(
            className, self.sym, self.chg, self.massNumber)


class Nucleus(Particle):
    def __str__(self):
        return "({}){}".format(self.massNumber, self.sym)


class UnbalancedCharge(Exception):
    def __init__(self, diff):
        Exception.__init__(self, "Unbalanced Charge, the charge of the left side must equal the charge on the right", diff)


class UnbalancedNumber(Exception):
    def __init__(self, diff):
        Exception.__init__(self, "Unbalanced Mass Number, the mass of the left side must equal the mass on the right", diff)


class Reaction:
    def __init__(self, left, right):
        self.tup1 = left
        self.tup2 = right
        self.equation = "{} + {} -> {} + {}".format(self.tup1[0], self.tup1[1], self.tup2[0], self.tup2[1])
        self.__checkEquation()

    def __checkEquation(self):
        leftSideChg = self.tup1[0].chg + self.tup1[1].chg
        rightSideChg = self.tup2[0].chg + self.tup2[1].chg

        if leftSideChg is not rightSideChg:
            raise UnbalancedCharge(leftSideChg - rightSideChg)

        leftSideMass = self.tup1[0].massNumber + self.tup1[1].massNumber
        rightSideMass = self.tup2[0].massNumber + self.tup2[1].massNumber

        if leftSideMass is not rightSideMass:
            raise UnbalancedNumber(leftSideMass - rightSideMass)

    def __repr__(self):
        return self.equation


class ChainReaction:
    reactions = []

    def __init__(self, name):
        self.name = name

    def addReaction(self, reaction):
        self.reactions.append(reaction)

    def __getNet(self):
        lhs = []
        rhs = []
        for react in self.reactions:
            lhs.append(react.tup1[0])
            lhs.append(react.tup1[1])

            rhs.append(react.tup2[0])
            rhs.append(react.tup2[1])

        lhsToRemove = []

        for l in lhs:
            for r in rhs:
                if l is r:
                    lhsToRemove.append(l)
                    rhs.remove(r)
                    # Move on to the next element
                    break

        for l in lhsToRemove:
            lhs.remove(l)

        net = lhs[0]

        for i in range(1, len(lhs)):
            net = "{} + {}".format(net, lhs[i])

        net = "{} -> {}".format(net, rhs[0])

        for i in range(1, len(rhs)):
            net = "{} + {}".format(net, rhs[i])

        return net

    def __repr__(self):
        toReturn = "{}:".format(self.name)
        for react in self.reactions:
            toReturn = "{}\n{}".format(toReturn, react)

        toReturn = "{}\nNet:\n{}".format(toReturn, self.__getNet())

        return toReturn


# Self testing/globals
d = Nucleus("H", 1, 2)  # hydrogen
li6 = Nucleus("Li", 3, 6)  # lithium
he4 = Nucleus("He", 2, 4)  # helium
em = Particle("e-", -1, 0)  # an electron
ep = Particle("e+", 1, 0)  # a positron
p = Particle("p", 1, 1)  # a proton
n = Particle("n", 0, 1)  # a neutron
nu_e = Particle("nu_e", 0, 0)  # a neutrino
gamma = Particle("gamma", 0, 0)  # a gamma particle


if __name__ == "__main__":
    print(Reaction(li6 + d, he4 + he4))
    print(Reaction((li6, d), (he4, he4)))
    print(Reaction((ep, ep), (ep, ep)))

    try:
        Reaction((li6, li6), (he4, he4))
        # If this does not throw an exception then the test failed.
        raise Exception("Reaction((li6, li6), (he4, he4)) did not raise exception as expected")
    except UnbalancedCharge:
        # Can ignore, this is expected
        print("caught UnbalancedCharge error")

    try:
        Reaction((ep, ep), (p, p))
        # If this does not throw an exception then the test failed.
        raise Exception("Reaction((ep, ep), (p, p)) did not raise exception as expected")
    except UnbalancedNumber:
        # Can ignore, this is expected
        print("caught UnbalancedNumber error")

    he3 = Nucleus(" He ", 2, 3)  # not defined above
    chnPP = ChainReaction(" proton - proton ( branch I ) ")
    for rctn in (Reaction((li6, d), (he4, he4)),
                 Reaction((ep, ep), (ep, ep)),
                 Reaction((d, p), (he3, gamma)),
                 Reaction((d, p), (he3, gamma)),
                 Reaction((li6, d), (he4, he4))):
        chnPP.addReaction(rctn)

    print(chnPP)

