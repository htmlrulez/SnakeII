import pygame
from ImageHandler import ImageHandlerII
from Button import Button
from GameSettings import GameSettings


class Settings:
    "Srarts up the settings tab, to set speed for the game"

    def __init__(self, screen: pygame.Surface) -> None:
        self.image_handler: ImageHandlerII = ImageHandlerII()
        self.screen: pygame.Surface = screen
        self.back_to_menu_button: Button = Button(
            GameSettings.MENU_EXIT_GAME_BUTTON_X_POS,
            GameSettings.MENU_EXIT_GAME_BUTTON_Y_POS,
            "Back to Menu",
        )

        self.quarter_speed_button: Button = Button(
            GameSettings.MENU_RECT_WIDTH, GameSettings.MENU_RECT_HEIGHT + 5, "25% Speed"
        )
        self.normal_speed_button: Button = Button(
            GameSettings.MENU_RECT_WIDTH * 2 + 5,
            GameSettings.MENU_RECT_HEIGHT + 5,
            "Normal Speed",
        )
        self.double_speed_button: Button = Button(
            GameSettings.MENU_RECT_WIDTH * 3 + 10,
            GameSettings.MENU_RECT_HEIGHT + 5,
            "200% Speed",
        )
        self.screen: pygame.Surface = screen
        self.image_handler: ImageHandlerII = ImageHandlerII()

    def start(self):
        "Settings mode to set up speed"
        self.screen.fill("white")
        self.screen.blit(self.image_handler.settings_background_path, (100, -50))
        self.select_settings_options()
        pygame.display.flip()

        settings_screen_running: bool = True
        while settings_screen_running:
            settings_event: pygame.event.Event = pygame.event.wait()
            mouse_pressed: tuple[bool, bool, bool] = pygame.mouse.get_pressed()
            if mouse_pressed == GameSettings.RIGHT_CLICK:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.quarter_speed_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.normal_speed_button.rect.x - 5,
                    GameSettings.MENU_RECT_HEIGHT + GameSettings.MENU_RECT_HEIGHT,
                ):
                    self.screen.fill("black")

                    return 25

                elif self.normal_speed_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.double_speed_button.rect.x - 10,
                    GameSettings.MENU_RECT_HEIGHT + GameSettings.MENU_RECT_HEIGHT,
                ):
                    self.screen.fill("black")

                    return 100

                elif self.double_speed_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.double_speed_button.rect.x + GameSettings.MENU_RECT_WIDTH,
                    GameSettings.MENU_RECT_HEIGHT + GameSettings.MENU_RECT_HEIGHT,
                ):
                    self.screen.fill("black")

                    return 200

                elif self.back_to_menu_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.back_to_menu_button.rect.x + GameSettings.MENU_RECT_WIDTH,
                    GameSettings.TOTAL_GAME_HEIGHT,
                ):
                    settings_screen_running = False
                    self.screen.fill("black")

                    return

            elif settings_event.type == pygame.QUIT:
                settings_screen_running: bool = False
                self.screen.fill("black")

                return

    def select_settings_options(self):
        "Select speed options in settings"
        buttons: list[Button] = [
            self.quarter_speed_button,
            self.normal_speed_button,
            self.double_speed_button,
            self.back_to_menu_button,
        ]
        for button in buttons:
            pygame.draw.rect(self.screen, "black", button.rect)
            button.menu_buttons(self.screen)
