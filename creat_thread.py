# Импорты необходимых модулей и функций
import time
from threading import Thread


# Объявление функции write_words
def wite_words(word_count, file_name):
    with open(file_name, mode='w', encoding='cp1251') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} /n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


# Взятие текущего времени
started_at = time.time()
# Запуск функций с аргументами из задачи
wite_words(10, file_name='example1.txt')
wite_words(30, file_name='example2.txt')
wite_words(200, file_name='example3.txt')
wite_words(100, file_name='example4.txt')
# Взятие текущего времени
ended_at = time.time()
# Вывод разницы начала и конца работы функций
time_spent = round(ended_at - started_at, 6)
print(f'Работа потоков: {time_spent}')

# Взятие текущего времени
started_at = time.time()
# Создание и запуск потоков с аргументами из задачи
first_thr = Thread(target=wite_words, args=(10, 'example5.txt'))
second_thr = Thread(target=wite_words, args=(30, 'example6.txt'))
third_thr = Thread(target=wite_words, args=(200, 'example7.txt'))
forth_thr = Thread(target=wite_words, args=(100, 'example8.txt'))

first_thr.start()
second_thr.start()
third_thr.start()
forth_thr.start()

first_thr.join()
second_thr.join()
third_thr.join()
forth_thr.join()
# Взятие текущего времени
ended_at = time.time()
# Вывод разницы начала и конца работы потоков
time_spent = round(ended_at - started_at, 6)
print(f'Работа потоков: {time_spent}')
