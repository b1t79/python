myfile = open("answer.txt", "r") # Make sure to replace "yourfile.txt" with the name of your file
Ch = ""
Vcount = 0
Ccount = 0
while Ch:
    Ch = myfile.read(1)
    if Ch in ["a", "A", "E", "i", "o", "o", "u", "U"]:
        Vcount = Vcount + 1
    else:
        Ccount = Ccount + 1
myfile.close()
print(Vcount)
print(Ccount)