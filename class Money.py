from save_data import data, day, month, year


class Money:

    def __init__(self, value: float, charcode: str):
        self.value = value
        self.charcode = charcode

    def __str__(self):
        return f"{self.value} {self.charcode}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, {self.charcode})"

    def __add__(self, add_money):
        if isinstance(add_money, Money):
            if self.charcode == add_money.charcode:
                return Money(round(self.value + add_money.value, 2), self.charcode)
            else:
                raise TypeError("Разные валюты")
        else:
            return NotImplemented

    def __sub__(self, sub_money):
        if isinstance(sub_money, Money):
            if self.charcode == sub_money.charcode:
                return Money(round(self.value - sub_money.value, 2), self.charcode)
            else:
                raise TypeError("Разные валюты")
        else:
            return NotImplemented

    def __mul__(self, num):
        if isinstance(num, (int, float)):
            return Money(round(self.value * num, 2), self.charcode)
        else:
            return NotImplemented

    def __truediv__(self, num):
        if isinstance(num, (int, float)):
            return Money(round(self.value / num, 2), self.charcode)
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Money):
            return self.value > other.value
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.value < other.value
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Money):
            return self.value >= other.value
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Money):
            return self.value <= other.value
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.value == other.value
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Money):
            return self.value != other.value
        else:
            return NotImplemented

    def convert_to_usd(self) -> float:
        if self.charcode == "USD":
            return self.value

        elif self.charcode in data["Valute"]:
            value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
            value2 = data["Valute"]["USD"]["Value"]
            self.value = round(self.value * value1 / value2, 2)
            self.charcode = "USD"
            print(f"Конвертация в USD прошла по курсу на {day}.{month}.{year}\n{self.value} {self.charcode}")
            return self.value

        elif self.charcode == "RUB":
            self.value = round(self.value / data["Valute"]["USD"]["Value"], 2)
            self.charcode = "USD"
            return self.value

        else:
            raise TypeError("Валюты, которую вы хотите поменять, не принимают в обменнике")

    def convert_to_valute(self, valute: str):
        if valute == self.charcode:
            print(f"Деньги находятся уже в той валюте, в которую вы хотите их конвертировать")
            return None

        elif valute in data["Valute"]:
            value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
            value2 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
            self.value = round(self.value * value1 / value2, 2)
            self.charcode = valute
            print(f"Конвертация в USD прошла по курсу на {day}.{month}.{year}\n{self.value} {self.charcode}")
            return self.value

        elif valute == "RUB":
            value1 = data["Valute"][self.charcode]["Value"]
            value2 = data["Valute"][self.charcode]["Nominal"]
            self.value = round(self.value * value1 / value2, 2)
            self.charcode = valute
            print(f"Конвертация в USD прошла по курсу на {day}.{month}.{year}\n{self.value} {self.charcode}")
            return self.value

        else:
            raise TypeError("Валюты, в которую вы хотите конвертировать свои деньги, нет в обменнике")


money1 = Money(300, "CZK")
money2 = Money(324.56, "USD")
money3 = Money(770.99, "EUR")

print(money1)
money1.convert_to_valute("EUR")
print(money1)
