from Menu import Menu
import pygame
from HallOfFame import HallOfFame


def main():
    "Starts the game menu"
    pygame.init()
    menu: Menu = Menu()
    pygame.font.get_fonts()
    hall_of_fame: HallOfFame = HallOfFame(menu.screen)
    hall_of_fame.read_json()
    menu.start()


main()
