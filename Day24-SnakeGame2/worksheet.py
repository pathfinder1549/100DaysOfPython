

file = open("textFile.txt")
contents = file.read()
file.close()

with open("textFile.txt") as file:
    contents = file.read()

with open("textFile.txt", mode="a") as file:
    # "a" for append mode
    file.write("\nsome text")