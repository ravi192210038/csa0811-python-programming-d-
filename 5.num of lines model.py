text="This is most straightforward way to count number of lines in text file in python .\nthe readlines()method read alllines from a file and store in a list.\nNext use the len()functionto find length of list which is nothing but total lines present in file"
lines=text.split("\n")
num_lines=len(lines)
words=text.split()
num_words=len(words)
print("number of lines",num_lines)
print("number of words in each line",num_words)

