from gamestate import GameState, Circle, Collisions
from render import Render
from network import CreateLobby, JoinLobby


def main():
    gameState = CreateLobby()

    print(Collisions(gameState))
    Render(gameState)


if __name__ == "__main__":
    main()
