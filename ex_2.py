import turtle


def draw_pifagor_tree(t, branch_length, level):
    """
    Recursive function to draw a Pifagor tree using turtle graphics.
    Args:
        t (turtle.Turtle): The turtle object to draw with.
        branch_length (int): The length of the branches in the tree.
        level (int): The number of levels or recursion depth for the tree.
    Returns:
        None
    """
    if level == 0:
        return
    t.forward(branch_length)
    t.left(45)
    draw_pifagor_tree(t, int(0.6 * branch_length), level - 1)
    t.right(90)
    draw_pifagor_tree(t, int(0.6 * branch_length), level - 1)
    t.left(45)
    t.backward(branch_length)


def main():
    """
    A function to set up the main program, initialize turtle graphics, and draw a Pythagoras tree based on the given
    level of recursion.
    """
    level = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)
    t.color("red")
    t.left(90)
    t.up()
    t.backward(200)
    t.down()

    draw_pifagor_tree(t, 100, level)

    screen.exitonclick()


if __name__ == "__main__":
    main()
