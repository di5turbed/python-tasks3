class Car:
    vehicle_type = "Автомобиль"
    fuel_types = ["Бензиновая", "Дизель", "Электрическая", "Гибрид"]

    def __init__(self, brand: str, model: str, year: int, color: str, engine_power_hp: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_power_hp = engine_power_hp
        self.mileage_km = 0

    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.year}), {self.color}, {self.engine_power_hp} ЛС"

    def is_powerful(self) -> bool:
        return self.engine_power_hp > 200

    def drive(self, distance_km: int) -> None:
        self.mileage_km += distance_km
        print(f"Машина проехала {distance_km} км. Пробег: {self.mileage_km} km")

    def repaint(self, new_color: str) -> None:
        print(f"Перекраска из {self.color} в {new_color}")
        self.color = new_color

    def get_age(self, current_year: int) -> int:
        return current_year - self.year


car1 = Car("Toyota", "Prius Alpha", 2021, "Серебристый", 99)
car2 = Car("Ferrari", "Testarossa", 1986, "Красный", 340)
car3 = Car("Volksvagen", "Jetta", 2013, "Синий", 102)

print(car1)
print(car2.is_powerful())
car3.drive(15000)
car1.repaint("Чёрный")
print(car1.color)
print(f"Возраст : {car3.get_age(2025)} лет")