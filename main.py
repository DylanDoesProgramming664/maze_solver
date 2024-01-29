from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    # Top Right: No Left or Top wall
    Maze(
        50,
        50,
        13,
        18,
        50,
        50,
        win,
    ).solve()
    win.wait_for_close()


if __name__ == "__main__":
    main()
