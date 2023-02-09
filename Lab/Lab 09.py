# import library
from random import randint

class Entity:
    # Lengkap constructor
    # Perhatikan access modifiernya!
    def __init__(self, name, hp, atk):
        self.__name=name
        self.__hp=hp
        self.__atk=atk

    # Lengkapi getter dan setter
    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_hp):
        self.__hp=new_hp

    # Lengkapi method-method dibawah ini
    def attack(self, other:object):
        other.take_damage(self.__atk)

    def take_damage(self, damage):
        self.__hp-=damage

    def is_alive(self):
        return self.__hp>0

    def __str__(self):
        # Akan digunakan untuk print nama
        return self.__name


class Player(Entity):
    # Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, hp, atk, defense):
        Entity.__init__(self,name,hp,atk)
        self.__defense=defense
    # Lengkapi getter
    def get_defense(self):
        return self.__defense

    # Lengkapi agar damage yang diterima dikurangi oleh DEF
    def take_damage(self, damage):
        if damage < self.__defense:
            Entity.take_damage(self,0)
        else:
            Entity.take_damage(self,damage-self.__defense)

class Boss(Entity):
    def __init__(self, name, hp, atk):
        super().__init__(name, hp, atk)

    # Lengkapi agar damage yang diterima Depram tidak dipengaruhi
    #       oleh DEF
    def attack(self, other:object):
        other.take_damage(self.get_atk()+other.get_defense()) # static method jika pakai entity


def main():
    # Meminta ATK dan DEF Depram
    atk = int(input("Masukkan ATK Depram: "))
    defense = int(input("Masukkan DEF Depram: "))

    # Inisialisasi Depram dan musuh-musuh
    depram = Player("Depram", 100, atk, defense)
    enemies = [
        Entity(f"Enemy {i}", randint(20, 100), randint(10,30))
        for i in range(randint(0, 1))
    ]
    enemies.append(Boss("Ohio Final Boss", randint(20, 100), randint(10,30)))

    print(f"Terdapat {len(enemies)} yang menghadang Depram!")
    print("------------")
    # for loop sesuai jumlah musuh
    for enemy in enemies:
        print(f"{enemy} muncul!")
        print()
        print("---Status---") # output hp 
        print(f"{enemy.get_name():20} HP: {enemy.get_hp()}")
        print(f"{depram.get_name():20} HP: {depram.get_hp()}")
        print("------------")
        while enemy.is_alive() and depram.is_alive():
            # Depram dan musuh melakukan attack dan print:
            # Depram menyerang: "Depram menyerang {enemy} dengan {damage} ATK!"
            # Musuh  menyerang: "{enemy} menyerang Depram dengan {damage} ATK!"
            # print output
            if enemy.get_hp() <= 0:
                break
            if isinstance(enemy, Entity) and not isinstance(enemy, Boss):
                print(f'Depram menyerang {enemy.get_name()} dengan {depram.get_atk()} ATK!')
                depram.attack(enemy)
                if defense > enemy.get_atk():
                    print(f'{enemy.get_name()} menyerang Depram dengan 0 ATK!')
                else:
                    print(f'{enemy.get_name()} menyerang Depram dengan {enemy.get_atk()-defense} ATK!')
                enemy.attack(depram)
            else:
                print(f'Depram menyerang {enemy.get_name()} dengan {depram.get_atk()} ATK!')
                depram.attack(enemy)
                print(f'{enemy.get_name()} menyerang Depram dengan {enemy.get_atk()} ATK!')
                enemy.attack(depram)

        # jika sudah mati
        if not depram.is_alive():
            print("------------")
            print()
            print("Tidak! Depram telah dikalahkan oleh musuhnya :(")
            return
        else:
            print(f"{enemy} telah kalah!")

        print("------------")
        print()

    print("Selamat! Semua musuh Depram telah kalah!")


if __name__ == "__main__":
    main()