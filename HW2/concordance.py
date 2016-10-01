def concordance(f, unique=True):
    wordDic = {}
    lineNum = 1

    for line in f:

        for word in line.split(' '):
            word = word.lower()

            # Remove any non alpha chars from the end of the word.
            while len(word) is not 0 and not word[-1].isalpha():
                word = word[:-1]

            if word is not '':
                if not unique:
                    # If not unique just add the line number to the list (even duplicates is fine)
                    if len(wordDic.get(word, [])) is 0:
                        wordDic[word] = []

                    wordDic[word].append(lineNum)
                else:
                    # Otherwise see if we have a list for that word, if the last entry is the line number, then do not add
                    # it again, only add if we have the word and do not have the current line number in its list.
                    if len(wordDic.get(word, [])) is 0:
                        # If we get an empty list append the line number
                        wordDic[word] = []
                        wordDic[word].append(lineNum)
                    elif wordDic[word][-1] is not lineNum:
                        # Otherwise, if we got a list, check the last entry, if it is not the line nubmer then add the
                        # line to the list
                        if len(wordDic.get(word, [])) is 0:
                            wordDic[word] = []
                        wordDic[word].append(lineNum)

        # Update line number
        lineNum += 1

    return wordDic


if __name__ is "__main__":
    f = open('test.txt', 'r')

    first = concordance(f)

    #checking
    if first["testing"] != [1]:
        raise Exception("Dictionary does not match expected.")
    if first["the"] != [1, 2]:
        raise Exception("Dictionary does not match expected.")
    if first["line"] != [1, 2]:
        raise Exception("Dictionary does not match expected.")
    if first["number"] != [1, 2]:
        raise Exception("Dictionary does not match expected.")
    if first["adding"] != [2]:
        raise Exception("Dictionary does not match expected.")
    if first["same"] != [2]:
        raise Exception("Dictionary does not match expected.")
    if first["to"] != [2]:
        raise Exception("Dictionary does not match expected.")

    f.close()
    f = open('test.txt', 'r')

    second = concordance(f, False)
    # checking
    if second["testing"] != [1]:
        raise Exception("Dictionary does not match expected.")
    if second["the"] != [1, 2, 2]:
        raise Exception("Dictionary does not match expected.")
    if second["line"] != [1, 2]:
        raise Exception("Dictionary does not match expected.")
    if second["number"] != [1, 2]:
        raise Exception("Dictionary does not match expected.")
    if second["adding"] != [2]:
        raise Exception("Dictionary does not match expected.")
    if second["same"] != [2, 2]:
        raise Exception("Dictionary does not match expected.")
    if second["to"] != [2]:
        raise Exception("Dictionary does not match expected.")
