import pygame
import pygame_menu
from sys import exit
from Constants.constants import *


pygame.init()
class Main():
    def start_model(self):

        # Starts the window to screen
        self.main_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.menu = pygame_menu.Menu('Welcome', SCREEN_WIDTH, SCREEN_HEIGHT, theme = pygame_menu.themes.THEME_BLUE)

        self.menu.add.button("Exit" , pygame_menu.events.EXIT)



        self.menu.mainloop(self.main_surface)
        pygame.display.update()

    def run_model(self):
        pass
    def show_math(self):
        pass
main = Main()
main.start_model()