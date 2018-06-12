import os

##########   WRITING FILE OUT   ##########
#open file to write
f = open('read_write.txt', 'w+')
#FOR: number in range from 1 to 10, write the number and a new line to our file
for number in range(1, 10):
    #write number to file (with a new line)
    f.write("{0}\n".format(number))
#create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']
#FOR: letter in letters from a to e, write letter and a new line to our file
for letter in letters:
    #write letter to file (with a new line)
    f.write("{0}\n".format(letter))
#seek file
f.seek(0)

file_contents = f.read()

g = open('output.txt', 'w+')
#for line in f:
g.write(file_contents)

f.close()
g.close()
