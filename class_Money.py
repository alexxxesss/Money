from save_data import data, day, month, year


class Money:
    """
    Класс, который описывает счет, на котором находятся денежные средства.

    Валюта, в которой деньги хранятся на счете должны быть из списка, представленного в файле price
    Если при инициализации не указать валюту, то автоматически создается экземпляр класса в рублях.

    Денежные средства, находящиеся на счете, могут быть конвертированы в другие валюты по текущему курсу ЦБ
    (или по последнему курсу, когда был доступ в интернет).

    Для конвертации в USD создан отдельный метод convert_to_usd().

    Методы класса:
    convert_to_usd(): Конвертирует денежные средства, находящиеся на счете в доллары США
    convert_to_valute(): Конвертирует денежные средства, находящиеся на счете в любую валюту из списка
    _convert_to_valute_for_compare(): Конвертирует денежные средства, находящиеся на счете в любую валюту из списка
    для методов сравнения
    """
    def __init__(self, value: (int, float), charcode: str = "RUB"):
        """
        Инициализация экземплаяра класса Money
        Леха петух
        тест строка 1
        тест строка 2
        тест строка 3
        :param value: Количество денег
        :param charcode: Наименование валюты в виде трех заглавных букв латинского алфавита.
        Используются международные общепринятые наименования (смотри файл price)
        """
        self.value = value
        self.charcode = charcode
        self.date = f"Данные на {day}.{month}.{year}"

    def __str__(self):
        return f"{self.value} {self.charcode}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value}, {self.charcode})"

    def __add__(self, add_money: "Money"):
        if isinstance(add_money, Money):
            if self.charcode == add_money.charcode:
                return Money(round(self.value + add_money.value, 2), self.charcode)
            else:
                raise TypeError("Разные валюты")
        else:
            return NotImplemented

    def __sub__(self, sub_money: "Money"):
        if isinstance(sub_money, Money):
            if self.charcode == sub_money.charcode:
                return Money(round(self.value - sub_money.value, 2), self.charcode)
            else:
                raise TypeError("Разные валюты")
        else:
            return NotImplemented

    def __mul__(self, num: int):
        if isinstance(num, (int, float)):
            return Money(round(self.value * num, 2), self.charcode)
        else:
            return NotImplemented

    def __truediv__(self, num: int):
        if isinstance(num, (int, float)):
            return Money(round(self.value / num, 2), self.charcode)
        else:
            return NotImplemented

    def __gt__(self, other: "Money"):
        if isinstance(other, Money):
            if self.charcode == other.charcode:
                return self.value > other.value
            else:
                return self.value > other._convert_to_valute_for_compare(self.charcode)
        else:
            return NotImplemented

    def __lt__(self, other: "Money"):
        if isinstance(other, Money):
            if self.charcode == other.charcode:
                return self.value < other.value
            else:
                return self.value < other._convert_to_valute_for_compare(self.charcode)
        else:
            return NotImplemented

    def __ge__(self, other: "Money"):
        if isinstance(other, Money):
            if self.charcode == other.charcode:
                return self.value >= other.value
            else:
                return self.value >= other._convert_to_valute_for_compare(self.charcode)
        else:
            return NotImplemented

    def __le__(self, other: "Money"):
        if isinstance(other, Money):
            if self.charcode == other.charcode:
                return self.value <= other.value
            else:
                return self.value <= other._convert_to_valute_for_compare(self.charcode)
        else:
            return NotImplemented

    def __eq__(self, other: "Money"):
        if isinstance(other, Money):
            if self.charcode == other.charcode:
                return self.value == other.value
            else:
                return self.value == other._convert_to_valute_for_compare(self.charcode)
        else:
            return NotImplemented

    def __ne__(self, other: "Money"):
        if isinstance(other, Money):
            return self.value != other.value
        else:
            return NotImplemented

    def convert_to_usd(self) -> float:
        """
        Метод конвертирует денежные средства, находящиеся на счете в доллары США

        :return: возвращает сумму на счете в долларах США
        """
        if self.charcode == "USD":
            return self.value

        elif self.charcode in data["Valute"]:
            value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
            value2 = data["Valute"]["USD"]["Value"]
            self.value = round(self.value * value1 / value2, 2)
            self.charcode = "USD"
            self.date = f"Данные на {day}.{month}.{year}"
            print(f"Конвертация в USD прошла по курсу на {day}.{month}.{year}\n{self.value} {self.charcode}")
            return self.value

        elif self.charcode == "RUB":
            self.value = round(self.value / data["Valute"]["USD"]["Value"], 2)
            self.charcode = "USD"
            self.date = f"Данные на {day}.{month}.{year}"
            return self.value

        else:
            raise TypeError("Валюты, которую вы хотите поменять, не принимают в обменнике")

    def convert_to_valute(self, valute: str):
        """
        Метод конвертирует денежные средства, находящиеся на счете в любую валюту из списка
        Данные используются только для сравнения разных валют. Атрибуты не изменяются
        Для выбора спользуются международные общепринятые наименования (смотри файл price)

        :param valute: Валюта, в которую нужно перевести средства, находящиеся на счете
        :return: возвращает сумму на счете в нужной валюте
        """
        if valute == self.charcode:
            print(f"Деньги находятся уже в той валюте, в которую вы хотите их конвертировать")
            return None

        elif valute in data["Valute"]:
            if self.charcode == "RUB":
                value1 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
                self.value = round(self.value / value1, 2)
                self.charcode = valute
                self.date = f"Данные на {day}.{month}.{year}"
                print(f"Конвертация в {self.charcode} прошла по курсу "
                      f"на {day}.{month}.{year}\n{self.value} {self.charcode}")
                return self.value

            else:
                value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
                value2 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
                self.value = round(self.value * value1 / value2, 2)
                self.charcode = valute
                self.date = f"Данные на {day}.{month}.{year}"
                print(f"Конвертация в {self.charcode} прошла по курсу "
                      f"на {day}.{month}.{year}\n{self.value} {self.charcode}")
                return self.value

        elif valute == "RUB":
            value1 = data["Valute"][self.charcode]["Value"]
            value2 = data["Valute"][self.charcode]["Nominal"]
            self.value = round(self.value * value1 / value2, 2)
            self.charcode = valute
            self.date = f"Данные на {day}.{month}.{year}"
            print(f"Конвертация в {self.charcode} прошла по курсу "
                  f"на {day}.{month}.{year}\n{self.value} {self.charcode}")
            return self.value

        else:
            raise TypeError("Валюты, в которую вы хотите конвертировать свои деньги, нет в обменнике")

    def _convert_to_valute_for_compare(self, valute: str):
        """
        Метод конвертирует денежные средства, находящиеся на счете в любую валюту из списка, без изменения самого счета
        Для выбора спользуются международные общепринятые наименования (смотри файл price)

        :param valute: Валюта, в которую нужно перевести средства, находящиеся на счете
        :return: возвращает сумму на счете в нужной валюте
        """

        if valute in data["Valute"]:
            value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
            value2 = data["Valute"][valute]["Value"] / data["Valute"][valute]["Nominal"]
            new_value = round(self.value * value1 / value2, 2)
            print(f"Сравнение прошло по курсу на {day}.{month}.{year}")
            return new_value

        elif valute == "RUB":
            value1 = data["Valute"][self.charcode]["Value"]
            value2 = data["Valute"][self.charcode]["Nominal"]
            new_value = round(self.value * value1 / value2, 2)
            print(f"Сравнение прошло по курсу на {day}.{month}.{year}")
            return new_value

        else:
            raise TypeError("Валюты, в которую вы хотите конвертировать свои деньги, нет в обменнике")


if __name__ == '__main__':

    bank_account1 = Money(3000, "CZK")
    bank_account2 = Money(150, "USD")
    bank_account3 = Money(200, "EUR")

    print("------------")
    print(bank_account1)
    print(bank_account2)
    print(bank_account3)
    print("------------")
    bank_account1.convert_to_valute("RUB")
    print("------------")
    print(bank_account1.date)
    print("------------")
    print(bank_account1 > bank_account2)
    print("------------")
    print(bank_account1)
    print(bank_account2)
    print(bank_account3)
    print("------------")
    print(bank_account1 < bank_account3)
    print("------------")
    bank_account1.convert_to_valute("CZK")
    print("------------")
    bank_account2.convert_to_valute("EUR")
    print("------------")
    bank_account2.convert_to_usd()
    print("------------")
    print(bank_account1)
    print(bank_account2)
    print(bank_account3)
    print("------------")
