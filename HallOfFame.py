import json
from pathlib import Path
import pygame
from Button import Button
from GameSettings import GameSettings
from ImageHandler import ImageHandlerII


class HallOfFame:
    "Starts highscores in game"

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen = screen
        self.high_score_database_path = (
            Path(__file__).resolve().parent / "Docs" / "snake_High_Score.json"
        )
        self.font_size = 32
        self.font: pygame.font.Font = pygame.font.Font(None, self.font_size)
        self.image_handler: ImageHandlerII = ImageHandlerII()

    def start(self):
        "Hall Of Fame for the Best player scores"
        self.screen.fill("black")
        self.screen.blit(self.image_handler.hall_of_fame_background_path, (0, 100))
        data = self.read_json()

        gap: int = 100
        i: int = 0
        for key, value in data.items():
            self.create_fame(
                GameSettings.HALL_OF_FAME_FIRST_POS_X,
                GameSettings.HALL_OF_FAME_FIRTS_POS_Y + (self.font_size + gap) * i,
                key,
                value,
            )
            i += 1
        pygame.display.flip()

    def read_json(self):
        "Reads from the database"
        empty_dict = {}
        try:
            with open(self.high_score_database_path, "+r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except OSError:
            with open(self.high_score_database_path, "w", encoding="utf-8") as f:
                json.dump(empty_dict, f)

    def create_fame(self, x_pos: int, y_pos: int, name: str, score: str):
        "displays the highscore"
        score = str(score)
        scored_name: str = name + ": " + score + " points"
        fame_name_plate = Button(x_pos, y_pos, scored_name)
        fame_name_plate.narrow_buttons(self.screen)
