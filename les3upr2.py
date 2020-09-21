def write_array(array, file):

    for i in range(len(array)):
        file.write(array[i] + '\n')
    file.close()
    pass

file = open("C:\\Users\\Анна\\PycharmProjects\\proga\\file2.txt", "w", encoding="utf8")
text = ['я помню чудное мгновенье', 'передо мной явилась ты', 'как мимолетное виденье', 'как гений чистой красоты']
write_array(text, file)