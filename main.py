from __future__ import annotations
import copy
import random
from typing import Iterable, Iterator
from matplotlib import pyplot as plt
import generate_test

import timeit


class HalberAffe:
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


def opposite(pos: int) -> int:
    """
    Returns the opposite Affe
    """
    return (pos + 4) % 8


type Tile = tuple[int, int, int, int]


def check(tile: Tile, top: Tile | None, left: Tile | None) -> bool:
    return (top is None or tile[0] == opposite(top[2])) and (
        left is None or tile[1] == opposite(left[3])
    )


def rotate(tile: Tile) -> Iterator[Tile]:
    """
    Rotates the tile times*90 degrees clockwise.
    """
    yield tile
    yield (
        (
            tile[1],
            tile[2],
            tile[3],
            tile[0],
        )
    )
    yield (
        (
            tile[2],
            tile[3],
            tile[0],
            tile[1],
        )
    )
    yield (
        (
            tile[3],
            tile[0],
            tile[1],
            tile[2],
        )
    )


data = []


def backtrack(
    board: list[Tile | None], tiles: Iterable[Tile], k: int, index: int = 0
) -> None | list[Tile | None]:
    # print(f"starting backtrack with index {index}, {len(tiles)} tiles left and board. {board}")
    # data.append(index) # TODO
    if index >= k * k:
        return board
    initial = board[index]
    for original in tiles:
        for tile in rotate(original):
            if check(
                tile,
                board[index - k] if index > 4 else None,
                board[index - 1] if index % k > 0 else None,
            ):
                board[index] = tile
                rboard = backtrack(
                    board,
                    # tuple(filter(lambda x: x is not original, tiles)),
                    tuple(btile for btile in tiles if btile is not original),
                    k,
                    index + 1,
                )
                if rboard:
                    return rboard
    board[index] = initial
    return None


def main():
    b = 5
    k = 5
    random.seed(69)
    tiles = generate_test.get_numbers(k)
    print(
        timeit.timeit(
            f"main2(tiles, {k})",
            globals={**globals(), "tiles": copy.deepcopy(tiles)},
            number=b,
        )
        / b
    )


def main2(tiles, k):
    annalenabaerboard: list[Tile | None] = [None] * k**2
    result = backtrack(annalenabaerboard, tiles, k)
    if result is None:
        print("nonono")
        return
    # print(result)
    # for row in result:
    #     assert row is not None
    # print(
    #     "[",
    #     " | ".join(
    #         f"{tile[0]} {tile[1]} {tile[2]} {tile[3]}" # type: ignore
    #         for tile in row
    #     ),
    #     "]",
    # )


if __name__ == "__main__":
    main()
    # plt.plot(data)
    if data:
        plt.ylim(0, k**2)
        plt.bar(*zip(*enumerate(data)), width=1)
        plt.show()
