#2.write a python program that:
#accepts a sentence from the user.input()
#counts the no of the words in it
# capitalizes the first letter of each word
# reverses the whole sentence 
sentence=input("enter a sentence: ")
print(sentence)
sentence_splitted=sentence.split(" ")
print(sentence_splitted)
print(len(sentence_splitted))
sentence_title=sentence.title()
print(sentence_title)
sentence_reverse=sentence[::-1]
print(sentence_reverse)
#3.convert the text to "good habits are hard to break!  "
#text ="  BAD habits are hard to break!  "
text ="  BAD habits are hard to break!  "
text=text.strip()
text=text.replace("BAD","good")
print(text)
#4. clean email and extract domain 
#email="  john.Doe@gmail.com"
email="  john.Doe@gmail.com"
email=email.strip()
email=email.lower()
print(email[9:18])
email=email.split("@")
domain=email[1]
print(domain)
#5.clean names and creat a formatted sentence "my name is John Doe and I love Reading Books"
#first="john"
#last="Doe"
#hobby="Reading books"
first="john"
first=first.title()
last="doe"
last=last.title()
hobby="  Reading books  "
hobby=hobby.strip()
sentence=f"my name is {first} {last} and I love {hobby}"
print(sentence)
