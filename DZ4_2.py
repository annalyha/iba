# Скопировать в файл F2 только четные строки из F1. Подсчитать размер файлов F1 и F2 (в байтах)
import os

list1 = []
list2 = []

with open(r'E:\F1.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        list1.append(line)

    i = 0
    for i in range(len(list1)):
        if (i+1) % 2 != 0:
            list1[i] = ''

    i = 0
    while i < len(list1):
        if list1[i] == '':
            list2.append(list1[i+1])
            del list1[i]
        else:
            i += 1

    with open(r'E:\F2.txt', 'w', encoding='utf-8') as ff:
        ff.write('\n'.join(list2))


print('Размер F1 '+ str(os.path.getsize("E:\\F1.txt"))+' байт')
print('Размер F2 '+ str(os.path.getsize("E:\\F2.txt"))+' байт')
