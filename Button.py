import pygame
from GameSettings import GameSettings


class Button:
    "Creates a Botton object with a rect, and a text"

    def __init__(self, x: int, y: int, text: str):
        self.rect: pygame.Rect = pygame.Rect(
            x, y, GameSettings.MENU_RECT_WIDTH, GameSettings.MENU_RECT_HEIGHT
        )
        self.text: str = text

    def set_font_on_text(self):
        "Sets and renders the text with the given font"
        font_type: pygame.font.Font = pygame.font.SysFont("arialblack", 20)
        text_render: pygame.Surface = font_type.render(
            self.text, False, "Black", "Green"
        )
        return text_render

    def menu_buttons(self, screen: pygame.Surface):
        "Renders wide Botton rect witn green cube and black text"
        text: pygame.Surface = self.set_font_on_text()
        pygame.draw.rect(screen, "Green", self.rect)
        text_rect: pygame.Rect = self.make_text_rect(text)
        screen.blit(text, text_rect)

    def narrow_buttons(self, screen: pygame.Surface):
        "Renders narrow Botton rect"
        text_surface: pygame.Surface = self.set_font_on_text()
        self.rect.w = max(len(self.text), text_surface.get_width())
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))

    def area_pressed(
        self, mouse_x: int, mouse_y: int, rect2_x: int, rect2_y: int
    ) -> bool:
        "Detects if the generated Botton area is pressed"
        return (mouse_x >= self.rect.x and mouse_y >= self.rect.y) and (
            mouse_x <= rect2_x and mouse_y <= rect2_y
        )
    

    def make_text_rect(self, text: pygame.Surface) -> pygame.Rect:
        "Make the centered rect inside the Button for the text"
        return pygame.Rect(
            self.rect.x + (self.rect.width - text.get_width()) // 2,
            self.rect.y + (self.rect.height - text.get_height()) // 2,
            text.get_width(),
            text.get_height(),
        )
