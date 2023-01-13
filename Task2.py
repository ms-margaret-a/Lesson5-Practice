# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_file = open('test_task2.txt', 'r')
content = my_file.read()
print(f'Содержит: \n {content}')
my_file = open('test_task2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк: {len(content)}')
my_file = open('test_task2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество слов: {len(content)}')
my_file.close()