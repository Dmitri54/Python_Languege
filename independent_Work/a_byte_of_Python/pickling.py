# pickle, при помощи стандартного модуля, можно сохранять любой объект Python в файле, 
# а затем извлекать его обратно. 
# Это называется длительным хранением объекта.


import pickle

# имя файла, в котором мы сохраним объект
shoplistfile = '/Users/User/Desktop/Python_Language/independent_Work/a_byte_of_Python/shoplist.data'

# список покупок
shoplist = ['яблоки', 'манго', 'морковь']

# Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в файл
f.close()

del shoplist # уничтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем объект из файла
print(storedlist)
