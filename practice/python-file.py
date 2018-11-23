from sys import argv

script, filename = argv

#if u want to write mode, change 'a' to 'w'
txt = open(filename, 'a')

print("Filename is: %s" %script)
# print(txt.read())


txt.write("I have added this line to the file.\n")

txt = open(filename)
print(txt.read())

# if u want to just truncate the file
# txt = open(filename, 'w')
# txt.truncate()
txt.close()
