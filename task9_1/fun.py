import pygame

def field_lines(scr):
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 2)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 2)

def cross_and_toe(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == "0":
                pygame.draw.circle(scr, (37, 40, 80), (j * 100 + 50, i * 100 + 50), 40)
            elif items[i][j] == "x":
                pygame.draw.line(scr, (66, 49, 137), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 2)
                pygame.draw.line(scr, (66, 49, 137), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 2)

def game_result(fd, symbol):
    flag_win = False
    for line in fd:
        if line.count(symbol) == 3:
            flag_win = True
    for i in range(3):
        if fd[0][i] == fd[1][i] == fd[2][i] == symbol:
            flag_win = True
    if fd[0][0] == fd[1][1] == fd[2][2] == symbol:
        flag_win = True
    if fd[0][2] == fd[1][1] == fd[2][0] == symbol:
        flag_win = True
    return flag_win