from class_Money import Money
from save_data import data, day, month, year


class KZT(Money):
    """
    Класс, который описывает казахстанский тенге
    """

    def convert_to_rub(self) -> Money:
        """
        Метод, который конвертирует валюту в рубли создает экземпляр класса Money в рублях
        :return: возвращает экземпляр класса Money в рублях
        """
        value1 = data["Valute"][self.charcode]["Value"] / data["Valute"][self.charcode]["Nominal"]
        self.value = round(self.value * value1, 2)
        self.charcode = "RUB"
        print(f"Конвертация в RUB прошла по курсу на {day}.{month}.{year}\n{self.value} {self.charcode}")
        return Money(self.value, "RUB")


if __name__ == '__main__':
    money = KZT(300, "KZT")
    print(money)
    money.convert_to_rub()
    print(money)
