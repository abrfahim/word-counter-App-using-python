
with open('words.txt' ,'r') as file:
    data = file.read().lower()
    file.close()
words = data.split()

# user can input words, case insensitive
search_words= input("give your words here:").lower().split()

matches = [i for i in words if i in search_words ]
for i in search_words:
    if i in matches:
        print(i, ">", matches.count(i), 'times')
    else:
        print(i, ">", matches.count(i),'times')
