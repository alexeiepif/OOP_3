#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Разработайте программу по следующему описанию.
# В некой игре-стратегии есть солдаты и герои. У всех есть свойство,
# содержащее уникальный номер объекта, и свойство, в котором
# хранится принадлежность команде. У солдат есть метод "иду за героем",
# который в качестве аргумента принимает объект типа "герой".
# У героев есть метод увеличения собственного уровня.
#
# В основной ветке программы создается по одному герою для
# каждой команды. В цикле генерируются объекты-солдаты. Их
# принадлежность команде определяется случайно. Солдаты
# разных команд добавляются в разные списки.
#
# Измеряется длина списков солдат противоборствующих команд
# и выводится на экран. У героя, принадлежащего команде
# с более длинным списком, увеличивается уровень.
#
# Отправьте одного из солдат первого героя следовать за ним.
# Выведите на экран идентификационные номера этих двух юнитов.

import random


class Unit:
    __id_counter = 1

    def __init__(self, team: str):
        self.id = Unit.__id_counter
        Unit.__id_counter += 1
        self.team = team


class Soldier(Unit):
    def __init__(self, team: str):
        super().__init__(team)

    def follow_hero(self, hero):
        if isinstance(hero, Hero):
            print(
                f"Солдат {self.id} идет за героем "
                f"{hero.id} из команды {hero.team}"
            )


class Hero(Unit):
    def __init__(self, team: str):
        super().__init__(team)
        self.level = 1

    def level_up(self):
        self.level += 1
        print(
            f"Герой {self.id} из команды "
            f"{self.team} повысил уровень до {self.level}"
        )


class Team:
    def __init__(self, name: str):
        self.name = name
        self.soldiers = []
        self.hero = None

    def add_hero(self):
        self.hero = Hero(self.name)
        print(f"Герой {self.hero.id} добавлен в команду {self.name}")

    def add_soldier(self):
        soldier = Soldier(self.name)
        self.soldiers.append(soldier)
        print(f"Солдат {soldier.id} добавлен в команду {self.name}")

    def get_soldier_count(self):
        return len(self.soldiers)

    def level_up_hero(self):
        if self.hero:
            self.hero.level_up()

    def follow_hero(self, index: int):
        if self.soldiers and self.hero:
            first_soldier = self.soldiers[index]
            first_soldier.follow_hero(self.hero)
            return first_soldier.id, self.hero.id
        return None, None


def main():
    team_red = Team("Red")
    team_blue = Team("Blue")

    team_red.add_hero()
    team_blue.add_hero()

    for _ in range(10):
        team = random.choice([team_red, team_blue])
        team.add_soldier()

    print(f"Солдаты команды {team_red.name}: {team_red.get_soldier_count()}")
    print(f"Солдаты команды {team_blue.name}: {team_blue.get_soldier_count()}")

    if team_red.get_soldier_count() > team_blue.get_soldier_count():
        team_red.level_up_hero()
    elif team_blue.get_soldier_count() > team_red.get_soldier_count():
        team_blue.level_up_hero()
    else:
        print("Количество солдат в обеих командах одинаково.")

    team_red.follow_hero(0)


if __name__ == "__main__":
    main()
