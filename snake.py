import pygame
import random

ekran_visina = 440
ekran_sirina = 440
ekran = pygame.display.set_mode([ekran_visina, ekran_sirina])
izadi = False


sat = pygame.time.Clock()

class Glava():
    def __init__(self):
        self.lokacija = [random.randint(4,20) * 20,random.randint(4,20) * 20]
        self.smjer = random.randint(0,3)
        return
        

    def kretanje(self):
        okretaj = False
        for dogadaj in pygame.event.get():
            if dogadaj == pygame.QUIT:
                izadi = True
            if dogadaj.type == pygame.KEYDOWN:
                if dogadaj.key == pygame.K_q:
                    izadi == True
                elif dogadaj.key == pygame.K_UP and self.smjer != 2 and not okretaj:
                    self.smjer = 0
                    okrenut = True
                elif dogadaj.key == pygame.K_DOWN and self.smjer != 0 and not okretaj:
                    self.smjer = 2
                    okrenut = True
                elif dogadaj.key == pygame.K_RIGHT and self.smjer != 3 and not okretaj:
                    self.smjer = 1
                    okrenut = True
                elif dogadaj.key == pygame.K_LEFT and self.smjer != 1 and not okretaj:
                     self.smjer = 3
                     okretaj = True
        if self.smjer == 0:
            self.lokacija[1] -= 20
        if self.smjer == 1:
            self.lokacija[0] += 20
        if self.smjer == 2:
            self.lokacija[1] += 20
        if self.smjer == 3:
            self.lokacija[0] -= 20
            
        if glava.lokacija[0] < 0:
            glava.lokacija[0] = 420
        if glava.lokacija[0] > 420:
            glava.lokacija[0] = 0
        if glava.lokacija[1] < 0:
            glava.lokacija[1] = 420
        if glava.lokacija[1] > 420:
            glava.lokacija[1] = 0

        return

tjelo = []
glava = Glava()
okretaja = 0
mjesto_hrane = [random.randint(1, 20) * 20,random.randint(1, 20) * 20]
while not izadi:
    sat.tick(15)
    okretaja += 1
    hrana = False
    if glava.lokacija == mjesto_hrane:
        hrana = True
        mjesto_hrane = [random.randint(1, 20) * 20,random.randint(1, 20) * 20]
    if (okretaja < 3):
        hrana = True
    if not hrana:
        del tjelo[0]
    tjelo.append([glava.lokacija[0],glava.lokacija[1]])
    glava.kretanje()
            
    ekran.fill([0,0,0])

    for dio in tjelo:
        pygame.draw.rect(ekran,[255,255,255],[dio[0],dio[1],20,20],0)
        if dio != tjelo[0] and dio == glava.lokacija:
            izadi = True
            
    pygame.draw.rect(ekran,[255,255,255],[glava.lokacija[0],glava.lokacija[1],20,20],0)
    pygame.draw.rect(ekran,[255,0,0],[mjesto_hrane[0],mjesto_hrane[1],20,20],0)
    pygame.display.flip()
pygame.quit()
