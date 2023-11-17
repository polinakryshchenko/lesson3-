import random
import logging

logging.basicConfig(filename='sims.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def log_event(message):
    logging.info(message)

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Auto:
    car_brands = {
        'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
        'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
        'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
        'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14},
    }

    def __init__(self):
        self.brand = random.choice(list(Auto.car_brands))
        self.fuel = Auto.car_brands[self.brand]['fuel']
        self.strength = Auto.car_brands[self.brand]['strength']
        self.consumption = Auto.car_brands[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class Job:
    vacancies = {
        'Java Developer': {'salary': 50, 'gladness_less': 10},
        'Python Developer': {'salary': 40, 'gladness_less': 3},
        'C++ Developer': {'salary': 45, 'gladness_less': 25},
        'Rust Developer': {'salary': 70, 'gladness_less': 1},
    }

    def __init__(self):
        self.job_name = random.choice(list(Job.vacancies))
        self.salary = Job.vacancies[self.job_name]['salary']
        self.gladness_less = Job.vacancies[self.job_name]['gladness_less']


class Human:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = None
        self.car = None
        self.home = None

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto()

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < self.car.consumption:
                manage = 'fuel'
                return
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'sweets':
            print('Yummy-yummy!')
            self.money -= 15
            self.satiety += 2
            self.gladness += 10

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day_str = f'Today is the {day} of {self.name}\'s life'
        log_event(f"{day_str:=^50}")
        #print(f"{day_str:=^50}", "\n")
        indexes_str = f'{self.name}\'s Indexes:'
        print(f"{indexes_str:^50}", "\n")
        print(f"money: {self.money}")
        print(f"gladness: {self.gladness}")
        print(f"satiety: {self.satiety}")
        indexes_str = 'Home Indexes:'
        print(f"{indexes_str:^50}", "\n")
        print(f"food: {self.home.food}")
        print(f"mess: {self.home.mess}")
        indexes_str = f'{self.car.brand}\'s Indexes:'
        print(f"fuel: {self.car.fuel}")
        print(f"strength: {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        elif self.satiety < 0:
            print('Hungry Death')
            return False
        elif self.money < -500:
            print('Bankrupt!')
            return False
        else:
            return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            print('Bought a car')
            self.get_car()
        if self.job is None:
            print('Got a job')
            self.get_job()

        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            print('Ill go eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print('I have to clean my house still')
                self.clean_home()
            else:
                print('Chilllllll')
                self.chill()
        elif self.money < 0:
            print('Start working')
            self.work()
        elif self.car.strength < 15:
            print('I need to repair my car')
            self.to_repair()
        elif dice == 1:
            print('Chillllll')
            self.chill()
        elif dice == 2:
            print('Start working')
            self.work()
        elif dice == 3:
            print('I have to clean my house still')
            self.clean_home()
        elif dice == 4:
            print('Time for sweets!')
            self.shopping('sweets')
        return True


illya = Human(name='Illya')

for day in range(1, 366):
    day_done = illya.live(day)
    if not day_done:
        break

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.happiness = 50

    def feed(self):
        self.happiness += 10

    def play(self):
        self.happiness += 20

    def check_happiness(self):
        if self.happiness > 100:
            self.happiness = 100
        elif self.happiness < 0:
            self.happiness = 0
        return self.happiness

    def pet_status(self):
        return f"{self.name} the {self.species} - Happiness: {self.happiness}"


class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Current balance: ${self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.balance}"
        else:
            return "Insufficient funds."

    def check_balance(self):
        return f"Current balance: ${self.balance}"