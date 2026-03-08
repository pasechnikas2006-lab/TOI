class Firearm:
    def __init__(self, name: str ,weapon_class: str, caliber: float, effective_range: float, rof: float, mag_capacity:int, manufacturer: str) -> None:
        self.name = name
        self.weapon_class = weapon_class
        self.caliber = caliber
        self.effective_range = effective_range
        self.rof = rof
        self.mag_capacity = mag_capacity
        self.Manufacturer = manufacturer

    def get_name(self) -> str:
        return self.name
    def get_weapon_class(self) -> str:
        return self.weapon_class
    def get_caliber(self) -> float:
        return self.caliber
    def get_effective_range(self) -> float:
        return self.effective_range
    def get_rof(self) -> float:
        return self.rof
    def get_mag_capacity(self) -> int:
        return self.mag_capacity
    def get_manufacturer(self) -> str:
        return self.Manufacturer
    def __str__(self) -> str:
        return (f"{self.name} \n"
                f"Калибр: {self.caliber}мм \n"
                f"эффективная дальность: {self.effective_range}м \n"
                f"скорострельность: {self.rof}в/м \n"
                f"ёмкость магазина: {self.mag_capacity} патронов\n"
                f"производитель: {self.Manufacturer} ")
AssaultRifle1 = Firearm("AR16", "AR" ,5.56, 500, 750, 30, "Armalite Armory" )
print(AssaultRifle1)
