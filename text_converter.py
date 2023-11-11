#converts the text put in a sample text file into whatsapp format
file = open("wsap_format.txt", "r+")

s = file.readlines()

for i in range(len(s)):
    j = i+1
    if s[i:j] == '\n':
        pass

newlis = []
for x in s:
    newlis.append(x.strip('\n'))
