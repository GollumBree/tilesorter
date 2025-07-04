from main import check, HalberAffe

raw_tiles = """RED_BOTTOM YELLOW_BOTTOM GREEN_BOTTOM GREEN_BOTTOM | BLUE_BOTTOM GREEN_TOP RED_BOTTOM GREEN_BOTTOM | BLUE_BOTTOM GREEN_TOP RED_BOTTOM GREEN_BOTTOM | BLUE_BOTTOM GREEN_TOP RED_BOTTOM GREEN_BOTTOM | BLUE_BOTTOM GREEN_TOP RED_BOTTOM GREEN_BOTTOM 
 GREEN_TOP RED_BOTTOM GREEN_BOTTOM BLUE_BOTTOM | RED_TOP BLUE_TOP GREEN_BOTTOM YELLOW_TOP | RED_TOP YELLOW_BOTTOM BLUE_BOTTOM BLUE_TOP | RED_TOP BLUE_BOTTOM GREEN_TOP BLUE_TOP | RED_TOP BLUE_BOTTOM GREEN_TOP BLUE_TOP 
 GREEN_TOP RED_BOTTOM GREEN_BOTTOM BLUE_BOTTOM | GREEN_TOP BLUE_TOP YELLOW_BOTTOM GREEN_BOTTOM | BLUE_TOP GREEN_TOP GREEN_TOP YELLOW_TOP | GREEN_BOTTOM YELLOW_BOTTOM GREEN_TOP BLUE_TOP | GREEN_BOTTOM BLUE_BOTTOM GREEN_TOP RED_BOTTOM 
 GREEN_TOP BLUE_BOTTOM BLUE_BOTTOM GREEN_BOTTOM | YELLOW_TOP GREEN_TOP BLUE_TOP RED_TOP | GREEN_BOTTOM RED_BOTTOM BLUE_BOTTOM YELLOW_TOP | GREEN_BOTTOM YELLOW_BOTTOM GREEN_TOP BLUE_TOP | GREEN_BOTTOM BLUE_BOTTOM RED_TOP RED_TOP 
 BLUE_TOP RED_TOP YELLOW_BOTTOM BLUE_BOTTOM | BLUE_BOTTOM BLUE_TOP BLUE_BOTTOM RED_TOP | BLUE_TOP RED_BOTTOM GREEN_BOTTOM RED_TOP | GREEN_BOTTOM RED_BOTTOM GREEN_TOP GREEN_TOP | RED_BOTTOM GREEN_BOTTOM RED_TOP BLUE_TOP """

grid = [
    [tuple(HalberAffe[name] for name in tile.split()) for tile in row.split(" | ")]
    for row in raw_tiles.strip().split("\n")
]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not check(
            grid[i][j], # type: ignore
            grid[i - 1][j] if i > 0 else None, # type: ignore
            grid[i][j - 1] if j > 0 else None, # type: ignore
        ):
            print(
                f"Tile at (x:{j}, y:{i}) is invalid with its neighbors (to the left or up)."
            )
print("All tiles checked.")
