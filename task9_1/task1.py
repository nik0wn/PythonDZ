import pygame
import fun
import random

SIZE_FIELD = (300, 300)

WINDOW = pygame.display.set_mode(SIZE_FIELD)
SCREEN = pygame.Surface(SIZE_FIELD)
pygame.display.set_caption('Крестики нолики')
SCREEN.fill((255, 255, 255))

cells = [
    ['', '',''],
    ['', '',''],
    ['', '','']]
mainloop = True
game_over = False
while mainloop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop =False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if cells[pos[1] // 100][pos[0] // 100] == "":
                cells[pos[1] // 100][pos[0] // 100] = "x"
                x, y = random.randint(0, 2), random.randint(0, 2)
                while cells[x][y] != "":
                    x, y = random.randint(0, 2), random.randint(0, 2)
                cells[x][y] = "0"

            win_player= fun.game_result(cells, "x")
            win_ai = fun.game_result(cells, "0")
            if win_player or win_ai:
                game_over = True
                if win_player:
                    pygame.display.set_caption("Вы победили")
                else:
                    pygame.display.set_caption("Компьютер победил")
            elif cells[0].count("x") + cells[0].count("0") + cells[1].count("x") + \
                    cells[1].count("0") + cells[2].count("x") + cells[2].count("0") == 8:
                game_over = True
                pygame.display.set_caption("Ничья")
                    
    fun.cross_and_toe(SCREEN,cells)   
    fun.field_lines(SCREEN)
    WINDOW.blit(SCREEN, (0,0))
    pygame.display.update()