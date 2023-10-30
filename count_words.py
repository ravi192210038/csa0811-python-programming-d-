
file_name = input("Enter file name:")

file1 = open(file_name, "r")

word_count = 0
i = 0
str1 = ""
print("Contents of file " + file_name + " are:")

# display and count number of  words in each line of text file
for line in file1:
    i+=1
    print(line, end='')
    words_in_line = len(line.split())
    str1 = str1 + "Words in Line No: " + str(i) + " are : " + str(words_in_line)+"\n"
    word_count+=words_in_line
    
print('\n\n ' + str1)    
print('\n\nTotal Number of  words in this file are = ' + str(word_count))

file1.close()
