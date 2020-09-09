# Created By - Anubha Barve (barveanubha2510@gmail.com)
# Created on - September 09,2020
from collections import Counter 


# function to find non-repeating character
def uniqueCharacter(s):

    string = s.lower()

    ch_count = Counter(string)

    input_string = ""

    for idx,ch in enumerate(s):

        ch = ch.lower()

        if ch_count[ch] == 1:
            print("First non-repeated Character is - ",ch)
            break

    ch_scount = sorted(ch_count.items(), key=lambda x:x[1])

    ch_count1 = Counter(s)

    ch_scount1 = sorted(ch_count1.items(), key=lambda x:x[1])

    #print(ch_scount)

    for c in ch_scount:

        if c[0] in s and c[1] == 1:
            input_string += c[0]
        elif c[0].upper() in s and c[1] == 1:
            input_string += c[0].upper()

    for c in ch_scount1:

        if c[0] not in input_string:
            input_string += c[0] * c[1]

    print("Rewritten String - ",input_string)


def main():

    st = input("Enter the string: ")

    uniqueCharacter(st)

if __name__ == "__main__":
    main()