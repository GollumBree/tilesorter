from __future__ import annotations
from enum import Enum
from cty import FixedLengthTuple, Array
from copy import deepcopy

k = 4


class HalberAffe(Enum):
    """
    Enum for Affe
    Red=Rot, Yellow=Braun, Green=Grün, Blue=Grau
    """

    RED_TOP = 0
    YELLOW_TOP = 1
    GREEN_TOP = 2
    BLUE_TOP = 3
    RED_BOTTOM = 4
    YELLOW_BOTTOM = 5
    GREEN_BOTTOM = 6
    BLUE_BOTTOM = 7

    def opposite(self) -> HalberAffe:
        """
        Returns the opposite Affe
        """
        return HalberAffe((self.value + 4) % 8)


type Tile = tuple[HalberAffe, HalberAffe, HalberAffe, HalberAffe]


def check(tile: Tile, top: Tile | None, left: Tile | None) -> bool:
    return (top is None or tile[0] == top[2].opposite()) and (
        left is None or tile[1] == left[3].opposite()
    )


def rotate(tile: Tile, times: int) -> Tile:
    """
    Rotates the tile times*90 degrees clockwise.
    """
    for _ in range(times % 4):
        tile = (tile[1], tile[2], tile[3], tile[0])
    return tile


def backtrack(
    board: Array[Array[Tile]], tiles: tuple[Tile, ...], index: int = 0
) -> None | Array[Array[Tile]]:
    #print(f"starting backtrack with index {index}, {len(tiles)} tiles left and board. {board}")
    if index >= k * k:
        return board
    for tile, original in [(rotate(t, i), t) for t in tiles for i in range(4)]:
        board[index // k][index % k] = tile
        if check(
            tile,
            board[index // k - 1][index % k] if index // k > 0 else None,
            board[index // k][(index % k) - 1] if index % k > 0 else None,
        ):
            rboard = backtrack(
                deepcopy(board),
                tuple(btile for btile in tiles if btile is not original),
                index + 1,
            )
            if rboard:
                return rboard
    return None

type FixedLengthTuple[T] = tuple[T, ...]

def main():
    tiles: FixedLengthTuple[Tile] = ((HalberAffe.GREEN_BOTTOM, HalberAffe.BLUE_BOTTOM, HalberAffe.GREEN_TOP, HalberAffe.RED_TOP), (HalberAffe.BLUE_BOTTOM, HalberAffe.RED_TOP, HalberAffe.RED_TOP, HalberAffe.GREEN_BOTTOM), (HalberAffe.RED_BOTTOM, HalberAffe.GREEN_BOTTOM, HalberAffe.YELLOW_TOP, HalberAffe.GREEN_TOP), (HalberAffe.RED_TOP, HalberAffe.YELLOW_BOTTOM, HalberAffe.GREEN_TOP, HalberAffe.GREEN_TOP), (HalberAffe.BLUE_TOP, HalberAffe.YELLOW_TOP, HalberAffe.GREEN_TOP, HalberAffe.GREEN_TOP), (HalberAffe.RED_BOTTOM, HalberAffe.BLUE_BOTTOM, HalberAffe.YELLOW_BOTTOM, HalberAffe.GREEN_TOP), (HalberAffe.BLUE_TOP, HalberAffe.YELLOW_BOTTOM, HalberAffe.GREEN_TOP, HalberAffe.YELLOW_BOTTOM), (HalberAffe.BLUE_BOTTOM, HalberAffe.YELLOW_TOP, HalberAffe.RED_BOTTOM, HalberAffe.RED_BOTTOM), (HalberAffe.RED_TOP, HalberAffe.BLUE_TOP, HalberAffe.YELLOW_BOTTOM, HalberAffe.RED_TOP), (HalberAffe.RED_BOTTOM, HalberAffe.BLUE_BOTTOM, HalberAffe.RED_TOP, HalberAffe.GREEN_BOTTOM), (HalberAffe.RED_BOTTOM, HalberAffe.RED_BOTTOM, HalberAffe.GREEN_BOTTOM, HalberAffe.GREEN_BOTTOM), (HalberAffe.BLUE_TOP, HalberAffe.YELLOW_TOP, HalberAffe.RED_BOTTOM, HalberAffe.GREEN_TOP), (HalberAffe.YELLOW_BOTTOM, HalberAffe.GREEN_BOTTOM, HalberAffe.BLUE_TOP, HalberAffe.GREEN_BOTTOM), (HalberAffe.RED_BOTTOM, HalberAffe.GREEN_BOTTOM, HalberAffe.YELLOW_BOTTOM, HalberAffe.BLUE_BOTTOM), (HalberAffe.BLUE_TOP, HalberAffe.RED_TOP, HalberAffe.YELLOW_TOP, HalberAffe.GREEN_TOP), (HalberAffe.BLUE_TOP, HalberAffe.RED_TOP, HalberAffe.BLUE_BOTTOM, HalberAffe.BLUE_BOTTOM))

    annalenabaerboard: Array[Array[Tile]] = Array([Array[Tile](k) for _ in range(k)])
    result = backtrack(annalenabaerboard, tiles)
    if result is None:
        print("nonono")
        return
    # print(result)
    for row in result:
        assert row is not None
        print(
            "[",
            " | ".join(
                f"{tile[0].name} {tile[1].name} {tile[2].name} {tile[3].name}" # type: ignore
                for tile in row
            ),
            "]",
        )


if __name__ == "__main__":
    main()
