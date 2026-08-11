from components.ai import HostileEnemy
from components import consumable
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char="@",
    color=(100, 100, 100),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=20, defense=10, power=12),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

dralk = Actor(
    char="D",
    color=(100, 100, 50),
    name="Dralk",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=25, defense=11, power=11),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=75),
)
ormersivilao = Actor(
    char="O",
    color=(100, 100, 0),
    name="Orm",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=50, defense=11, power=12),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)

confusion_scroll = Item(
    char="~",
    color=(100, 100, 0),
    name="Confusion Scroll",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="~",
    color=(100, 100, 0),
    name="Fireball Scroll",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
health_potion = Item(
    char="!",
    color=(100, 0, 0),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="~",
    color=(100, 100, 0),
    name="Lightning Scroll",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)