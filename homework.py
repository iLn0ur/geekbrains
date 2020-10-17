from time import sleep


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self. surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus
        }


# задание №3


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


# задание №1


class TrafficLight:
    def __init__(self, n):
        self._color = {'red': '\033[31m',
                       'yellow': '\033[33m',
                       'green': '\033[32m'}
        self.n = n

    def running(self):
        for i in range(self.n):
            print(f'{self._color["red"]} red')
            sleep(7)
            print(f'{self._color["yellow"]} yellow')
            sleep(2)
            print(f'{self._color["green"]} green')
            sleep(7)


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self):
        print(f'{self._width * self._length * 25 * 5 / 1000} tons')


# задание №4


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, i=True):
        if i:
            print('авто движется')
        # self.stop(False)

    def stop(self, i=True):
        if i:
            print('авто остановилось')
        # self.go(False)

    def turn(self):
        direction = input('введите направление движения - влево или вправо')
        print(direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'{self.name}, превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'{self.name}, превышение скорости')


class PoliceCar(Car):
    pass


# задание №5


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки -', self.title)


class Pen(Stationery):
    def __init__(self, title='ручка'):
        self.title = title

    def draw(self):
        print(f'пишет {self.title}')


class Pencil(Stationery):
    def __init__(self, title='карандаш'):
        self.title = title

    def draw(self):
        print(f'подчеркивает {self.title}')

class Handle(Stationery):
    def __init__(self, title='маркер'):
        self.title = title

    def draw(self):
        print(f'выделяет {self.title}')


if __name__ == '__main__':
    # ivan = Position('ivan', 'petrov', 'worker', 100, 50)
    # print(ivan.get_full_name())
    # print(ivan.get_total_income())
    # n = input('enter how many times you want to see traffic lights')
    # traffic = TrafficLight(int(n))
    # traffic.running()
    # m = Road(20, 5000)
    # m.count_mass()

    # car = Car(59, 'blue', 'sedvik', False)
    # car.go()
    # car.stop()
    # car.show_speed()
    # town_car = TownCar(61, 'silver', 'honda', False)
    # town_car.show_speed()
    # town_car.go()
    # print(town_car.is_police)
    # police_car = PoliceCar(100, 'black', 'pharaon', True)
    # police_car.show_speed()
    # print(police_car.is_police)

    st = Stationery('кисть')
    st.draw()
    pen = Pen()
    pen.draw()
    pencil = Pencil()
    pencil.draw()
    handle = Handle()
    handle.draw()
