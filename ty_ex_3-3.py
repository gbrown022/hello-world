def rightJustify(aString):
    padding = ''
    screenWidth = 70
    stringLength = len(aString)
    columnStart = screenWidth - stringLength
    for x in range(0, columnStart):
        padding += ' '
    print padding + aString

    # Make sure we're printing to the correct column
    print '0123456789012345678901234567890123456789012345678901234567890123456789'

rightJustify('Geoffrey')
