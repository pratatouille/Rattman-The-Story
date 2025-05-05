import pygame
from src.utils import *
import time
from itertools import cycle

class TitleScene:
    def __init__(self):

        self.titles = cycle([shared.title_img1, shared.title_img2])
        self.title_current = next(self.titles)
        self.title_start = time.perf_counter()

        self.start_button = Button(1200, 450, 256, 256, shared.start_button_images);

    def animate_title(self):
        if time.perf_counter() - self.title_start >= 0.8:
            new_title = next(self.titles)
            if new_title != self.title_current:
                self.title_current = new_title
            self.title_start = time.perf_counter()

    def draw(self):
        shared.screen.blit(self.title_current)
        self.start_button.draw()

    def update(self):
        self.animate_title()
        self.start_button.update()


class Scene1:
    def __init__(self):
        self.dialogues: list[TextBox] = iter([
            TextBox("GlaDOS: a supercomputer based on quantum computing. Originally developed to \"Store Caroline into a computer\". \n(Click on the Core for more info.)", shared.computer_voice),
            TextBox("Wheatley: the Morality Core for behavorial control over GLaDOS.", shared.computer_voice)
        ])

        # self.dialogues_list = [
        #     TextBox("GlaDOS: a supercomputer based on quantum computing. Originally developed to \"Store Caroline into a computer\". \n(Click on the Core for more info.)", shared.computer_voice),
        #     TextBox("Wheatley: the Morality Core for behavorial control over GLaDOS.", shared.computer_voice)
        # ]

        self.glados_head_surf = pygame.Surface((100,200), pygame.SRCALPHA)
        self.glados_head_rect = self.glados_head_surf.get_frect(center=(845,160))
        self.glados_hovering = False

        self.wheatley_head_surf = pygame.Surface((220,320), pygame.SRCALPHA)
        self.wheatley_head_rect = self.wheatley_head_surf.get_frect(center=(1075, 295))
        self.wheatley_hovering = False

        self.current_dialogue = next(self.dialogues)
        self.computer_screen = pygame.image.load("assets/Scene1.png")
        self.done = False

        self.next_scene_button = Button(1439, 422, 256, 256, shared.arrow_right_images)

    # def check_hover(self):
    #     if self.glados_head_rect.collidepoint(shared.mouse_pos):
    #         self.dialogues_list[1].draw()
    #     if self.wheatley_head_rect.collidepoint(shared.mouse_pos):
    #         self.dialogues_list[1].draw()

    def update(self):
        if shared.kp[pygame.K_SPACE] and self.current_dialogue.done and not self.done:
            try:
                self.current_dialogue = next(self.dialogues)
                return
            except StopIteration:
                self.done = True
        
        # self.check_hover()
        self.next_scene_button.update()
        self.current_dialogue.update()

    def draw(self):
        shared.screen.blit(self.computer_screen)
        self.current_dialogue.draw()
        self.next_scene_button.draw()


class Scene2:
    def __init__(self):
        self.dialogues: list[TextBox] = iter([
            TextBox("Rattman: I really don't have a good feeling about her, Henry.", shared.rattmans_voice),
            TextBox("Henry: Hey, it's fine. We finally succeeded into making a morality core, and we all worked really hard on this. It's for the legacy of Cave Johnson.", shared.henrys_voice),
            TextBox("Rattman: I guess so. Maybe I'm just being paranoid.", shared.rattmans_voice),
            TextBox("Henry: ...in true you fashion. You are.", shared.henrys_voice)
        ])
        self.current_dialogue = next(self.dialogues)
        self.characters_background = pygame.image.load("assets/henryandrattman.png")
        self.next_scene_button = Button(1439, 422, 256, 256, shared.arrow_right_images)
        self.done = False
        self.next_scene_button = Button(1439, 422, 256, 256, shared.arrow_right_images)

    def update(self):
        if shared.kp[pygame.K_SPACE] and self.current_dialogue.done and not self.done:
            try:
                self.current_dialogue = next(self.dialogues)
                return
            except StopIteration:
                self.done = True
        self.next_scene_button.update()
        self.current_dialogue.update() 

    def draw(self):
        shared.screen.blit(self.characters_background)
        self.current_dialogue.draw()
        self.next_scene_button.draw()

class Scene3:
    def __init__(self):
        self.funny_background = pygame.image.load("assets/funnyending.png")
        self.workinprogress_img = pygame.image.load("assets/workinprogress.png")
        self.workinprogress_img.set_alpha(220)

    def update(self):
        pass

    def draw(self):
        shared.screen.blit(self.funny_background) 
        shared.screen.blit(self.workinprogress_img)


