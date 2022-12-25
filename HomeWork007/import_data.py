# модуль импорта данных

path = r'/Users/User/Desktop/Python_Language/HomeWork007/phone.csv'

def import_data(data, sep=None):
    with open(path, 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")