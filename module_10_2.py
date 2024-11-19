import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, str, int):
        super().__init__()
        self.str = str
        self.int = int

    def run(self):
        print(f'{self.str}, на нас напали')
        health = 100
        days = 0
        while health > 0:
            health -=  self.int
            days += 1
            sleep(1)
            print(f'{self.str}, сражается {days} день(дня)..., осталось {health}.')
        print(f'{self.str} одержал победу спустя {days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')