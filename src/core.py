import pygame
import time
import os
from itertools import cycle
from src import shared
from src import scenes
from src import utils

pygame.init()

class Core:
    def __init__(self):
        self.clock = pygame.Clock()

        self.scenes = [scenes.TitleScene(), scenes.Scene1(), scenes.Scene2(), scenes.Scene3()]

        self.scene_index = int(utils.read_save("save.txt"))

        shared.dt = 0
        shared.screen = pygame.display.set_mode((1600,900),  pygame.SCALED)

        self.cursor_current = next(shared.cursors)
        self.cursor_start = time.perf_counter()
        pygame.mouse.set_cursor(self.cursor_current)
        

    def get_events(self):
        shared.events = pygame.event.get()
        shared.mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        shared.mouse_press = pygame.mouse.get_pressed()
        shared.kp = pygame.key.get_just_pressed()


    def exit_game(self):
        for event in shared.events:
            if event.type == pygame.QUIT:
                raise (SystemExit)
    
    def animate_cursor(self):
        if time.perf_counter() - self.cursor_start >= 1:
            new_cursor = next(shared.cursors)
            if new_cursor != self.cursor_current:
                self.cursor_current = new_cursor
                pygame.mouse.set_cursor(self.cursor_current)
            self.cursor_start = time.perf_counter()
                    
    def update(self):
        self.scene_index = int(utils.read_save("save.txt"))
        self.scenes[self.scene_index].update()

    def print_mouse_pos(self):
        # print(shared.mouse_pos)
        pass

    def draw(self):
        shared.screen.fill("black")
        self.scenes[self.scene_index].draw()
        pygame.display.flip()

    def game_loop(self):    
        while True:
            self.get_events()
            self.exit_game()
            self.animate_cursor()
            self.print_mouse_pos()
            self.update()
            self.draw()


def main():
    core = Core()
    core.game_loop()
