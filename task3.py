class Tv:
    def __init__(self, b, c):
        self.b=b
        self.c=c

    def num(self):
        print("Вы успешно включили телевизор")

    def v1(self):
        x = int(input('Введите громкость'))
        if x > 100:
            print('Громкость установлена на макс.')
        elif x <= 100 and x >= 0:
            print('Громкость изменена')
            x1 = 0
            x1 = x
        elif x < 0:
            print('Громкость установлена на минимум')
            x1 = 0
        print('Сейчас', x1, 'уровень громкости')
    def v2(self):
        x2 = int(input('Изменить канал'))
        if x2 > 32:
            print('Не бывает каналов выше 32')
        elif x2 <=32 and x2 > 0:
            print('Канал изменён')
            x3 = x2
        elif x2<=0:
            print('Не бывает каналов ниже 1го')
            print('Сейчас показывает', x3, 'канал')
def main():
    crit = Tv()
    x1 = 0
    x3 = 0
    choice = None  
    while choice != "0":
        print \
        ("""
        Телевизор
    
        0 - Выйти
        1 - Включить телевизор
        2 - Настроить звук
        3 - Изменить канал
        4 - Узнать настройки звука, каналов
        """)
    
        choice = input("Ваш выбор: ")
        print()

        if choice == "0":
            print("Вы выключили телевизор")

        elif choice == "1":
            crit.num=int(input('Номер канала:'))
        
        elif choice == "2":
            crit.v1=int(input('Изменить громкость:'))
        else:
            print("Извините, в меню нет пункта", choice)
    
main()