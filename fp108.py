myfile=open("Answer.txt","r")
line=" "   #initially stored a spce (a non-None value)
while line :
    line = myfile.readline() #one line read from file
    #printing the line by word using split()
for word in line.split()
         print(word,end= '#')
    print()
    #close the file
    myfile.close
