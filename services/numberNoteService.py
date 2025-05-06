from patterns.numberNoteRegex import NumberNoteRegex

def extractNumberNote(linCurrent, linNext):
    return{
        'footer': NumberNoteRegex(linCurrent).matchDescribeNoteFotterInline,
        'nextLine': NumberNoteRegex(linNext).matchNumberNote if NumberNoteRegex(linCurrent).matchDescribeNote else None,
        'inline': NumberNoteRegex(linCurrent).matchNumberNoteInline,
    }
    # nNota = None

    # if not nNota:
    #     nNota = NumberNoteRegex(linCurrent).matchNumberNoteInline
    #     if nNota:
    #         print(f'if matchNumberNoteInline: {nNota}')
    #     #     return nNota

    # if not nNota and NumberNoteRegex(linCurrent).matchDescribeNote:
    #     nNota = NumberNoteRegex(linNext).matchNumberNote
    #     if nNota:
    #         print(f'if matchNumberNote: {nNota}')
    #     #     return nNota

    # if NumberNoteRegex(linCurrent).matchDescribeNoteFotterInline:
    #    nNota = NumberNoteRegex(linCurrent).matchDescribeNoteFotterInline
    #    if nNota:
    #         print(f'if matchDescribeNoteFotterInline: {nNota}')
    # #         return nNota

    # return nNota        
