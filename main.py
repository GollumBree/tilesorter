from __future__ import annotations
from enum import Enum, auto
from cty import FixedLengthTuple, Array


class Affe(Enum):
    """
    Enum for Affe
    """

    RED_TOP = auto()
    RED_BOTTOM = auto()
    YELLOW_TOP = auto()
    YELLOW_BOTTOM = auto()
    GREEN_TOP = auto()
    GREEN_BOTTOM = auto()
    BLUE_TOP = auto()
    BLUE_BOTTOM = auto()


type Tile = tuple[Affe, Affe, Affe, Affe]

tiles: FixedLengthTuple[Tile, 16] = ()
board: Array[Array[Tile]] = Array([Array[Tile](4) for _ in range(4)])


