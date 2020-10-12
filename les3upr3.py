import os
import zipfile

file = open("C:\\Users\\Анна\\PycharmProjects\\proga\\otvet.txt", "w")
#myzip = zipfile.ZipFile('C:\\Users\\Анна\\PycharmProjects\\proga\\main.zip')
# for file in myzip.namelist():
#     myzip.extractall('C:\\Users\\Анна\\PycharmProjects\\proga')
ans  =  []
for current_dir, dirs, files in os.walk('C:\\Users\\Анна\\PycharmProjects\\proga\\main'):
    for i in files:
        #if current_dir not in ans:
        if i[-2:] == 'py':
            ans.append(current_dir)
            break
    #print(current_dir, dirs, files)

ans.sort()
for i in range(len(ans)):
    file.write(ans[i])
    file.write('\n')
file.close()
#print(ans)
#myzip.close()
