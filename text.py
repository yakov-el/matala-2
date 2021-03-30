def revword(word):
    newword=word.lower()
    return(newword[::-1])


def countword():
    fname = input('Enter the file name: ')
    handle=open(fname)
    word = handle.readline()
    word = word.rstrip()
    counter=1
    for line in handle:
        line = line.split()
        for i in line:
            if revword(i) == word:
                    counter = counter+1 
    return(counter)