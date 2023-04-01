import numpy as np
import pygame

SPEED, PIXGAP = 0.2, 40
COLOR0, COLOR1, COLOR2 = (1,10,20), (75, 27, 28), (186, 74, 59)
OFFSET = np.array([40]*2)
pygame.font.init()
FONT = pygame.font.Font('Roboto-Bold.ttf', 300)


class Number:
    Center = np.array([0.15, 0.3])
    Size = np.array([0.05, 0.2])
    Generic = pygame.Surface(OFFSET*12)
    Generic.fill(COLOR0)
    pygame.draw.circle(Generic, COLOR1, (250, 250), 230)
    pygame.draw.circle(Generic, COLOR2, (250, 250), 190)
    
    def __init__(self, value, speed, PixG):
        self.Value = np.uintc(value)
        self.L = np.ushort(self.Value*PixG/speed)
        self.T = np.linspace(0.25, 1.25, self.L)
        self.CreateImage()
    
    def CreateImage(self):
        Image = self.Generic.copy()
        text = FONT.render(str(self.Value), True, COLOR0)
        textRect = text.get_rect()
        textRect.center = OFFSET*6+[10, 0]
        Image.blit(text, textRect)
        self.Image = pygame.transform.smoothscale(Image, OFFSET*2)
        
        
    def Pos(self, t):
        return self.Center + self.Size * self.trig(self.T[t%self.L])

    def trig(self, Nbr):
        return np.array([np.cos(Nbr*2*np.pi), np.sin(Nbr*2*np.pi)])



A = Number(2, SPEED, PIXGAP)

pygame.init()
ecran = pygame.display.set_mode((0,0), pygame.FULLSCREEN, pygame.NOFRAME)
width, height = ecran.get_size()

Scale = np.array([width, height])


t = 0
while True:
    ecran.fill(COLOR0)
    for events in pygame.event.get():
        pass

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: break
    
    Current = A.Pos(t)*Scale-OFFSET
    ecran.blit(A.Image, Current)
    t += 1
    
    pygame.display.flip()
    pygame.image.save(ecran, f'Images/{t%A.L}.jpg')