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
    fighter=Fighter(hp=20, base_defense=10, base_power=12),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

drekirsivilao = Actor(
    char="D",
    color=(100, 100, 0),
    name="Dralk",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=25, base_defense=11, base_power=12),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)
ormersivilao = Actor(
    char="O",
    color=(100, 100, 0),
    name="Orm",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=50, base_defense=11, base_power=13),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
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
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    color=(255, 255, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)

knife = Item(
    char="/", color=(100, 100, 100), name="Knife", equippable=equippable.Knife()
)

shortblade = Item(char="/", color=(100, 100, 100), name="Sword", equippable=equippable.ShortBlade())

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
    color=(100, 100, 100),
    name="Heavy Shield",
    equippable=equippable.HeavyShield(),
)