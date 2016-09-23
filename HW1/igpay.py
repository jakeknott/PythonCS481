def igpay(stringToConvert):
    if len(stringToConvert) is 0:
        return stringToConvert

    # make a copy of the string, incase we just return it.
    savedString = stringToConvert

    # This will set isUpper to true, only if, the first letter is upper but not the whole string,
    # if the whole string is upper, then we leave it alone.
    if stringToConvert[0].isupper():
        isFirstUpper = True
    else:
        isFirstUpper = False

    # this will determine if the whole string is upper case.
    if stringToConvert.isupper():
        isAllUpper = True
    else:
        isAllUpper = False

    stringToConvert = stringToConvert.lower()

    foundVowelIndex = 0
    vowels = "aeiouAEIOU"

    if stringToConvert[0] in vowels:
        #Since it begings with a vowel, just append 'way'
        convertedString = stringToConvert + "way"

        if isFirstUpper:
            # If we started with an uppercase, we need to perserve that.
            convertedString = convertedString[0].upper() + convertedString[1:]

            # If the whole thing was upper, we must return the new string as all upper
            if isAllUpper:
                return convertedString.upper();

            # Otherwise return just the first upper case
            return convertedString
        else:
            return convertedString;


    #If it does not start with a vowel, go find the first one.
    for c in stringToConvert:
        if c in vowels:
            #found our vowel
            # that the string and make the first part from the vowel on, then the start to the vowel, then appen 'ay'
            convertedString = stringToConvert[foundVowelIndex:] + stringToConvert[0 : foundVowelIndex] + "ay"
            if isFirstUpper:
                #If we started with an uppercase, we need to perserve that.
                convertedString = convertedString[0].upper() + convertedString[1:]

                # If the whole thing was upper, we must return the new string as all upper
                if isAllUpper:
                    return convertedString.upper();

                # Otherwise return just the first upper case
                return convertedString
            else:
                return convertedString;

        foundVowelIndex = foundVowelIndex + 1

    return savedString;

if __name__ == '__main__':
    if "Arrotpay" != igpay("Parrot"):
        raise Exception("igpay('Parrot') did not give expected result")
    else:
        print(igpay("Parrot"))

    if "arrotpay" != igpay("parrot"):
        raise Exception("igpay('parrot') did not give expected result")
    else:
        print(igpay("parrot"))

    if "ARROTPAY" != igpay("PARROT"):
        raise Exception("igpay('PARROT') did not give expected result")
    else:
        print(igpay("PARROT"))

    if "addway" != igpay("add"):
        raise Exception("igpay('add') did not give expected result")
    else:
        print(igpay("add"))

    if "Addway" != igpay("Add"):
        raise Exception("igpay('Add') did not give expected result")
    else:
        print(igpay("Add"))

    if "ADDWAY" != igpay("ADD"):
        raise Exception("igpay('ADD') did not give expected result")
    else:
        print(igpay("ADD"))

    if "officeway" != igpay("office"):
        raise Exception("igpay('office') did not give expected result")
    else:
        print(igpay("office"))

    if "why" != igpay("why"):
        raise Exception("igpay('why') did not give expected result")
    else:
        print(igpay("why"))

    if "ightsknay" != igpay("knights"):
        raise Exception("igpay('knights') did not give expected result")
    else:
        print(igpay("knights"))

    if "Ightsknay" != igpay("Knights"):
        raise Exception("igpay('Knights') did not give expected result")
    else:
        print(igpay("Knights"))

    if "IGHTSKNAY" != igpay("KNIGHTS"):
        raise Exception("igpay('KNIGHTS') did not give expected result")
    else:
        print(igpay("KNIGHTS"))
