# class User:
#     user_id = 1
#
#     def __init__(self, fname, lname, email=None):
#         self.fname = fname
#         self.lname = lname
#         self.email = email
#         self.id = User.user_id
#         User.user_id += 1
#
#     def get_info(self):
#         print(f"{self.id}--{self.fname} {self.lname}:{self.email} ")
#
#     def __str__(self):
#         return self.fname
#
#     def __int__(self):
#         print("Вы переводите меня в int")
#         return self.__id
#
#
# class Manager(User):
#
#     def __init__(self, fname, lname, status, salary, email=None):
#         User.__init__(self, fname, lname, email)
#         self.status = status
#         self.salary = salary
#
#     def get_info(self):
#         User.get_info(self)
#         print(f"{self.status},{self.salary}")
#
#
#
#
# #
# Vasya = User("Артём", "Дмитриевич")
# Dima = User("Дима", "Иванович", "dima@email.com")
# Vasya.get_info()
#
# ivan = Manager("Дима", "Иванов", "Директор", 1300)
# ivan.get_info()
# #
# Vasya.get_info()
# Dima.get_info()
#
# print(int(Dima))


class Tomato():
    states = {
        1: "Зеленый",
        2: "Желтый",
        3: "Красный"
    }

    def __init__(self, _index):
        self._index = _index
        self.stadion = 1
        self.status = Tomato.states[self.stadion]

    def get_info(self):
        print(self.status)

    def grow(self):
        self.stadion += 1
        self.status = Tomato.states[self.stadion]

    def is_ripe(self):
        if self.stadion == 3:
            print("Созрел")
        else:
            print("Не созрел")


class TomatoBush(Tomato):

    def __init__(self, count):
        self.count = count
        self.tomatoes = []
        for i in range(count):
            self.tomatoes.append(Tomato(1))

    def grow_all(self):
        for i in range(len(self.tomatoes)):
            self.tomatoes[i].grow()

    def all_are_ripe(self):
        for i in range(len(self.tomatoes)):
            if self.tomatoes[i].stadion != 3:
                print("Не все созрели")
                break
        else:
            print("Все созрели")

    def give_away_ripe(self):
        i = 0
        while i < len(self.tomatoes):
            if self.tomatoes[i].stadion == 3:
                del self.tomatoes[i]
            else:
                i += 1


toma = TomatoBush(3)

toma.tomatoes[1].get_info()
toma.grow_all()
toma.tomatoes[1].grow()
toma.tomatoes[2].grow()
toma.tomatoes[1].get_info()
toma.tomatoes[2].get_info()
toma.all_are_ripe()
print(len(toma.tomatoes))
toma.give_away_ripe()
toma.tomatoes[0].get_info()
toma.grow_all()
toma.all_are_ripe()
print(len(toma.tomatoes))
# toma.tomatoes[1].get_info()
# toma.all_are_ripe()

toma_1 = TomatoBush(2)


