"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета
  количества разных слов, где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя форматирование
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  при этом не делить слова.
"""


def wiki_function():
    list_strok = []
    new_list_strok = []

    # открытие файла
    file1 = open("wiki.txt", "r")

    # если сторка не пустая, то добавить
    for line in file1:
        if line != '\n':
            list_strok.append(line)

    # закрыть файл
    file1.close

    # если буква и пробел, то присоеденить
    for i in range(len(list_strok)):
        new_list_strok.append("".join(c for c in list_strok[i] if (c.isalpha() or c == " ")))

    # соединяем в одну строку и разделяем пробелом
    final_stroka = " ".join(new_list_strok)

    # делим строку по словам
    final_stroka = final_stroka.split(" ")
    dictt = {}

    # добавляем слова в словарь
    for i in range(len(final_stroka)):
        if (not (final_stroka[i] in dictt.keys())):
            dictt[final_stroka[i]] = 1
        else:
            dictt[final_stroka[i]] += 1

    # создаем список из пар в словаре и сортируем по второму значению
    dictt = list(dictt.items())
    dictt.sort(key=lambda i: i[1])
    dictt.reverse()

    # вывод самых встречемых слов
    for i in range(1,11):
       print (i, 'place ---', dictt[i-1][0], '---', dictt[i-1][1], 'times')

    # создаем список из 10 самых встречающихся слов
    list_10 = []
    for i in range(10):
        list_10.append(dictt[i][0])

    # замена 10 самых встречаемых слов на PYTHON
    for i in range(len(final_stroka)):
        if (final_stroka[i] in list_10):
            final_stroka[i] = "PYTHON"

    # создаем и открываем новый файл и записываем в него
    new_file = open("new wiki file.txt", "w+")
    s = 0
    for i in range(len(final_stroka)):
        if ((s + len(final_stroka[i]) + 1) > 100):
            new_file.write('\n')
            s = 1
        s = s + len(final_stroka[i]) + 1
        new_file.write(final_stroka[i] + " ")
    new_file.close()


# Вызов функции
wiki_function()
