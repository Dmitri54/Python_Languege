# Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# --------------------------------------------------------------------------------------------------
# Выполнение алгоритма сжатия данных кодирования длин серий (RLE) для строки `str`
def encode(s):
 
    encoding = "" # сохраняет выходную строку. Изначально пустая строка. 
    i = 0
    while i < len(s):
        # подсчитывает количество вхождений символа в индексе `i`
        count = 1
 
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
 
        # добавляет к результату текущий символ и его количество
        encoding += str(count) + s[i]
        i = i + 1
 
    return encoding
 
 
if __name__ == '__main__':
 
    s = 'aaabbcf'
    print(encode(s))  # 3a2b1c1f

    