#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


# Базовый класс для всех юнитов
class Unit:
    __id_counter = 1  # Для генерации уникальных идентификаторов

    def __init__(self, team: str):
        self.id = Unit.__id_counter  # Уникальный идентификатор
        Unit._id__counter += 1
        self.team = team  # Команда, к которой принадлежит юнит


# Класс солдата
class Soldier(Unit):
    def __init__(self, team: str):
        super().__init__(
            team
        )  # Инициализируем базовые свойства через класс Unit

    def follow_hero(self, hero):
        """Солдат следует за героем"""
        if isinstance(hero, Hero):
            print(
                "Солдат {self.id} идет за героем "
                f"{hero.id} из команды {hero.team}"
            )


# Класс героя
class Hero(Unit):
    def __init__(self, team: str):
        super().__init__(team)
        self.level = 1  # Уровень героя

    def level_up(self):
        """Увеличивает уровень героя"""
        self.level += 1
        print(
            "Герой {self.id} из команды "
            f"{self.team} повысил уровень до {self.level}"
        )


# Класс команды
class Team:
    def __init__(self, name: str):
        self.name = name
        self.soldiers = []  # Список солдат команды
        self.hero = None  # Герой команды

    def add_hero(self):
        """Добавляет героя в команду"""
        self.hero = Hero(self.name)
        print(f"Герой {self.hero.id} добавлен в команду {self.name}")

    def add_soldier(self):
        """Добавляет солдата в команду"""
        soldier = Soldier(self.name)
        self.soldiers.append(soldier)
        print(f"Солдат {soldier.id} добавлен в команду {self.name}")

    def get_soldier_count(self):
        """Возвращает количество солдат в команде"""
        return len(self.soldiers)

    def level_up_hero(self):
        """Увеличивает уровень героя команды"""
        if self.hero:
            self.hero.level_up()

    def follow_hero(self, index: int):
        """Отправляет первого солдата следовать за героем"""
        if self.soldiers and self.hero:
            first_soldier = self.soldiers[index]
            first_soldier.follow_hero(self.hero)
            return first_soldier.id, self.hero.id
        return None, None


# Основная логика программы
def main():
    # Создаем команды
    team_red = Team("Red")
    team_blue = Team("Blue")

    # Добавляем по одному герою в каждую команду
    team_red.add_hero()
    team_blue.add_hero()

    # Генерируем 10 случайных солдат и добавляем их в соответствующие команды
    for _ in range(10):
        team = random.choice([team_red, team_blue])
        team.add_soldier()

    # Выводим длины списков солдат
    print(f"Солдаты команды {team_red.name}: {team_red.get_soldier_count()}")
    print(f"Солдаты команды {team_blue.name}: {team_blue.get_soldier_count()}")

    # Увеличиваем уровень героя команды с большим количеством солдат
    if team_red.get_soldier_count() > team_blue.get_soldier_count():
        team_red.level_up_hero()
    elif team_blue.get_soldier_count() > team_red.get_soldier_count():
        team_blue.level_up_hero()
    else:
        print("Количество солдат в обеих командах одинаково.")

    # Отправляем одного из солдат команды Red следовать за ее героем
    team_red.follow_hero(0)


if __name__ == "__main__":
    main()
