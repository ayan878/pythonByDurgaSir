
file=open("File Handling/Example_01.txt",'w')
print("File Name: ",file.name) # Name of the opened file
print("File Mode: ",file.mode) #mode of the opened file
print("Is File Readable: ",file.readable()) #return boolean whether file readdable or not 
print("Is File Writable: ",file.writable()) #return boolean wheather file writable  or or
print("Is File Closed : ",file.closed) #return boolean file open or not
file.close()
print("Is File Closed : ",file.closed)

#writing data to the text files

file= open("Example_01.txt",'w')
file.write("It is Example_01.text file.")
print("Data written to the file succesfully")
file.close()

# Open a file in read mode
file = open("Example_01.txt", 'r')
data= file.read() #read total data from the file
print(data)

#open a file in write mode
file = open("Example_01.txt",'w')
list=["Ayan","Belal","Ehsan","Shazeb"]
file.writelines(list)
print("List of line written to the file succesfully")
file.close()

#To read only first 10 characters:
file=open("Example_01.txt",'r')
data=file.read(10)
print(data)
file.close()

#To read data only one line
file=open("Example_01.txt",'r')
data=file.readline()
print(data)
file.close()

#To read data line by line
file=open("Example_01.txt",'r')
data=file.readlines()
print(data)
file.close()