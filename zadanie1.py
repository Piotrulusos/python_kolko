text_file = open("content.txt", "r")

for Pythons in text_file:
    if Pythons.find('Python') >= 0:
        print(Pythons, end='')

text_file.close()
