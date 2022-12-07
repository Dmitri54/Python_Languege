class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса, содержащая количество роботов
    population = 0
    def __init__(self, name):
        '''Инициализация данных.'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        # При создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1
    def __del__(self):
        '''Я умираю.'''
        print('{0} уничтожается!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последним.'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов.'.format(Robot.population))
    def sayHi(self):
        '''Приветствие робота.

        Да, они это могут.'''
        print('Приветствую! Мои хозяева называют меня {0}.'.format(self.name))
    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов.'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2') # (Инициализация R2-D2)
droid1.sayHi()          # Приветствую! Мои хозяева называют меня R2-D2.
Robot.howMany()         # У нас 1 роботов.

droid2 = Robot('C-3PO') # (Инициализация C-3PO)
droid2.sayHi()          # Приветствую! Мои хозяева называют меня C-3PO.
Robot.howMany()         # У нас 2 роботов.

print("\nЗдесь роботы могут проделать какую-то работу.\n")

print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1              # R2-D2 уничтожается!
                        # Осталось 1 работающих роботов.
del droid2              # C-3PO уничтожается!
                        # C-3PO был последним.
Robot.howMany()         # У нас 0 роботов.
