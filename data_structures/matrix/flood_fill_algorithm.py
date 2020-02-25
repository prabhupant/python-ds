# Reference - https://www.geeksforgeeks.org/flood-fill-algorithm-implement-fill-paint/

# Dimensions of paint screen
M = 8
N = 8

def flood_fill_util(screen, x, y, prev_color, new_color):
    if x < 0 or x >= M or y < 0 or y >= N or screen[x][y] != prev_color or screen[x][y] == new_color:
        return

    screen[x][y] = new_color
    flood_fill_util(screen, x + 1, y, prev_color, new_color)
    flood_fill_util(screen, x - 1, y, prev_color, new_color)
    flood_fill_util(screen, x, y + 1, prev_color, new_color)
    flood_fill_util(screen, x, y - 1, prev_color, new_color)


def flood_fill(screen, x, y, new_color):
    prev_color = screen[x][y] # Finding the previous color on x and y
    flood_fill_util(screen, x, y, prev_color, new_color)



