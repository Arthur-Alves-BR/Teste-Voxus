from views import view1
from models.model1 import Model1


def action_1() -> None:
    data = Model1.get_entries("SELECT * FROM table1 WHERE name age = 35")
    countries = ("Mexico", "Chile", "Colombia", "Brazil")
    view1.render(_count_by_country(data, countries))


def action_2() -> None:
    data = Model1.get_entries("SELECT * FROM table1 WHERE name age = 35")
    south_america_countries = ("Chile", "Colombia", "Brazil")
    view1.render(_count_by_country(data, south_america_countries))


def _count_by_country(data: list, countries: list) -> dict:
    counter = {}
    for item in data:
        if item.country in counter:
            counter[item.country] += 1
        elif item.country in countries:
            counter[item.country] = 1

        result = {}
        for country, amount in counter.items():
            if amount == 1:
                result[country] = "Uma"
            elif amount == 2:
                result[country] = "Duas"
            elif amount == 3:
                result[country] = "Três"
    return result
