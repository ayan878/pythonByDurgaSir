
file=open("File Handling/Example_01.txt",'w')
print("File Name: ",file.name)
print("File Mode: ",file.mode)
print("Is File Readable: ",file.readable())
print("Is File Writable: ",file.writable())
print("Is File Closed : ",file.closed)
file.close()
print("Is File Closed : ",file.closed)
