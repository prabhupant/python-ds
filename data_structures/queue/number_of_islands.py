# Input: binary matrix, 0 means water, 1 means land
# Output: the number of islands

import sys
from queue import Queue
from typing import List


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    vlen = len(grid)
    hlen = len(grid[0])

    que = Queue()
    islandsCnt = 0

    for v in range(vlen):
        for h in range(hlen):
            if grid[v][h] == '1':
                que.put((v, h))
                islandsCnt += 1
                while not que.isEmpty():
                    curV, curH = que.get()
                    for x, y in (
                        [curV, curH - 1], [curV, curH + 1],
                            [curV - 1, curH], [curV + 1, curH]):
                        if (vlen > x >= 0 and hlen > y >= 0 and
                                grid[x][y] == "1"):
                            que.put((x, y))
                            grid[x][y] = "0"
    return islandsCnt
