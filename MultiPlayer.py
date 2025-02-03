import pygame
from SnakeAndBait import SnakeII, Bait
from ImageHandler import ImageHandlerII
from Button import Button
from GameSettings import GameSettings
from Score import Score


class MultiPlayer:
    "MultiPlayer game mode"

    def __init__(
        self,
        screen: pygame.Surface,
    ) -> None:
        self.image_handler: ImageHandlerII = ImageHandlerII()
        self.screen: pygame.Surface = screen
        self.player_one_victory: Button = Button(
            GameSettings.TOTAL_GAME_WIDTH // 2 - 50,
            GameSettings.TOTAL_GAME_HEIGHT // 2 - 50,
            "Player One Won",
        )
        self.player_two_victory: Button = Button(
            GameSettings.TOTAL_GAME_WIDTH // 2 - 50,
            GameSettings.TOTAL_GAME_HEIGHT // 2 - 50,
            "Player Two Won",
        )
        self.snake_one: SnakeII = SnakeII(64 * 8, 64 * 8)
        self.snake_two: SnakeII = SnakeII(64 * 10, 64 * 15)
        self.bait: Bait = Bait(64 * 7, 64 * 8)
        self.player_one_score: Score = Score(self.snake_one, self.screen)
        self.player_two_score: Score = Score(self.snake_two, self.screen)

    def start(self, speed: int):
        "Starts multiplayer snake mode"

        turn1_pressed: int | None = None
        turn2_pressed: int | None = None

        pygame.time.set_timer(pygame.USEREVENT, speed)

        running: bool = True
        while running:
            event: pygame.event.Event = pygame.event.wait()
            if event.type == pygame.USEREVENT:
                if turn1_pressed is not None:
                    self.snake_one.turn(turn1_pressed)
                    turn1_pressed = None

                if turn2_pressed is not None:
                    self.snake_two.turn(turn2_pressed)
                    turn2_pressed = None

                self.snake_one.move()
                self.snake_two.move()
                self.snake_one.body_follow()
                self.snake_two.body_follow()
                self.multiplayer_render(
                    self.snake_one,
                    self.snake_two,
                    self.bait,
                    self.player_one_score,
                    self.player_two_score,
                )
                if self.snake_one.self_collision():
                    self.player_two_won_the_game()

                if self.snake_two.self_collision():
                    self.player_one_won_the_game()

                if self.multiplayer_snake_collision(self.snake_one, self.snake_two):
                    running = False
                    break

            if event.type == pygame.KEYDOWN:
                if event.key in (
                    pygame.K_DOWN,
                    pygame.K_UP,
                    pygame.K_LEFT,
                    pygame.K_RIGHT,
                ):
                    turn1_pressed = event.key

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_s, pygame.K_w, pygame.K_a, pygame.K_d):
                    turn2_pressed = event.key

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break

            if event.type == pygame.QUIT:
                running = False
                break

    def multiplayer_high_score_text(self, score: int):
        "Multi player score displayer"
        score_text: Button = Button(
            GameSettings.MULTI_PLAYER_SCORE_BOX, 0, "High Score: " + str(score)
        )
        score_text.narrow_buttons(self.screen)

    def multiplayer_snake_collision(self, snake_one: SnakeII, snake_two: SnakeII):
        "Checks for collisions in multiplayer snake mode"
        snake_one_head: pygame.Rect = snake_one.body[0].rect
        snake_two_head: pygame.Rect = snake_two.body[0].rect

        for snake_two_rect in snake_two.body:
            if snake_one_head.colliderect(snake_two_rect):
                self.player_two_won_the_game()

        for snake_one_rect in snake_one.body:
            if snake_two_head.colliderect(snake_one_rect):
                self.player_one_won_the_game()

    def multiplayer_food_collision(
        self, snake_one: SnakeII, snake_two: SnakeII, bait: Bait, screen: pygame.Surface
    ):
        "Checks collision between food and snake in multi player mode"
        if snake_one.body[0].rect.colliderect(bait.rect):
            bait.multiplayer_respawn(screen, snake_one)
            snake_one.grow()
        elif snake_two.body[0].rect.colliderect(bait.rect):
            bait.multiplayer_respawn(screen, snake_two)
            snake_two.grow()

    def player_one_won_the_game(self):
        "Annuncment of player 1 winning the game"
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.player_one_victory.narrow_buttons(self.screen)
        pygame.display.flip()

    def player_two_won_the_game(self):
        "Annuncment of player 2 winning the game"
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.player_two_victory.narrow_buttons(self.screen)
        pygame.display.flip()

    def multiplayer_render(
        self,
        snake_one: SnakeII,
        snake_two: SnakeII,
        bait: Bait,
        score_one: Score,
        score_two: Score,
    ):
        "Renders background, food respawn, snake, bait, score"
        self.screen.blit(self.image_handler.multiplayer_background_path, (0, 0))
        self.multiplayer_food_collision(snake_one, snake_two, bait, self.screen)
        snake_one.draw(self.screen)
        snake_two.draw_second_snake(self.screen)
        bait.draw_multiplayer_snake(self.screen)
        score_one.display()
        score_two.display_second_snake_score()
        pygame.display.flip()
