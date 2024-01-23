from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)
    # Top Left: No Right or Bottom wall
    c = Cell(win)
    c.has_right_wall = False
    c.has_bottom_wall = False
    c.draw(50, 50, 100, 100)

    # Bottom Right: No Left or Bottom wall
    c = Cell(win)
    c.has_left_wall = False
    c.has_bottom_wall = False
    c.draw(100, 100, 150, 150)

    # Bottom Left: No Right or Top wall
    c = Cell(win)
    c.has_right_wall = False
    c.has_top_wall = False
    c.draw(50, 100, 100, 150)

    # Top Right: No Left or Top wall
    c = Cell(win)
    c.has_left_wall = False
    c.has_top_wall = False
    c.draw(100, 50, 150, 100)

    win.wait_for_close()


if __name__ == "__main__":
    main()
