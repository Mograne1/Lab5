#Нешерет Максим 
#ІКСМ-1
with open("text.txt", "r", encoding='utf-8') as file:
    read_content = file.read()

file_content = read_content.split()

word_count = {}
for word in file_content:
    word = word.strip('.,!?()[]{}"\'').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

while True:
    print('\n Меню.')
    print('1. Навести кількість появ кожного слова у тексті.')
    print('2. Навести кількість появ певного слова у тексті.')
    print('3. Завершити програму.')
    choose = input(' Ваш вибір: ')

    if choose == '1':
        for word, count in word_count.items():
            print(f'{word}: {count}')
    elif choose == '2':
        certain_word = input('Введіть певне слово: ')
        print(f"Слово {certain_word} з'являлось в тексті {word_count.get(certain_word, 0)} разів.")
    elif choose == '3':
        print('До побачення!')
        break
    else:
        print('Виникла помилка при введенні, спробуйте знову.')