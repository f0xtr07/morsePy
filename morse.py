def morseEnc(encMorse):
    morseCharsAZ = {'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----'}      #create a dictionary of morse (key,value) pair. This would be helpful when we directly want to reference the value for each key
    
    parseMorse = encMorse.upper() #store the passed string into a different string variable and convert all characters into upper case for smoother conversion

    #next step is to parse the string to identify which characters entered in the user input match the AZ dictionary
    #once the character is identified, write the corresponding value of the dictionary to a string variable
    #string variable index manipulation is required at this step

    finalString = ''


    #Below commented out nested for loop code is a working solution but an unexpected sorting of the string character occurs
    #for key,value in morseCharsAZ.items():
    #    for x in range(len(parseMorse)):
    #        if(parseMorse[x]==key):
    #            finalString = finalString + ' ' + value

    for x in range(len(parseMorse)):
        for key, values in morseCharsAZ.items():
            if(parseMorse[x]==key):
                finalString = finalString + ' ' + values

    print(finalString)


def morseDec(decrypt):
    morseCharsAZ = {'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----'}

    decryptedString = ''
    parseMorse = decrypt
    splitString = parseMorse.split(" ")
    #print(splitString)

    for x in splitString:
        for key,values in morseCharsAZ.items():
            if(x==values):
                decryptedString = decryptedString + '' + key

    print(decryptedString)
                
