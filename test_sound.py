import pygame

pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")
pygame.mixer.music.play()

input("Press Enter to stop...")