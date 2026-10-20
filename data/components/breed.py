from __future__ import annotations

import random
from typing import List, Optional, Tuple, TYPE_CHECKING

import numpy as np  # type: ignore
import tcod

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor


class Breed(BaseComponent):
    parent: Actor
    def __init__(self, breed_max_hp: int):
        self.breed_hp = breed_max_hp