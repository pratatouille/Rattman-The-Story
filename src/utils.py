import pygame
import time
import os
from itertools import cycle
from src import shared

class Button:
    def __init__(self, x, y, width, height, images):
        self.x = x
        self.y = y
        self.surf = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image_offhover = images[0]
        self.images_onhover = [images[1], images[2]]
        self.rect = self.surf.get_frect(center=(self.x, self.y))
        self.frames = cycle(self.images_onhover)
        self.start = time.perf_counter()
        self.frame = next(self.frames)
        self.hovering = False

    def animate(self):
        if time.perf_counter() - self.start >= 1:
            self.surf.fill(00000000)
            self.frame = next(self.frames)
            self.surf.blit(self.frame)
            self.start = time.perf_counter()

    def check_hover(self):
        if self.rect.collidepoint(shared.mouse_pos):
            self.hovering = True
        else:
            self.hovering = False
    
    def update(self):
        self.check_hover()
        if self.check_click():
            scene_index = read_save("save.txt")
            scene_index += 1
            overwrite_save("save.txt", scene_index)
        if self.hovering:
            self.animate()
        else: 
            self.surf.fill(00000000)
            self.surf.blit(self.image_offhover)

    def draw(self):
        shared.screen.blit(self.surf, self.rect)

    def check_click(self):
        for event in shared.events:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                return True
        return False


class Timer:
    def __init__(self, cooldown: float):
        self.cooldown = cooldown
        self.start = time.perf_counter()
    
    def tick(self):
        diff = time.perf_counter() - self.start

        if diff >= self.cooldown:
            self.start = time.perf_counter()
            return True
        return False
        

class TextBox:
    def __init__(self, dialogue, voice: pygame.Sound):
        self.dialogue = dialogue
        self.characters = iter(dialogue)
        self.voice = voice
        self.pos = pygame.Vector2(0, 700)
        self.size = (1600, 300)
        self.timer = Timer(0.05)
        self.text = ""
        self.done = False
        self.voice_index = 0
        

    def update(self):
        if shared.kp[pygame.K_SPACE]:
            self.text = self.dialogue
            self.done = True


        if self.timer.tick() and not self.done:
            self.voice_index += 1
            try:
                self.text += next(self.characters)
                if self.voice_index>=2 and self.text[-1].isalpha():
                    self.voice.play()
                    self.voice_index = 0
            except StopIteration:
                self.done = True
            
    def draw(self):
        pygame.draw.rect(shared.screen, "black", (self.pos, self.size))

        text_surf = shared.talking_font.render(self.text, True, "white", wraplength=self.size[0])
        shared.screen.blit(text_surf, (10, self.pos.y + 10))
        
            
def read_save(path):
    with open(path, "r") as f:
        return int(f.read().strip())

def overwrite_save(path, value):
    with open(path, "w") as f:
        f.write(str(value))
