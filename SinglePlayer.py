import pygame
from SnakeAndBait import SnakeII, Bait
from ImageHandler import ImageHandlerII
from Button import Button
from GameSettings import GameSettings
from Score import Score


class SinglePLayer:
    "SinglePlayer game mode"

    def __init__(self, screen: pygame.Surface) -> None:
        self.image_handler: ImageHandlerII = ImageHandlerII()
        self.screen: pygame.Surface = screen
        self.single_player_loose: Button = Button(
            GameSettings.TOTAL_GAME_WIDTH // 2 - 50,
            GameSettings.TOTAL_GAME_HEIGHT // 2 - 50,
            "Self Collision Detected",
        )
        self.bait: Bait = Bait(64 * 7, 64 * 8)
        self.snake: SnakeII = SnakeII(64 * 8, 64 * 8)
        self.score: Score = Score(self.snake, self.screen)

    def start(self, speed: int):
        "Starts single player snake mode"
        turn_pressed: int | None = None
        pygame.time.set_timer(pygame.USEREVENT, speed)
        running: bool = True
        while running:
            event: pygame.event.Event = pygame.event.wait()
            if event.type == pygame.USEREVENT:
                if turn_pressed is not None:
                    self.snake.turn(turn_pressed)
                    turn_pressed: None | int = None
                self.snake.move()
                self.snake.body_follow()
                self.singleplayer_render(self.snake, self.bait, self.score)
                if self.snake.self_collision():
                    self.single_player_lost_the_game()
                    self.score.write_json()
                    return

            if event.type == pygame.KEYDOWN:
                if event.key in (
                    pygame.K_DOWN,
                    pygame.K_UP,
                    pygame.K_LEFT,
                    pygame.K_RIGHT,
                ):
                    turn_pressed = event.key

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

            if event.type == pygame.QUIT:
                running = False
                break

    def singleplayer_render(self, snake: SnakeII, bait: Bait, score: Score):
        "Renders snake, bait, score for single player"
        self.screen.blit(self.image_handler.single_player_background_path, (0, 0))
        self.food_collision(snake, bait, self.screen)
        score.display()
        snake.draw(self.screen)
        bait.draw(self.screen)
        pygame.display.flip()

    def single_player_lost_the_game(self):
        "Annuncment of player loosing in single game"
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.single_player_loose.narrow_buttons(self.screen)
        pygame.display.flip()

    def food_collision(self, snake: SnakeII, bait: Bait, screen: pygame.Surface):
        "Checks collision between food and snake"
        if snake.body[0].rect.colliderect(bait.rect):
            bait.respawn(screen, snake)
            snake.grow()
