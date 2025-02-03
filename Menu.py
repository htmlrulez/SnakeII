import pygame
from Button import Button
from GameSettings import GameSettings
from ImageHandler import ImageHandlerII
from SinglePlayer import SinglePLayer
from MultiPlayer import MultiPlayer
from Settings import Settings
from HallOfFame import HallOfFame


class Menu:
    "Creates the game menu"

    def __init__(self):
        self.screen: pygame.Surface = pygame.display.set_mode(
            (GameSettings.TOTAL_GAME_WIDTH, GameSettings.TOTAL_GAME_HEIGHT)
        )
        self.menu_image_handler: ImageHandlerII = ImageHandlerII()

        self.single_player_button: Button = Button(
            GameSettings.MENU_SINGLE_PLAYER_BUTTON_X_POS,
            GameSettings.MENU_SINGLE_PLAYER_BUTTON_Y_POS,
            "Single Player",
        )
        self.multi_player_button = Button(
            GameSettings.MENU_MULIT_PLAYER_BUTTON_X_POS,
            GameSettings.MENU_MULIT_PLAYER_BUTTON_Y_POS,
            "Multi Player",
        )
        self.settings_button = Button(
            GameSettings.MENU_SETTINGS_BUTTON_X_POS,
            GameSettings.MENU_SETTINGS_BUTTON_Y_POS,
            "Settings",
        )
        self.exit_game_button = Button(
            GameSettings.MENU_SETTINGS_BUTTON_X_POS,
            GameSettings.MENU_EXIT_GAME_BUTTON_Y_POS,
            "Exit Game",
        )
        self.change_speed_button = Button(
            GameSettings.MENU_MULIT_PLAYER_BUTTON_X_POS,
            GameSettings.MENU_MULIT_PLAYER_BUTTON_Y_POS,
            "Change Speed",
        )
        self.high_score_button: Button = Button(
            GameSettings.MENU_SINGLE_PLAYER_BUTTON_X_POS,
            GameSettings.MENU_EXIT_GAME_BUTTON_Y_POS,
            "Hall Of Fame",
        )

    def select_menu_options(self):
        "Sets up the menu option bars"

        buttons: list[Button] = [
            self.single_player_button,
            self.multi_player_button,
            self.settings_button,
            self.exit_game_button,
            self.high_score_button,
        ]
        for button in buttons:
            button.menu_buttons(self.screen)
            pygame.display.flip()

    def start(self):
        "Starts the game menu"
        pygame.init()
        self.screen.blit(self.menu_image_handler.basic_background_path, (0, 100))
        base_speed: int = GameSettings.SNAKE_GAME_SPEED
        speed: int = base_speed
        pygame.display.flip()
        self.select_menu_options()

        menu_screen_running: bool = True
        while menu_screen_running:
            menu_event: pygame.event.Event = pygame.event.wait()
            mouse_pressed: tuple[bool, bool, bool] = pygame.mouse.get_pressed()
            if mouse_pressed == GameSettings.RIGHT_CLICK:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if self.settings_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.settings_button.rect.x + GameSettings.MENU_RECT_WIDTH,
                    GameSettings.MENU_RECT_HEIGHT,
                ):

                    settings: Settings = Settings(self.screen)
                    match settings.start():
                        case 25:
                            new_speed: int = 350
                            speed: int = new_speed
                        case 100:
                            new_speed: int = 100
                            speed: int = new_speed
                        case 200:
                            new_speed: int = 50
                            speed: int = new_speed
                        case _:
                            new_speed: int = 100
                            speed: int = new_speed

                    self.screen.blit(
                        self.menu_image_handler.basic_background_path, (0, 100)
                    )
                    self.select_menu_options()

                elif self.single_player_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.multi_player_button.rect.x - 5,
                    GameSettings.MENU_RECT_HEIGHT,
                ):
                    single_player: SinglePLayer = SinglePLayer(self.screen)
                    single_player.start(speed)
                    self.screen.fill("black")
                    self.screen.blit(
                        self.menu_image_handler.basic_background_path, (0, 100)
                    )
                    self.select_menu_options()

                elif self.multi_player_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.settings_button.rect.x - 10,
                    GameSettings.MENU_RECT_HEIGHT,
                ):
                    multi_player: MultiPlayer = MultiPlayer(self.screen)
                    multi_player.start(speed)

                    self.screen.fill("black")
                    self.screen.blit(
                        self.menu_image_handler.basic_background_path, (0, 100)
                    )
                    self.select_menu_options()

                elif self.high_score_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.high_score_button.rect.x + GameSettings.MENU_RECT_WIDTH,
                    GameSettings.TOTAL_GAME_HEIGHT,
                ):

                    hall_of_fame: HallOfFame = HallOfFame(self.screen)
                    hall_of_fame.start()
                    self.select_menu_options()

                elif self.exit_game_button.area_pressed(
                    mouse_x,
                    mouse_y,
                    self.exit_game_button.rect.x + GameSettings.MENU_RECT_WIDTH,
                    GameSettings.TOTAL_GAME_HEIGHT,
                ):
                    menu_screen_running: bool = False
                    pygame.quit()

                elif menu_event.type == pygame.QUIT:
                    menu_screen_running: bool = False
                    pygame.quit()
