from custom_module import *
file = open("user.csv","r")
file_string = file.read()+";EOP"

file_string = manual_split(file_string,"\n")
print(file_string)
print(manual_len(file_string))