    # 1
with open("file1.txt") as f1, open("file2.txt") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    for i in range(min(len(lines1), len(lines2))):
        if lines1[i] != lines2[i]:
            print(f"Файл 1: {lines1[i]} \nФайл 2: {lines2[i]}")

   # 2
vowels = set("aeiouAEIOU")  # почему-то при вводе русских гласных букв подсчет некорректный
chars = 0
lines = 0
vowel_count = 0
consonant_count = 0
digit_count = 0

with open("file3.txt", "r") as f:
    for line in f:
        lines += 1
        chars += len(line)
        for char in line:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
            elif char.isdigit():
                digit_count += 1
with open("output.txt", "w") as f:
    f.write(f"Количество символов: {chars}\n")
    f.write(f"Количество строк: {lines}\n")
    f.write(f"Количество гласных: {vowel_count}\n")
    f.write(f"Количество согласных: {consonant_count}\n")
    f.write(f"Количество цифр: {digit_count}")

    # 3
with open("file4.txt", "r") as f:
    lines = f.readlines()
with open("output2.txt", "w") as f:
    f.writelines(lines[:-1])

   # 4
with open("file5.txt", "r") as f:
    lines = f.readlines()
long_len = 0
for line in lines:
    if len(line) > long_len:
        long_len = len(line)
print(f"Длина самой длинной строки равна: {long_len}")

    # 5
word = input("Введите слово: ")
count = 0

with open("file6.txt", "r") as f:
    for line in f:
        words = line.split()
        count += words.count(word)

print(f"Слово '{word}' встречается в файле {count} раз(а).")

    # 6
search_word = input("Введите слово для замены: ")
replace_word = input("Введите слово, на которое нужно заменить: ")

with open("file7.txt", "r") as f:
    data = f.read()

data = data.replace(search_word, replace_word)

with open("output3.txt", "w") as f:
    f.write(data)