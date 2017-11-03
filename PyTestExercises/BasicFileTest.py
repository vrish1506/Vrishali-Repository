#File Test

file = open("testfile.txt", "w")
file.write("Hello World \n")
file.write("This is first line \n")
file.write("This is second line \n")

file.close()

file1 = open("testfile.txt", "r")
print("File Read: Contents of file")
print(file1.read())
file1.close()


file2 = open("testfile.txt", "r")
print(file2.read(5))
file2.close()

file3 = open("testfile.txt", "r")
print(file3.readline())
file3.close() 



