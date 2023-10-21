import sys
from textwrap import wrap

# encrypt = sys.argv[1]
# num = sys.argv[2]
# ori = sys.argv[3]

def caesar_cipher(string, shift):
    
    # Inisialiasi kalimat / teks original untuk dicocokkan
    ori = "KAhil aKbAR bAyU aDiTYO"
    temp = ""
    tempComb = ""
    caesarEncode = ""
    
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    kombUp = [] # [AA, AB, AC, ..., MA, MB, MC, ..., ..., ZZ]

    kombLo = [] # [aa, ab, ac, ..., ma, mb, mc, ..., ..., zz]

    kombUpLo = [] # [Aa, Ab, Ac, ..., Ma, Mb, Mc, ..., ..., Zz]

    kombLoUp = [] # [aA, aB, aC, ..., mA, mB, mC, ..., ..., zZ]

    for char1 in upper:
        for char2 in upper:
            kombUp.append(char1 + char2)

    for char3 in lower:
        for char4 in lower:
            kombLo.append(char3 + char4)

    for char5 in upper:
        for char6 in lower:
            kombUpLo.append(char5 + char6)
            kombLoUp.append(char6 + char5)

    delSpace = string.replace(" ", "")
    # print("delSpace : ", delSpace)

    addWrap = wrap(delSpace, 2)
    # print("addWrap : ", addWrap)

    for char in addWrap:
        if char in kombUp:
            index = kombUp.index(char)
            cipher = (index - shift) % 676
            tempComb += kombUp[cipher]
            # print("tempComb : ", tempComb)
        
        elif char in kombLo:
            index = kombLo.index(char)
            cipher = (index - shift) % 676
            tempComb += kombLo[cipher]
            # print("tempComb : ", tempComb)
        
        elif char in kombUpLo:
            index = kombUpLo.index(char)
            cipher = (index - shift) % 676
            tempComb += kombUpLo[cipher]
            # print("tempCombUp : ", tempComb)

        elif char in kombLoUp:
            index = kombLoUp.index(char)
            cipher = (index - shift) % 676
            tempComb += kombLoUp[cipher]
            # print("tempCombLo : ", tempComb)

        else:
            tempComb += char
    # print("tempComb : ", tempComb)

    for abjad in tempComb:
        if abjad in upper:
            index = upper.index(abjad)
            cipher = (index - shift) % 26
            temp += upper[cipher]
            # print("tempUp : ",temp)

        elif abjad in lower:
            index = lower.index(abjad)
            cipher = (index - shift) % 26
            temp += lower[cipher]
            # print("tempLo : ",temp)

        else:
            temp += abjad
    # print("temp : ", temp)

    findSpace = 0
    for char in temp:
        if findSpace < len(ori) and ori[findSpace].isspace():
            caesarEncode += " "
            findSpace += 1
            # print("findspace : ", caesarEncode)

        caesarEncode += char
        findSpace += 1

        # print("findspace : ", caesarEncode)

    return caesarEncode

# Manual
string = input("String : ")
shift = int(input("Shift : "))

# uncomment kode string & shift dibawah jika ingin melakukan decrypt otomatis
# string = encrypt
# shift = int(num)
#

shift %= 26

result = caesar_cipher(string, shift)
print("\nDecrypt : ", result)
