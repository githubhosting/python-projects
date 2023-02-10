# create a file and open it and write hello world

# f = open("test.txt", "w")
# f.write("Hello World")
# f.write("This is our new text file")
# f.write("and this is another line.")
# f.close()

# create a text file and write 10 lines of text into it

f = open("test.txt", "w")
for i in range(80):
    f.write("This is line %d\r" % (i + 1))
f.close()

# read the file and print

f = open("test.txt", "r")
if f.mode == 'r':
    contents = f.read()
    print(contents)
f.close()

# f = open("test.txt", "r")
# lines = [line.rstrip('\n') for line in f]
# f.close()
# print(lines)
#
# for line in lines:
#      if line.startswith("This"):
#          print(line)






