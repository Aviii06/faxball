from gamestate import GameState, Circle
import random
import socket
import sys

GlobalCodes = []
GlobalGames = {}


def GenCode():
    if len(GlobalCodes) == 10000:
        raise Exception("Too many lobbies")

    code = ""
    for _ in range(4):
        code += str(random.randint(0, 9))

    if code in GlobalCodes:
        return GenCode()

    return code


def CreateLobby():
    code = GenCode()
    gameState = GameState(code)
    gameState.AddCircle(Circle(50, 300, 269, "Ball"))
    gameState.AddCircle(Circle(50, 300, 300))

    # s = socket.socket()
    # try:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     print("Socket successfully created")
    # except socket.error as err:
    #     print("Socket creation failed with error %s" % (err))
    #
    # port = 12345
    # try:
    #     host_ip = socket.gethostbyname("localhost")
    # except socket.gaierror:
    #     print("There was an error resolving the host")
    #     sys.exit()
    #
    # s.connect((host_ip, port))
    host_ip = "localhost"
    port = 12345
    GlobalGames[code] = (host_ip, port)
    return gameState


def JoinLobby(code):
    if code in GlobalCodes:
        return GlobalGames[code]
    else:
        raise Exception("Invalid code")
