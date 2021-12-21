# Статические методы - методы, которые не требуют создания экземпляра класса.
#
# class MyClass:
#
#     def __init__(self):
#         self.a = 5
#
#     @staticmethod
#     def func(b, c):
#         return b * c
#
#
# def func():
#     return 3 ** 3
#
#
# print(MyClass.func(3, 3))
# print(func())

#
# class Player:
#
#     player_id = 1
#
#     def __init__(self, username):
#         self.username = username
#         self.__id = Player.player_id
#         self.level = 1
#         Player.player_id += 1
#
#     def lvl_up(self):
#         self.level += 1
#
#     @property
#     def id(self):
#         return self.__id
#
#     @id.setter
#     def id(self, player_id):
#         self.__id = player_id
#
#     # свойство - позволяет вызывать метод без использования()
#     @property
#     def get_info(self):
#         return f"{self.__id} {self.username}:{self.level} level "
#
#
# Petlitski = Player("Artem")
# Petlitski.lvl_up()
# print(Petlitski.id)
#
# Petlitski.id = 11
# print(Petlitski.id)
# print(Petlitski.get_info)
#
# Dima = Player("Dima")
# Dima.lvl_up()
# print(Dima.get_info)


# Задача . Написать класс Character-персонаж.Создать дочерний класс, который будет уточнять наш родительский класс

class Character:
    lvl = 1

    def __init__(self, name, health, mana):
        self._name = name
        self._health = health
        self._mana = mana
        self._lvl = Character.lvl

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Ошибка")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        if isinstance(health, (int, float)):
            self._health = health
        else:
            raise ValueError("Ошибка")

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, mana):
        if isinstance(mana, (int, float)):
            self._mana = mana
        else:
            raise ValueError("Ошибка")

    @property
    def level(self):
        return self._lvl

    @level.setter
    def level(self, lvl):
        if isinstance(lvl, int):
            self._lvl = lvl
        else:
            raise ValueError("Ошибка")

    def get_info(self):
        return f"{self.name}-lvl:{self.lvl},health-{self.health},mana-{self.mana}"


class Hero(Character):

    def __init__(self, username, health, mana, ultimate):
        Character.__init__(self, username, health, mana)
        self._ultimate = ultimate

    def get_info(self):
        return f"{self.name}-lvl:{self.lvl},health-{self.health},mana-{self.mana},ultimate -{self._ultimate}"


Artem = Character("Artem", 100, 100)
print(Artem.get_info())
Artem.health = 70
print(Artem.get_info())
Dima = Hero("dima", 100, 100, "Мощь")
print(Dima.get_info())
