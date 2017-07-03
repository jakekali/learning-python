# # This is a comment
# this code gets the list of all the presidents from a txt file, and then puts them in an array
# it then displays some information, and requests that the user add there name to list of presidents

file = open("presidents.txt", "r")

presidents = []
for line in file:
    line = line.strip()
    presidents.append(line)
file.close()
print("There were " + str(len(presidents)) + " of the USA. \n and they are: ")
print(presidents)

print("Add yourself to the list of presidents of the united states")
name = input("What is your name?")

file = open("presidents.txt", "a")

file.write(name + '\n')

file.close()