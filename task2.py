class Hero:
    def get_description(self):
        pass

    def get_power(self):
        pass


class Warrior(Hero):
    def get_description(self):
        return "Warrior"

    def get_power(self):
        return 100


class Mage(Hero):
    def get_description(self):
        return "Mage"

    def get_power(self):
        return 80


class Palladin(Hero):
    def get_description(self):
        return "Palladin"

    def get_power(self):
        return 90


class InventoryDecorator(Hero):
    def __init__(self, hero):
        self.hero = hero

    def get_description(self):
        return self.hero.get_description()

    def get_power(self):
        return self.hero.get_power()


class Armor(InventoryDecorator):
    def get_description(self):
        return self.hero.get_description() + " + Plate Armor"

    def get_power(self):
        return self.hero.get_power() + 30


class Weapon(InventoryDecorator):
    def get_description(self):
        return self.hero.get_description() + " + Sharp Sword"

    def get_power(self):
        return self.hero.get_power() + 50


class Artifact(InventoryDecorator):
    def get_description(self):
        return self.hero.get_description() + " + Magic Ring"

    def get_power(self):
        return self.hero.get_power() + 20


if __name__ == "__main__":
    hero = Warrior()
    print("Base: " + hero.get_description() + " (Power: " + str(hero.get_power()) + ")")

    hero_with_armor = Armor(hero)
    hero_fully_equipped = Weapon(hero_with_armor)

    print(
        "Equipped: " + hero_fully_equipped.get_description() + " (Power: " + str(hero_fully_equipped.get_power()) + ")")

    mage = Artifact(Mage())
    print("Mage Equipped: " + mage.get_description() + " (Power: " + str(mage.get_power()) + ")")