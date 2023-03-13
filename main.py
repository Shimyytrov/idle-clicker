# import
import time
import sys
import pygame
import json

data = {
    "point": 0,
    "level": 1
}
with open('data.json', 'r') as data_json:
    data = json.load(data_json)

# config
pygame.init()
pygame.display.set_caption("Idle Clicker")
fps = 50
fps_clock = pygame.time.Clock()

font = pygame.font.Font('./assets/fonts/mindustry.ttf', 48)
def font_mindustry(fontsize):
    return pygame.font.Font('./assets/fonts/mindustry.ttf', int(128/fontsize))


swap = pygame.mixer.Sound('./assets/sounds/swap.wav')

running = True
point = 0



while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT: # quit
            pygame.quit()
            sys.exit()
    time.sleep(0.01)
    swap.play()
    point += 1
    print(point)

    fps_clock.tick(fps)