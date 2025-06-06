import random
from typing import Tuple

from more_itertools import flatten


def generate_valid_grid(n=4):
    grid = [[None for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # Seiten, die von Nachbarn bestimmt werden
            top = None
            left = None

            if i > 0:
                above_tile = grid[i - 1][j]
                top_color, top_type = above_tile[2]
                top = (top_color, opposite_type(top_type))

            if j > 0:
                left_tile = grid[i][j - 1]
                left_color, left_type = left_tile[1]
                left = (left_color, opposite_type(left_type))

            # Zufällige Wahl, falls noch nicht festgelegt
            if top is None:
                top = random_side()
            if left is None:
                left = random_side()

            # Zufällige right und bottom Seiten
            right = random_side()
            bottom = random_side()

            tile = (top, right, bottom, left)
            grid[i][j] = tile
    return grid


def to_halberaffe(color: str, typ: str) -> str:
    color_map = {"R": "RED", "G": "GREEN", "B": "BLUE", "Y": "YELLOW"}
    type_map = {"O": "TOP", "U": "BOTTOM"}
    return f"HalberAffe.{color_map[color]}_{type_map[typ]}"


def to_number(color: str, typ: str) -> int:
    color_map = {"R": 0, "G": 1, "B": 2, "Y": 3}
    type_map = {"O": 0, "U": 4}
    return color_map[color] + type_map[typ]


def opposite_type(t: str) -> str:
    return "U" if t == "O" else "O"


Side = Tuple[str, str]
colors = ["R", "G", "B", "Y"]
types = ["O", "U"]


def random_side() -> Side:
    return random.choice(colors), random.choice(types)


def convert_tile_to_halberaffe(tile):
    return tuple(to_halberaffe(*side) for side in tile)

def convert_tile_to_number(tile):
    return tuple(to_number(*side) for side in tile)

def rotate_tile(
    tile: Tuple[str, str, str, str], times: int
) -> Tuple[str, str, str, str]:
    top, right, bottom, left = tile
    for _ in range(times % 4):
        top, right, bottom, left = left, top, right, bottom
    return (top, right, bottom, left)


def shuffle_and_rotate(grid, n=4):
    random.shuffle(grid)
    tiles = [rotate_tile(tile, random.randint(0, 3)) for tile in grid]
    return tuple(tiles[i * n : (i + 1) * n] for i in range(n))


def get_numbers(n):
    grid = generate_valid_grid(n)
    final = shuffle_and_rotate([convert_tile_to_number(grid[i][j]) for i in range(len(grid)) for j in range(len(grid))], n)
    return tuple(flatten(final))


def main(n):
    # Generiere, mische und rotiere
    grid = generate_valid_grid(n)
    # print("Generated 4x4 grid:")
    # for row in grid_4x4:
    #     print(row)
    final = shuffle_and_rotate(
        [convert_tile_to_halberaffe(grid[i][j]) for i in range(len(grid)) for j in range(len(grid))],
        n,
    )
    # print("\nShuffled and rotated tiles:")
    # for row in final_4x4:
    #     print(row)

    print(
        "("
        + ", ".join(
            (
                "(" + ", ".join(str(side) for side in tile) + ")"
                for tile in flatten(final)
            )
        )
        + ")"
    )


if __name__ == "__main__":
    main(4)
