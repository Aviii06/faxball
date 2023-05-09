from gamestate import GameState, Circle


def Render(gamestate):
    for circle in gamestate.circles:
        print(circle.type, circle.radius, circle.x, circle.y)
