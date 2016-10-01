import sys
import concordance

for i in range(1, len(sys.argv)):
    f = open(sys.argv[i], 'r')

    wordCount = concordance.concordance(f, False)


    for k, v in sorted(wordCount.items()):
        print("{0} ({1}):".format(k, len(v)))
        print("\t {0}: ".format(sys.argv[i]), end=" ")

        fDict = {}

        for item in v:
            frequency = fDict.get(item, 0)
            fDict[item] = frequency + 1

        for k2, v2 in fDict.items():
            if v2 > 1:
                print("{0} ({1}),".format(k2, v2), end=" ")
            else:
                print("{0},".format(k2), end= " ")

        print()

    f.close()