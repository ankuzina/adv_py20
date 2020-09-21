file = open("C:\\Users\\Анна\\PycharmProjects\\proga\\file1.txt", "rt")
text = file.readlines()
text1 = []
for i in range(len(text)):
    text1.append(text[i].strip())
file.close()
for i in range(len(text1)):
    print(text1[i])