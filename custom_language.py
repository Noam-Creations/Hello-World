def jeffDawg(word):
    newWord = ""
    vowels = ["a", "e", "i", "o", "u"]

    fL = word[0]
    if fL == vowels:
        newWord += "jess"

        
    for c in word:
        #every time there is an s it puts %74517485%$%@9854
        if c == "s":
            newWord += "%74517485%$%@9854"
        #every time there is an e it puts 3847
        elif c == "e":
            newWord += "3847"
        #every time there is an g it puts %89hello
        elif c == "g":
            newWord += "%89hello"
        else:
            newWord += c

    newWord += "dawg"
    return newWord