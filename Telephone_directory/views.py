import sys
import csv


path = r'/Users/User/Desktop/Python_Language/Telephone_directory/data.csv'

def add(i):
    with open(path, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)


def view():
    data = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

# view()

def remove(i):
    def save(j):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i

    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)
    save(new_list)


# remove('54321')
# view()

def update(i):
    def update_newlist(j):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i[0]
    # ['123', 'demo','M','123', 'demo@gmail.com']

    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]

                    data = [name, gender, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

# sample = ['123', 'boyCoder', 'M', '123', 'boy123@gmail.com']
# update(sample)

def search(i):
    data = []
    telephone = i

    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    print(data)
    return data

search('123')