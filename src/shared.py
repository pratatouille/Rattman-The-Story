import pygame
import assets
from itertools import cycle

pygame.init()

screen: pygame.Surface


dt: float
events: list[pygame.event.Event]
kp: pygame.key.ScancodeWrapper
mouse_pos: pygame.Vector2
mouse_press: list[pygame.event.Event]

cursor1 = pygame.cursors.Cursor((0, 0), pygame.image.load("assets/cursor1.png"))
cursor2 = pygame.cursors.Cursor((0, 0), pygame.image.load("assets/cursor2.png"))
cursors = cycle([cursor1, cursor2])
cursor_start = 0

title_img1 = pygame.image.load("assets/titlescreen1.png")
title_img2 = pygame.image.load("assets/titlescreen2.png")

start_button_images = [pygame.image.load("assets/start_button1.png"), pygame.image.load("assets/start_button2.png"), pygame.image.load("assets/start_button3.png")]

arrow_right_images = [pygame.image.load("assets/arrow_right1.png"), pygame.image.load("assets/arrow_right2.png"), pygame.image.load("assets/arrow_right3.png")]

glados_font = pygame.font.Font("assets/Courier-Prime-Code.ttf", 15)
talking_font = pygame.font.Font("assets/Lato-Regular.ttf", 30)

sans_voice = pygame.mixer.Sound("assets/sansvoice.mp3")
computer_voice = pygame.mixer.Sound("assets/computervoice.mp3")
computer_voice.set_volume(0.7)
henrys_voice = pygame.mixer.Sound("assets/henrysvoice.mp3")
rattmans_voice = pygame.mixer.Sound("assets/rattmansvoice.mp3")