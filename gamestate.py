class Circle:
    def __init__(self, radius, x, y, type="Player"):
        self.radius = radius
        self.x = x
        self.y = y
        self.type = type

    def GetPoisiton(self):
        return self.x, self.y

    def SetPosition(self, x, y):
        self.x = x
        self.y = y


class GameState:
    def __init__(self, code):
        self.circles = []
        self.code = code

    def AddCircle(self, circle):
        self.circles.append(circle)


def Collisions(gameState):
    for i in range(len(gameState.circles)):
        for j in range(i + 1, len(gameState.circles)):
            circle1 = gameState.circles[i]
            circle2 = gameState.circles[j]
            x1, y1 = circle1.GetPoisiton()
            x2, y2 = circle2.GetPoisiton()
            if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (circle1.radius + circle2.radius) ** 2:
                return True
    return False
