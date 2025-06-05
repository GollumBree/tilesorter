from __future__ import annotations
from cty import FixedLengthTuple, Array
from matplotlib import pyplot as plt
import generate_test

k = 4


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

    @staticmethod
    def opposite(pos: int) -> int:
        """
        Returns the opposite Affe
        """
        return (pos + 4) % 8


type Tile = tuple[int, int, int, int]


def check(tile: Tile, top: Tile | None, left: Tile | None) -> bool:
    return (top is None or tile[0] == HalberAffe.opposite(top[2])) and (
        left is None or tile[1] == HalberAffe.opposite(left[3])
    )


def rotate(tile: Tile, times: int) -> Tile:
    """
    Rotates the tile times*90 degrees clockwise.
    """
    tile = (
        tile[times % 4],
        tile[(1 + times) % 4],
        tile[(2 + times) % 4],
        tile[(3 + times) % 4],
    )
    return tile


data = []


def backtrack(
    board: Array[Array[Tile]], tiles: tuple[Tile, ...], index: int = 0
) -> None | Array[Array[Tile]]:
    # print(f"starting backtrack with index {index}, {len(tiles)} tiles left and board. {board}")
    data.append(index)
    if index >= k * k:
        return board
    initial = board[index // k][index % k]
    for tile, original in [(rotate(t, i), t) for t in tiles for i in range(4)]:
        board[index // k][index % k] = tile
        if check(
            tile,
            board[index // k - 1][index % k] if index // k > 0 else None,
            board[index // k][(index % k) - 1] if index % k > 0 else None,
        ):
            rboard = backtrack(
                board,
                tuple(btile for btile in tiles if btile is not original),
                index + 1,
            )
            if rboard:
                return rboard
    board[index // k][index % k] = initial
    return None


type FixedLengthTuple[T] = tuple[T, ...]


def main():
    # tiles: FixedLengthTuple[Tile] = (
    #     (
    #         HalberAffe.GREEN_BOTTOM,
    #         HalberAffe.BLUE_BOTTOM,
    #         HalberAffe.GREEN_TOP,
    #         HalberAffe.RED_TOP,
    #     ),
    #     (
    #         HalberAffe.BLUE_BOTTOM,
    #         HalberAffe.RED_TOP,
    #         HalberAffe.RED_TOP,
    #         HalberAffe.GREEN_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.GREEN_BOTTOM,
    #         HalberAffe.YELLOW_TOP,
    #         HalberAffe.GREEN_TOP,
    #     ),
    #     (
    #         HalberAffe.RED_TOP,
    #         HalberAffe.YELLOW_BOTTOM,
    #         HalberAffe.GREEN_TOP,
    #         HalberAffe.GREEN_TOP,
    #     ),
    #     (
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.YELLOW_TOP,
    #         HalberAffe.GREEN_TOP,
    #         HalberAffe.GREEN_TOP,
    #     ),
    #     (
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.BLUE_BOTTOM,
    #         HalberAffe.YELLOW_BOTTOM,
    #         HalberAffe.GREEN_TOP,
    #     ),
    #     (
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.YELLOW_BOTTOM,
    #         HalberAffe.GREEN_TOP,
    #         HalberAffe.YELLOW_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.BLUE_BOTTOM,
    #         HalberAffe.YELLOW_TOP,
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.RED_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.RED_TOP,
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.YELLOW_BOTTOM,
    #         HalberAffe.RED_TOP,
    #     ),
    #     (
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.BLUE_BOTTOM,
    #         HalberAffe.RED_TOP,
    #         HalberAffe.GREEN_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.GREEN_BOTTOM,
    #         HalberAffe.GREEN_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.YELLOW_TOP,
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.GREEN_TOP,
    #     ),
    #     (
    #         HalberAffe.YELLOW_BOTTOM,
    #         HalberAffe.GREEN_BOTTOM,
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.GREEN_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.RED_BOTTOM,
    #         HalberAffe.GREEN_BOTTOM,
    #         HalberAffe.YELLOW_BOTTOM,
    #         HalberAffe.BLUE_BOTTOM,
    #     ),
    #     (
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.RED_TOP,
    #         HalberAffe.YELLOW_TOP,
    #         HalberAffe.GREEN_TOP,
    #     ),
    #     (
    #         HalberAffe.BLUE_TOP,
    #         HalberAffe.RED_TOP,
    #         HalberAffe.BLUE_BOTTOM,
    #         HalberAffe.BLUE_BOTTOM,
    #     ),
    # )
    tiles=generate_test.get_numbers(4)

    annalenabaerboard: Array[Array[Tile]] = Array(
        [Array[Tile](None for _ in range(k)) for _ in range(k)]
    )
    result = backtrack(annalenabaerboard, tiles)
    if result is None:
        print("nonono")
        return
    # print(result)
    for row in result:
        assert row is not None
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
    print(1)
    plt.plot(data)
    plt.show()
    print(2)
