filepath = 'F:\Python notepad\An Example Notepad.txt'

word_count = 0

with open(filepath, 'r') as file:
    for line in file:
        # The below code removes any unesscessary spaces
        line = line.strip()
        if line: # The reason we add if line is because to automatically
            # check for blank lines, if we didnt use it there would be extra
            # words
            word_count += len(line.split())
    contents = file.read()

print(word_count)

