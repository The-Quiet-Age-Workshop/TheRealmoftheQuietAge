from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=20, mana=2, sleep=100, thirst=100, base_defense=10, base_power=1),
    inventory=Inventory(capacity=7),
    level=Level(level_up_base=200),
)

bulverfijal = Actor(
    char="B",
    color=(50, 100, 0),
    name="Temperate Bul",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=15, mana=2, sleep=100, thirst=100, base_defense=0, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

bulverkal = Actor(
    char="B",
    color=(100, 100, 100),
    name="Arctic Bul",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=20, mana=2, sleep=100, thirst=100, base_defense=0, base_power=9),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

bulverpura = Actor(
    char="B",
    color=(50, 50, 0),
    name="Arid Bul",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=15, mana=2, sleep=100, thirst=100, base_defense=0, base_power=8),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

bulverjuln = Actor(
    char="B",
    color=(0, 100, 0),
    name="Tropical Bul",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=10, mana=2, sleep=100, thirst=100, base_defense=0, base_power=7),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)

drekirfijal = Actor(
    char="d",
    color=(50, 100, 0),
    name="Temperate Drek",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=20, mana=2, sleep=100, thirst=100, base_defense=10, base_power=4),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=50),
)

drekirpura = Actor(
    char="d",
    color=(50, 50, 0),
    name="Arid Drek",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=20, mana=2, sleep=100, thirst=100, base_defense=10, base_power=4),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=50),
)

drekirjalan = Actor(
    char="d",
    color=(100, 100, 50),
    name="Alpine Drek",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=15, mana=2, sleep=100, thirst=100, base_defense=10, base_power=3),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=25),
)

drekirjuln = Actor(
    char="d",
    color=(0, 100, 0),
    name="Tropical Drek",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=15, mana=2, sleep=100, thirst=100, base_defense=10, base_power=3),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=25),
)

drekirkal = Actor(
    char="D",
    color=(100, 100, 100),
    name="Arctic Drek",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=25, mana=2, sleep=100, thirst=100, base_defense=10, base_power=5),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=75),
)

drekirsivilao = Actor(
    char="D",
    color=(100, 100, 0),
    name="Dralk",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=25, mana=2, sleep=100, thirst=100, base_defense=11, base_power=5),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=75),
)

ormerfijal = Actor(
    char="O",
    color=(50, 50, 0),
    name="Temperate Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=45, mana=2, sleep=100, thirst=100, base_defense=10, base_power=8),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=75),
)

ormerpura = Actor(
    char="O",
    color=(50, 50, 0),
    name="Arid Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=45, mana=2, sleep=100, thirst=100, base_defense=10, base_power=8),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=75),
)

ormerjalan = Actor(
    char="O",
    color=(100, 100, 50),
    name="Alpine Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=40, mana=2, sleep=100, thirst=100, base_defense=10, base_power=7),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=50),
)

ormerjuln = Actor(
    char="O",
    color=(0, 100, 0),
    name="Tropical Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=40, mana=2, sleep=100, thirst=100, base_defense=10, base_power=7),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=50),
)

ormerkal = Actor(
    char="O",
    color=(100, 100, 100),
    name="Arctic Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=50, mana=2, sleep=100, thirst=100, base_defense=10, base_power=9),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=100),
)

ormersivilao = Actor(
    char="O",
    color=(100, 100, 0),
    name="Caste Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=50, mana=2, sleep=100, thirst=100, base_defense=11, base_power=9),
    inventory=Inventory(capacity=7),
    level=Level(xp_given=100),
)

tirndarfijal = Actor(
    char="T",
    color=(50, 100, 0),
    name="Temperate Tirn",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=20, mana=2, sleep=100, thirst=100, base_defense=0, base_power=12),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

tirndarkal = Actor(
    char="T",
    color=(100, 100, 100),
    name="Arctic Tirn",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=25, mana=2, sleep=100, thirst=100, base_defense=0, base_power=13),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)

tirndarpura = Actor(
    char="T",
    color=(50, 50, 0),
    name="Arid Tirn",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=20, mana=2, sleep=100, thirst=100, base_defense=0, base_power=12),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=50),
)

tirndarklar = Actor(
    char="T",
    color=(100, 100, 50),
    name="Alpine Tirn",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(food=100, hp=15, mana=2, sleep=100, thirst=100, base_defense=0, base_power=11),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=25),
)

confusion_scroll = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(255, 0, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
rations = Item(
    char="!",
    color=(127, 255, 150),
    name="Rations",
    consumable=consumable.Food(amount=100),
)
blanket = Item(
    char="~",
    color=(255, 175, 150),
    name="Blanket",
    consumable=consumable.Bed(amount=100),
)
bandages = Item(
    char="~",
    color=(255, 127, 150),
    name="Bandages",
    consumable=consumable.HealingConsumable(amount=2),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

knife = Item(
    char="/",
    color=(100, 100, 100),
    name="Knife",
    equippable=equippable.Knife()
)

hatchet = Item(
    char="/",
    color=(100, 100, 100),
    name="Hatchet",
    equippable=equippable.Hatchet())

club = Item(
    char="/",
    color=(100, 100, 100),
    name="Club",
    equippable=equippable.Club())

shortblade = Item(
    char="/",
    color=(100, 100, 100),
    name="Short Blade",
    equippable=equippable.ShortBlade())

light_armour = Item(
    char="[",
    color=(100, 100, 0),
    name="Light Armour",
    equippable=equippable.LightArmour(),
)

medium_armour = Item(
    char="[",
    color=(100, 100, 50),
    name="Medium Armour",
    equippable=equippable.MediumArmour(),
)

heavy_armour = Item(
    char="[",
    color=(100, 100, 100),
    name="Heavy Armour",
    equippable=equippable.HeavyArmour(),
)

light_shield = Item(
    char="[",
    color=(100, 100, 0),
    name="Light Shield",
    equippable=equippable.LightShield(),
)

medium_shield = Item(
    char="[",
    color=(100, 100, 50),
    name="Medium Shield",
    equippable=equippable.MediumShield(),
)

heavy_shield = Item(
    char="[",
    color=(100, 100, 100),
    name="Heavy Shield",
    equippable=equippable.HeavyShield(),
)