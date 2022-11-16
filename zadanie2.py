text_file = open('content.txt', 'r')

user_letter = input('Enter letter')
contents = text_file.read()

for word in contents.split():
    if word[0].find(user_letter) >= 0:
        print(word)
