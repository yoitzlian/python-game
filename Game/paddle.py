import pygame
BLACK = (0,0,0)

class Paddle(pygame.sprite.Sprite):
    #this class represents the Paddle

    def __init__(self, color, width, height):
        #Sprite constructor
        super().__init__()

        #Pass in the color of the paddle, its width and weight.
        #Set the background color
        self.image =pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        #The Paddle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #Dimension
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #checking if im not going too far
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
        #chekin if im not going too far
        if self.rect.y > 400:
            self.rect.y = 400