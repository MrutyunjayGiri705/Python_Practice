file=open("M.txt","r")
# content=file.read()
# print(content)
# read_line=file.readline(10)
# print(read_line)
read_line=file.readlines()
print(read_line)

file.close()