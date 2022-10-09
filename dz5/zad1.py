# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
my_text = 'London is a capital of GB'
print(my_text)
def del_some_words(my_text):
    my_text = list(filter(lambda x: input("Введите символ, слова с которым хотите удалить") not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)