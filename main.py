import pygame
import random


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[random.randint(0, 1) for _ in range(height)] for q in range(width)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def render(self, screen):
        colors = [pygame.Color("red"), pygame.Color("blue")]
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.circle(screen, colors[self.board[x][y]], (
                    x * self.cell_size + self.left * 1.5, y * self.cell_size + self.top * 1.5), self.cell_size // 2 - 2)
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # cell - кортеж (x, y)
    def on_click(self, cell):
        x, y = cell
        for i in range(self.width):
            self.board[i][y] = (self.board[i][y] + 1) % 2
        for i in range(self.height):
            # чтобы не перекрашивать дважды
            if i == y:
                continue
            self.board[x][i] = (self.board[x][i] + 1) % 2

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


def main():
    pygame.init()
    n = int(input())
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Чёрное в белое и наоборот')

    # поле n на n
    board = Board(n, n)
    board.set_view(50, 50, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
