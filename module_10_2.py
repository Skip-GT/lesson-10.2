from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            sleep(1)
            self.enemies -= self.power
            self.days += 1
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(я)!")


knights = [
        Knight('Sir Lancelot', 10),
        Knight('Sir Galahad', 20)
    ]


for knight in knights:
    knight.start()

for knight in knights:
    knight.join()

print("Все битвы закончились!")
