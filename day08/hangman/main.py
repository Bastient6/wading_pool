import pygame

def draw_stickman(window):
    pygame.draw.circle(window, (255, 0, 0), [300, 100], 50, 3)
    pygame.draw.line(window,  (255, 0, 0), [300, 150],  [300, 300], 3)
    pygame.draw.line(window,  (255, 0, 0), [200, 200],  [400, 200], 3)
    pygame.draw.line(window,  (255, 0, 0), [300, 300],  [250, 400], 3)
    pygame.draw.line(window,  (255, 0, 0), [300, 300],  [350, 400], 3)




def main():
    status = 0
    pygame.init()
    background = pygame.image.load("./hangman/asset/Space-Background-Images.jpg")
    window = pygame.display.set_mode((600,600))
    background = pygame.transform.scale(background, (600, 600))
    while status != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = 1
        window.blit(background, (0, 0))
        draw_stickman(window)
        pygame.display.update()

    pygame.quit()

main()