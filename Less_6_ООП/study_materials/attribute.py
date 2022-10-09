class Auto:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def on_auto_start(self, auto_name, auto_model, auto_year):
        print("Двигатель запущен.")
        # атрибуты экземпляра класса
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto.auto_count += 1


a = Auto()
a.on_auto_start("Жигули", "2121", 1973)
print(a.auto_name, a.auto_model)
print(a.auto_count)

a_2 = Auto()
a.on_auto_start("Москвич", "412", 1980)
print(a.auto_name, a.auto_model)
print(a.auto_count)

a = Auto()
a.on_auto_start("Жигули", "2121", 1973)
print(a.auto_name, a.auto_model)
print(a.auto_count)