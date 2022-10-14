
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Например, строчку aaababbcbbb он переводит в (a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3).


def coding(text: str):
    archive = [('just for volume',100500)]
    pre_letter = text[0]
    i = 0
    count = 1
    for letter in text:
        if letter == pre_letter:
            archive[i] = (letter, count+1)
            count += 1
        else:
            pre_letter = letter
            count = 1
            i += 1
            archive.append((letter, count))
    return archive


text = 'aaababbcbbbccccddddddeffffffffffffffffff'
print(text)
archive = coding(text)
print(archive)
decode = ''.join(list(i * j for (i,j) in archive))
print(decode)
