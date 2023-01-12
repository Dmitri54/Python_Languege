import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Backup' # Подставьте ваш путь.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)
# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')

# Обратите внимание, что мы заменяем пробелы в комментарии подчёркиваниями: 
# управлять файлами без пробелов в именах намного легче.

# Дополнительные усовершенствования:
# 1. Добавить уровень подробности вывода, чтобы при указании параметра «-v» 
# она становилась более «разговорчивой».
# 2. Передавать сценарию другие файлы и каталоги прямо в командной строке. 
# Эти имена можно получать из списка sys.argv и добавлять к нашему списку source 
# при помощи метода extend класса list
# 4. Прекращение использования os.system для создания архивов, а применение вместо него
#  встроенных модулей zipfile или tarfile. Они являются частью стандартной библиотеки, 
# поэтому всегда доступны для использования без зависимости от внешней программы zip на компьютере.