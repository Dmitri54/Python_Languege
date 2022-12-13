# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях).
# Пример: 
# 2*x² + 4*x + 5 = 0 
# +
# x² + 5 = 0
# Ответ: 3*x² = 4*x + 10 = 0
# =======================================================================================================
f = open ('/Users/User/Desktop/Python_Language/HomeWork004/file_hw005.0.txt', 'r')
l = [line.strip() for line in f]
f = open ('/Users/User/Desktop/Python_Language/HomeWork004/file_hw005.1.txt', 'r')
m = [line.strip() for line in f]
l_1 = str(l).split(' + ')
m_1 = str(m).split(' + ')
count = 6
new_list = []
while count > 0:
    for i in l_1:
        a = str('x^' + str(count))
        if a in i:
            b = i
            for j in m_1:
                c = str('x^' + str(count))
                if c in j:
                    d = j
                    e = b + d
                    new_list.append(e)

        count -= 1
new_list.append(l[-1] + m[-1])

print(new_list)
# Не доделана.

