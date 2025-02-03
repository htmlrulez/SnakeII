import pygame
from pathlib import Path


class ImageHandlerII:
    """Handles the images for the game"""

    def __init__(self):

        self.snake_image_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "singleplayersnake.png"
        )
        self.multiplayer_snake_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "multiplayersnake.png"
        )
        self.single_player_background_picture_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "snake-gamebackground.jpg"
        )
        self.basic_background_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "snake-gamebackground.jpg"
        )
        self.single_player_background_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent
            / "Docs"
            / "single_player_correct_3_test.jpg"
        )
        self.multiplayer_background_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "multiplayer_correct_1_test.jpg"
        )
        self.settings_background_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "settings_background_image.jpg"
        )

        self.hall_of_fame_background_path: pygame.Surface  = pygame.image.load(
            Path(__file__).resolve().parent / "Docs" / "hsbgcopyy.png"
        )

        self.head_right: pygame.Rect = pygame.Rect(256, 0, 64, 64)
        self.head_left: pygame.Rect = pygame.Rect(192, 64, 64, 64)
        self.head_up: pygame.Rect = pygame.Rect(192, 0, 64, 64)
        self.head_down: pygame.Rect = pygame.Rect(256, 64, 64, 64)
        self.tail_right: pygame.Rect = pygame.Rect(256, 128, 64, 64)
        self.tail_left: pygame.Rect = pygame.Rect(192, 192, 64, 64)
        self.tail_up: pygame.Rect = pygame.Rect(192, 128, 64, 64)
        self.tail_down: pygame.Rect = pygame.Rect(256, 192, 64, 64)
        self.body_horizontal: pygame.Rect = pygame.Rect(64, 0, 64, 64)
        self.body_vertical: pygame.Rect = pygame.Rect(128, 64, 64, 64)
        self.top_left_turning_position: pygame.Rect = pygame.Rect(0, 0, 64, 64)
        self.bottom_left_turning_position: pygame.Rect = pygame.Rect(0, 64, 64, 64)
        self.bottom_right_turning_position: pygame.Rect = pygame.Rect(128, 128, 64, 64)
        self.top_right_turning_position: pygame.Rect = pygame.Rect(128, 0, 64, 64)
        self.bait: pygame.Rect = pygame.Rect(0, 194, 64, 64)

    def set_correct_image(
        self, image: pygame.Surface, snake_pos_on_image: pygame.Rect
    ) -> pygame.Surface:
        """Sets the correct image for the Snake body"""
        picture = image
        handler_surface = picture.copy()
        snake_turn = snake_pos_on_image
        handler_surface.set_clip(snake_turn)
        image = picture.subsurface(handler_surface.get_clip())
        return image
