from pathlib import Path
import json
import pygame
from SnakeAndBait import SnakeII
from ImageHandler import ImageHandlerII
from Button import Button
from GameSettings import GameSettings


class Score:
    "Manages the dynamic name input along with current score upon death"

    def __init__(self, snake: SnakeII, screen: pygame.Surface) -> None:
        self.name: str = ""
        self.snake: SnakeII = snake
        self.name_input_rect: pygame.Rect = pygame.Rect(GameSettings.NAME_INPUT_RECT)
        self.color: pygame.Color = pygame.Color("Red")
        self.font_size_for_score_box: pygame.font.Font = pygame.font.Font(None, 32)
        self.high_score_database_path: Path = (
            Path(__file__).resolve().parent / "Docs" / "snake_High_Score.json"
        )
        self.screen: pygame.Surface = screen
        self.image_handler: ImageHandlerII = ImageHandlerII()
        self.instructions: str = (
            "Type your name in the box. Hit 'Enter' to save highscore and continue."
        )
        self.name_input_instruction_rect: pygame.Rect = pygame.Rect(300, 200, 180, 69)

    def get_name(self):
        "Gets name from the user"
        name_typing = True
        while name_typing is True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.name = self.name[0:-1]
                    elif event.key == pygame.K_RETURN:
                        return
                    else:
                        self.name += event.unicode
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.dynamic_name_input_rect()
            self.instruction_for_name_input()
            pygame.display.flip()

    def read_json(self):
        "reads the score from json.file"
        with open(self.high_score_database_path, "+r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    def write_json(self):
        "writes the score to json.file"
        all_dict = self.read_json()
        self.get_name()
        new_d: dict[str, int] = {self.name: self.snake.score}
        all_dict.update(new_d)
        sorted_dict_to_write: dict[str, int] = dict(
            sorted(all_dict.items(), key=lambda value: value[1], reverse=True)
        )

        if len(sorted_dict_to_write) > 5:
            sorted_dict_to_write.popitem()
            with open(self.high_score_database_path, "w", encoding="utf-8") as f:
                json.dump(sorted_dict_to_write, f)
        else:
            with open(self.high_score_database_path, "w", encoding="utf-8") as f:
                json.dump(sorted_dict_to_write, f)

    def display(self):
        "Single player score displayer"
        score_text: Button = Button(0, 0, "Highscore: " + str(self.snake.score))
        score_text.narrow_buttons(self.screen)

    def display_second_snake_score(self):
        "Single player score displayer"
        gap: int = 60
        score_text: Button = Button(
            GameSettings.MULTI_PLAYER_SCORE_BOX - gap,
            0,
            "Highscore: " + str(self.snake.score),
        )
        score_text.narrow_buttons(self.screen)

    def instruction_for_name_input(self):
        "Instructions for name input"
        padding = 50
        font = pygame.font.SysFont("palatino-semi-bold", 50)
        text_surface: pygame.Surface = font.render(
            self.instructions, False, "Black", "Green"
        )

        rect = pygame.Rect(
            (GameSettings.TOTAL_GAME_WIDTH - text_surface.get_width()) // 2,
            self.name_input_rect.y - text_surface.get_height() - padding,
            text_surface.get_width(),
            text_surface.get_height(),
        )
        self.screen.blit(text_surface, rect)

    def dynamic_name_input_rect(self):
        "creates a dynamically growing rect on the screen for name input"
        self.screen.blit(self.image_handler.single_player_background_path, (0, 0))

        padding: int = 5
        total_empty_space: int = 2
        text_surface = self.font_size_for_score_box.render(self.name, True, "black")
        self.name_input_rect.w = max(
            GameSettings.NAME_INPUT_RECT.width,
            text_surface.get_width() + total_empty_space * padding,
        )
        self.name_input_rect.h = max(
            GameSettings.NAME_INPUT_RECT.height,
            text_surface.get_height() + total_empty_space * padding,
        )

        pygame.draw.rect(self.screen, "white", self.name_input_rect)
        pygame.draw.rect(self.screen, self.color, self.name_input_rect, 3)

        self.screen.blit(
            text_surface,
            (self.name_input_rect.x + padding, self.name_input_rect.y + padding),
        )
