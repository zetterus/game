class Character:
    '''any character general properties'''

    def __init__(self, name, hp, att, lvl):
        self.name = name
        self.hp = hp
        self.att = att
        self.lvl = lvl


class Player(Character):
    '''player properties'''

    def __init__(self, name, hp, att, lvl, xp, money, *skills):
        Character.__init__(self, name, hp, att, lvl)
        self.xp = xp
        self.money = money
        self.skills = skills


class NPC(Character):
    '''player properties'''

    def __init__(self, name, hp, att, lvl, xp_reward, loot):
        Character.__init__(self, name, hp, att, lvl)
        self.xp_reward = xp_reward
        self.loot = loot


class Item:
    '''general item properties'''

    def __init__(self, item_name, price, grade, weight, dur, enh, sock, set):
        self.item_name = item_name
        self.price = price
        self.grade = grade
        self.weight = weight
        self.dur = dur
        self.enh = enh
        self.sock = sock
        self.set = set


class Weapon(Item):
    '''general weapon properties'''

    def __init__(self, item_name, price, grade, weight, dur, enh, sock, set, type, dmg, arp, stamina_used):
        Item.__init__(self, item_name, price, grade, weight, dur, enh, sock, set)
        self.type = type
        self.dmg = dmg
        self.arp = arp
        self.stamina_used = stamina_used


class Armor(Item):
    '''general armor properties'''

    def __init__(self, item_name, price, grade, weight, dur, enh, sock, set, type, arm, stamina):
        Item.__init__(self, item_name, price, grade, weight, dur, enh, sock, set)
        self.type = type
        self.arm = arm
        self.stamina = stamina


# @staticmethod
def obj_info(self):
    for k, v in self.__dict__.items():
        print(f'{k}: {v}')


# checks
c = Character('dummy', 50, 5, 1)
obj_info(c)
print('-----')
p = Player('zetter', 55, 1, 1, 3, 2, None)
obj_info(p)
print('-----')
m = NPC('mob', 25, 3, 1, 1, None)
obj_info(m)
print('-----')
i = Item('object_1', 30, 'no', 1, 1, 0, 0, None)
obj_info(i)
print('-----')
w = Weapon('twisted_dirk', 100, 'no', 5, 20, 0, 0, None, 'dagger', 3, 1, 1)
obj_info(w)
print('-----')
a = Armor('shabby_vest', 75, 'no', 15, 50, 0, 0, None, 'Light', 1, 10)
obj_info(a)
print('-----')

# item names!!! vasya, mb item ids?

