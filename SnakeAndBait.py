import random
import pygame
from SnakeBody import SnakeBody
from GameSettings import GameSettings
from ImageHandler import ImageHandlerII


class SnakeII:
    "Manages the snake body"

    def __init__(self, x: int, y: int):

        self.body: list[SnakeBody] = [
            SnakeBody(x, y),
            SnakeBody(x - GameSettings.SNAKE_WIDTH, y),
        ]
        self.image_handler: ImageHandlerII = ImageHandlerII()
        self.score: int = 1

    def draw(self, screen: pygame.Surface) -> None:
        "Draws out the body of the snake"
        for index, body_part in enumerate(self.body):
            if index == 0:
                self.head_logic(screen)

            elif index == len(self.body) - 1:
                self.tail_logic(screen)

            else:
                self.body_logic(screen, index)

    def head_logic(self, screen: pygame.Surface) -> None:
        "Draws the correct image for the head"
        for index, object_iterable in enumerate(self.body[:1]):
            if index == 0 and object_iterable.x_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.head_right,
                    ),
                    object_iterable.rect,
                )

            elif index == 0 and object_iterable.x_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.head_left,
                    ),
                    object_iterable.rect,
                )

            elif index == 0 and object_iterable.y_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path, self.image_handler.head_up
                    ),
                    object_iterable.rect,
                )

            elif index == 0 and object_iterable.y_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.head_down,
                    ),
                    object_iterable.rect,
                )

    def tail_logic(self, screen: pygame.Surface) -> None:
        "Draws the correct image for the tail"
        for _, object_iterable in enumerate(self.body[-1:]):
            if self.body[-1] and object_iterable.x_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.tail_right,
                    ),
                    object_iterable.rect,
                )

            elif self.body[-1] and object_iterable.x_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.tail_left,
                    ),
                    object_iterable.rect,
                )

            elif self.body[-1] and object_iterable.y_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path, self.image_handler.tail_up
                    ),
                    object_iterable.rect,
                )

            elif len(self.body) >= 2 and object_iterable.y_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.tail_down,
                    ),
                    object_iterable.rect,
                )

    def body_logic(self, screen: pygame.Surface, index: int):
        "Draws the correct image for the body"
        prevx: int = self.body[index + 1].rect.x
        nextx: int = self.body[index - 1].rect.x
        prevy: int = self.body[index + 1].rect.y
        nexty: int = self.body[index - 1].rect.y
        prev_block_x_speed: int = self.body[index + 1].x_speed
        prev_block_yspeed: int = self.body[index + 1].y_speed

        body_part: SnakeBody = self.body[index]

        if prevx == nextx:
            screen.blit(
                self.image_handler.set_correct_image(
                    self.image_handler.snake_image_path,
                    self.image_handler.body_vertical,
                ),
                body_part.rect,
            )
        elif prevy == nexty:
            screen.blit(
                self.image_handler.set_correct_image(
                    self.image_handler.snake_image_path,
                    self.image_handler.body_horizontal,
                ),
                body_part.rect,
            )
        else:
            if (body_part.y_speed > 0 and prev_block_x_speed < 0) or (
                body_part.x_speed > 0 and prev_block_yspeed < 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.top_left_turning_position,
                    ),
                    body_part.rect,
                )
            elif (body_part.y_speed > 0 and prev_block_x_speed > 0) or (
                body_part.x_speed < 0 and prev_block_yspeed < 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.top_right_turning_position,
                    ),
                    body_part.rect,
                )
            elif (body_part.x_speed > 0 and prev_block_yspeed > 0) or (
                body_part.y_speed < 0 and prev_block_x_speed < 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.bottom_left_turning_position,
                    ),
                    body_part.rect,
                )
            elif (body_part.x_speed < 0 and prev_block_yspeed > 0) or (
                body_part.y_speed < 0 and prev_block_x_speed > 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.snake_image_path,
                        self.image_handler.bottom_right_turning_position,
                    ),
                    body_part.rect,
                )

    def draw_second_snake(self, screen: pygame.Surface) -> None:
        "Draws snake for multi player mode"
        for index, object_iterable in enumerate(self.body):
            if index == 0:
                self.second_snake_head_logic(screen)
            elif index == len(self.body) - 1:
                self.second_snake_tail_logic(screen)
            else:
                self.second_snake_body_logic(screen, index)
                


    def second_snake_head_logic(self, screen: pygame.Surface) -> None:
        "Draws the correct image for the second snake head"
        for index, object_iterable in enumerate(self.body[:1]):
            if index == 0 and object_iterable.x_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.head_right,
                    ),
                    object_iterable.rect,
                )

            elif index == 0 and object_iterable.x_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.head_left,
                    ),
                    object_iterable.rect,
                )

            elif index == 0 and object_iterable.y_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.head_up,
                    ),
                    object_iterable.rect,
                )

            elif index == 0 and object_iterable.y_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.head_down,
                    ),
                    object_iterable.rect,
                )

    def second_snake_tail_logic(self, screen: pygame.Surface) -> None:
        "Draws the correct image for the tail"
        for _, object_iterable in enumerate(self.body[-1:]):
            if len(self.body) >= 2 and object_iterable.x_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.tail_right,
                    ),
                    object_iterable.rect,
                )

            elif len(self.body) >= 2 and object_iterable.x_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.tail_left,
                    ),
                    object_iterable.rect,
                )

            elif len(self.body) >= 2 and object_iterable.y_speed < 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.tail_up,
                    ),
                    object_iterable.rect,
                )

            elif len(self.body) >= 2 and object_iterable.y_speed > 0:
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.tail_down,
                    ),
                    object_iterable.rect,
                )





    def second_snake_body_logic(self, screen: pygame.Surface, index: int):
        prevx: int = self.body[index + 1].rect.x
        nextx: int = self.body[index - 1].rect.x
        prevy: int = self.body[index + 1].rect.y
        nexty: int = self.body[index - 1].rect.y
        prev_block_x_speed: int = self.body[index + 1].x_speed
        prev_block_y_speed: int = self.body[index + 1].y_speed

        body_part: SnakeBody = self.body[index]

        if prevx == nextx:
            screen.blit(
                self.image_handler.set_correct_image(
                    self.image_handler.multiplayer_snake_path,
                    self.image_handler.body_vertical,
                ),
                body_part.rect,
            )

        elif prevy == nexty:
            screen.blit(
                self.image_handler.set_correct_image(
                    self.image_handler.multiplayer_snake_path,
                    self.image_handler.body_horizontal,
                ),
                body_part.rect,
            )

        else:
            if (body_part.y_speed > 0 and prev_block_x_speed < 0) or (
                body_part.x_speed > 0 and prev_block_y_speed < 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.top_left_turning_position,
                    ),
                    body_part.rect,
                )

            elif (body_part.y_speed > 0 and prev_block_x_speed > 0) or (
                body_part.x_speed < 0 and prev_block_y_speed < 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.top_right_turning_position,
                    ),
                    body_part.rect,
                )

            elif (body_part.x_speed > 0 and prev_block_y_speed > 0) or (
                body_part.y_speed < 0 and prev_block_x_speed < 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.bottom_left_turning_position,
                    ),
                    body_part.rect,
                )

            elif (body_part.x_speed < 0 and prev_block_y_speed > 0) or (
                body_part.y_speed < 0 and prev_block_x_speed > 0
            ):
                screen.blit(
                    self.image_handler.set_correct_image(
                        self.image_handler.multiplayer_snake_path,
                        self.image_handler.bottom_right_turning_position,
                    ),
                    body_part.rect,
                )

    def move(self):
        "Moves the snake"
        for body in self.body:
            body.move()

    def turn(self, key: int) -> None:
        "Turn the body of the snake"
        if key in (pygame.K_DOWN, pygame.K_s):
            if self.body[0].y_speed < 0:
                self.turn_up()
            else:
                self.turn_down()

        elif key in (pygame.K_UP, pygame.K_w):
            if self.body[0].y_speed > 0:
                self.turn_down()
            else:
                self.turn_up()

        elif key in (pygame.K_LEFT, pygame.K_a):
            if self.body[0].x_speed > 0:
                self.turn_right()
            else:
                self.turn_left()

        elif key in (pygame.K_RIGHT, pygame.K_d):
            if self.body[0].x_speed < 0:
                self.turn_left()
            else:
                self.turn_right()

    def turn_up(self):
        "Turns the snake body up"
        self.body[0].turn_up()

    def turn_down(self):
        "Turns the snake body down"
        self.body[0].turn_down()

    def turn_right(self):
        "Turns the snake body right"
        self.body[0].turn_right()

    def turn_left(self):
        "Turns the snake body left"
        self.body[0].turn_left()

    def grow(self):
        "Adds +1 score to the snake score and grows the snake by 1 block"
        self.score += 1
        tail: SnakeBody = self.body[-1]
        if tail.x_speed > 0:
            snake_part = SnakeBody(tail.rect.x - GameSettings.SNAKE_WIDTH, tail.rect.y)
            snake_part.x_speed = GameSettings.SNAKE_SPEED
            snake_part.y_speed = 0
            self.body.append(snake_part)

        elif tail.x_speed < 0:
            snake_part = SnakeBody(tail.rect.x + GameSettings.SNAKE_WIDTH, tail.rect.y)
            snake_part.x_speed = -GameSettings.SNAKE_SPEED
            snake_part.y_speed = 0
            self.body.append(snake_part)

        elif tail.y_speed > 0:
            snake_part = SnakeBody(tail.rect.x, tail.rect.y - GameSettings.SNAKE_HEIGHT)
            snake_part.x_speed = 0
            snake_part.y_speed = GameSettings.SNAKE_SPEED
            self.body.append(snake_part)

        elif tail.y_speed < 0:
            snake_part = SnakeBody(tail.rect.x, tail.rect.y + GameSettings.SNAKE_HEIGHT)
            snake_part.x_speed = 0
            snake_part.y_speed = -GameSettings.SNAKE_SPEED
            self.body.append(snake_part)

    def body_follow(self):
        "Makes the snake parts follow the previous one"
        for i in range(len(self.body) - 1, 0, -1):
            next_item = i - 1

            self.body[i].x_speed = self.body[next_item].x_speed
            self.body[i].y_speed = self.body[next_item].y_speed

    def self_collision(self) -> bool:
        "Checks for snake self collisions"
        for i in self.body[1:]:
            head = self.body[0].rect
            if head.colliderect(i.rect):
                return True


class Bait:
    "Creates a Bait object for the game"

    def __init__(self, x: int, y: int):
        self.rect: pygame.Rect = pygame.Rect(
            x, y, GameSettings.BAIT_WIDTH, GameSettings.BAIT_HEIGHT
        )
        self.image: ImageHandlerII = ImageHandlerII()

    def respawn(self, screen: pygame.Surface, snake: SnakeII):
        "Respawns and renders the Bait and checks for the Snake body to avoid collision in single player game mode"
        self.rect.x = (
            random.randrange(
                0, (GameSettings.TOTAL_GAME_WIDTH // GameSettings.BAIT_WIDTH)
            )
            * GameSettings.BAIT_WIDTH
        )
        self.rect.y = (
            random.randrange(
                0, (GameSettings.TOTAL_GAME_HEIGHT // GameSettings.BAIT_HEIGHT)
            )
            * GameSettings.BAIT_HEIGHT
        )

        for _ in snake.body:
            self.collision_with_snake(snake)
        screen.blit(
            self.image.set_correct_image(self.image.snake_image_path, self.image.bait),
            self.rect,
        )

    def multiplayer_respawn(self, screen: pygame.Surface, snake: SnakeII):
        "Respawns and renders the Bait and checks for the Snake body to avoid collision in multiplayer game mode"
        self.rect.x = (
            random.randrange(
                0, (GameSettings.TOTAL_GAME_WIDTH // GameSettings.BAIT_WIDTH)
            )
            * GameSettings.BAIT_WIDTH
        )
        self.rect.y = (
            random.randrange(
                0, (GameSettings.TOTAL_GAME_HEIGHT // GameSettings.BAIT_HEIGHT)
            )
            * GameSettings.BAIT_HEIGHT
        )

        for _ in snake.body:
            self.collision_with_snake(snake)
        screen.blit(
            self.image.set_correct_image(
                self.image.multiplayer_snake_path, self.image.bait
            ),
            self.rect,
        )

    def draw_multiplayer_snake_bait(self, screen: pygame.Surface):
        "Draws bait image in multiplayer mode"
        screen.blit(
            self.image.set_correct_image(
                self.image.multiplayer_snake_path, self.image.bait
            ),
            self.rect,
        )

    def draw(self, screen: pygame.Surface):
        "Draws bait in single player mode"
        screen.blit(
            self.image.set_correct_image(self.image.snake_image_path, self.image.bait),
            (self.rect.x, self.rect.y),
        )

    def draw_multiplayer_snake(self, screen: pygame.Surface):
        "Draws bait image in multiplayer mode"
        screen.blit(
            self.image.set_correct_image(
                self.image.multiplayer_snake_path, self.image.bait
            ),
            (self.rect.x, self.rect.y),
        )

    def collision_with_snake(self, snake: SnakeII):
        "Checks for collisions between snakes in multiplayer mode"
        apple: pygame.Rect = self.rect
        for snake_rect in snake.body:
            if apple.colliderect(snake_rect.rect):
                self.rect.x = (
                    random.randrange(
                        0, (GameSettings.TOTAL_GAME_WIDTH // GameSettings.BAIT_WIDTH)
                    )
                    * GameSettings.BAIT_WIDTH
                )
                self.rect.y = (
                    random.randrange(
                        0, (GameSettings.TOTAL_GAME_HEIGHT // GameSettings.BAIT_HEIGHT)
                    )
                    * GameSettings.BAIT_HEIGHT
                )
