import pygame
from GameSettings import GameSettings


class SnakeBody:
    "Handles the body of the Snake"

    def __init__(self, x: int, y: int):
        self.image: None | pygame.Surface = None
        self.rect: pygame.Rect = pygame.Rect(
            x, y, GameSettings.SNAKE_WIDTH, GameSettings.SNAKE_HEIGHT
        )
        self.x_speed: int = GameSettings.SNAKE_SPEED
        self.y_speed: int = 0

    def move(self):
        "Moves the body with x or y speed"
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x >= GameSettings.TOTAL_GAME_WIDTH:
            self.rect.x = 0

        elif self.rect.y >= GameSettings.TOTAL_GAME_HEIGHT:
            self.rect.y = 0

        elif self.rect.x <= -GameSettings.SNAKE_WIDTH:
            self.rect.x = GameSettings.TOTAL_GAME_WIDTH - self.rect.width

        elif self.rect.y <= -GameSettings.SNAKE_HEIGHT:
            self.rect.y = GameSettings.TOTAL_GAME_HEIGHT - self.rect.height

    def turn_up(self):
        "Turn the snake up"
        self.x_speed: int = 0
        self.y_speed: int = -GameSettings.SNAKE_SPEED

    def turn_down(self):
        "Turn the snake down"
        self.x_speed: int = 0
        self.y_speed: int = GameSettings.SNAKE_SPEED

    def turn_right(self):
        "Turn the snake right"
        self.x_speed: int = GameSettings.SNAKE_SPEED
        self.y_speed: int = 0

    def turn_left(self):
        "Turn the snake left"
        self.x_speed: int = -GameSettings.SNAKE_SPEED
        self.y_speed: int = 0
