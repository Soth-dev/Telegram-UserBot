import random
import os
from typing import List, Dict, Tuple
from PIL import Image
from contextlib import ExitStack
import io
from telethon.events import NewMessage
from tgubot.handler.spy import SPY
from tgubot.plugin.functions import ARG, Q, M


@SPY(outgoing=True, pattern="!!maze (\\S+) (\\S+)")
async def maze(E: NewMessage.Event):
    input = "tgubot/assets/tiles/"
    width = int(ARG(E, 1))
    height = int(ARG(E, 2))
    await E.edit(Q(M(f"!!maze {width} {height}")), parse_mode="HTML")
    grid = create(width, height)
    fixed = fix(grid)
    im = rander(fixed, input)
    if im:
        with io.BytesIO() as buff:
            im.save(buff, "PNG")
            buff.name = "maze.png"
            buff.seek(0)
            if E.is_reply:
                await E.client.send_file(E.chat_id, buff, reply_to=E.reply_to_msg_id)
            else:
                await E.client.send_file(E.chat_id, buff, reply_to=E.id)
    await E.delete()


TILE_MAP = {
    "#": "full.png",
    " ": "empty.png",
    "t": "top.png",
    "b": "bottom.png",
    "l": "left.png",
    "r": "right.png",
    "w": "top_left.png",
    "a": "top_right.png",
    "s": "bottom_left.png",
    "d": "bottom_right.png",
    "h": "empty_top_left.png",
    "j": "empty_top_right.png",
    "k": "empty_bottom_left.png",
    "p": "empty_bottom_right.png",
}

HORIZ_MAP = {
    ("#", "#"): ["#", "#"],
    ("#", " "): ["#", "l"],
    (" ", "#"): [" ", "r"],
    (" ", " "): [" ", " "],
}


def create(width: int, height: int):
    grid_width = width * 2 + 1
    grid_height = height * 2 + 1

    grid = [["#" for _ in range(grid_width)] for _ in range(grid_height)]

    visited = [[False for _ in range(width)] for _ in range(height)]

    stack = [(0, 0)]
    visited[0][0] = True
    grid[1][1] = " "

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        cx, cy = stack[-1]
        unvisited_neighbors = []

        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < width and 0 <= ny < height:
                if not visited[ny][nx]:
                    unvisited_neighbors.append((nx, ny, dx, dy))

        if not unvisited_neighbors:
            stack.pop()
        else:
            nx, ny, dx, dy = random.choice(unvisited_neighbors)
            visited[ny][nx] = True

            grid[ny * 2 + 1][nx * 2 + 1] = " "

            wall_x = cx * 2 + 1 + dx
            wall_y = cy * 2 + 1 + dy
            grid[wall_y][wall_x] = " "

            stack.append((nx, ny))

    grid[1][0] = " "
    grid[grid_height - 2][grid_width - 1] = " "

    return grid


def _build_interp_map() -> Dict[Tuple[str, str, str], str]:
    """Generates an O(1) lookup dictionary for vertical tile interpolation."""
    m = {}
    for p in "#rad":
        m[("#", "#", p)] = "#"
    for p in " lhk":
        m[(" ", " ", p)] = " "
    m[("l", "l", "#")] = "l"
    m[("r", "r", " ")] = "r"
    for p in "twj":
        m[("#", " ", p)] = "t"
    for p in "bsp":
        m[(" ", "#", p)] = "b"
    m[("#", "l", "#")] = "w"
    m[("#", "r", "t")] = "a"
    m[("l", "#", "#")] = "s"
    m[("r", "#", "b")] = "d"
    m[("l", " ", "t")] = "h"
    m[("r", " ", " ")] = "j"
    m[(" ", "l", "b")] = "k"
    m[(" ", "r", " ")] = "p"
    return m


def rander(grid: List[List[str]], input_path: str) -> Image.Image | None:
    if not grid or not grid[0]:
        return

    with ExitStack() as stack:
        images = {
            char: stack.enter_context(Image.open(os.path.join(input_path, filename)))
            for char, filename in TILE_MAP.items()
        }

        cell_size = 16
        im = Image.new("RGB", (len(grid[0]) * cell_size, len(grid) * cell_size))

        for ir, row in enumerate(grid):
            y = ir * cell_size
            for i, char in enumerate(row):
                if char in images:
                    im.paste(images[char], (i * cell_size, y))
        return im


def _expand_horizontal(row: List[str]) -> List[str]:
    """Helper to handle the repetitive horizontal row expansion."""
    new_row = []
    for i in range(len(row) - 1):
        new_row.extend(HORIZ_MAP.get((row[i], row[i + 1]), [" ", " "]))
    new_row.append("#")
    return new_row


def fix(grid: List[List[str]]) -> List[List[str]]:
    if not grid or not grid[0]:
        return grid

    new_grid = []
    new_row1 = _expand_horizontal(grid[0])

    for irow in range(len(grid) - 1):
        new_row2 = _expand_horizontal(grid[irow + 1])
        new_row3 = []

        last = "t" if irow == 0 else "b" if irow == 1 else "#"

        for i in range(len(new_row1) - 1):
            char = _build_interp_map().get((new_row1[i], new_row2[i], last), "#")
            new_row3.append(char)
            last = char  # Update state

        new_row3.append("#")

        new_grid.append(new_row1)
        new_row1 = new_row2
        new_grid.append(new_row3)

    row_len = len(new_row1)
    new_grid.append(["#"] * row_len)

    try:
        new_grid[-3][-1] = " "
        new_grid[-4][-1] = "t"
        new_grid[-2][-1] = "b"

        new_grid[-2][-2] = "b"
    except IndexError:
        pass  # Safety net in case the grid is too small for these offsets

    return new_grid
