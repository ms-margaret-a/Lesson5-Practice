# Создать(программно)текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

def summary():
    try:
        with open('task5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Неверный ввод')
summary()