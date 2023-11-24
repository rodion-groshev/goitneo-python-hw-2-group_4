from collections import defaultdict
from datetime import datetime


def get_birthday_per_week(users):
    default_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days < 7:
            if birthday_this_year.strftime("%A") in ["Saturday", "Sunday"] and delta_days <= 5:
                default_dict[birthday_this_year.strftime("Monday")].append(name)
            else:
                default_dict[birthday_this_year.strftime("%A")].append(name)

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    default_dict = {day: default_dict[day] for day in week}

    for day in default_dict:
        if default_dict[day]:
            print(f"{day}: {', '.join(default_dict[day])}")


if __name__ == "__main__":
    get_birthday_per_week([{"name": "Bill Gates", "birthday": datetime(1955, 11, 21)},
                           {"name": "Eva Smith", "birthday": datetime(1945, 11, 24)},
                           {"name": "Steve Jobs", "birthday": datetime(1945, 11, 25)},
                           {"name": "Adam Smith", "birthday": datetime(1945, 11, 26)}

                           ])
