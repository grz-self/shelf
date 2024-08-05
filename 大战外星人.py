import time
import pygame,pygame.font
import sys
import random
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound('biuboom.mp3')
ha=0
sound1=pygame.mixer.Sound("music1.mp3")
sound1.play()
over=pygame.mixer.Sound("over.mp3")
win=pygame.mixer.Sound("win.mp3")
ad=pygame.mixer.Sound("ad.mp3")
root = pygame.display.set_mode((500, 550))
randoms=[0,100,200,300,400]
font=pygame.font.Font(None,50)
pygame.display.set_caption("My Game") 
clock = pygame.time.Clock()
sprite_image = pygame.image.load("plane.png")
biu=pygame.image.load("biubiu.png")
wxrim=pygame.image.load("wxrim.png")
xim=pygame.image.load("x.png")
fim=pygame.image.load("f.png")
class x(pygame.Rect):
    def __init__(self):
        super().__init__(10,490,50,50)
        self.image=xim
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=490
class f(pygame.Rect):
    def __init__(self):
        super().__init__(270,490,50,50)
        self.image=fim
        self.rect=self.image.get_rect()
        self.rect.x=270
        self.rect.y=490
nf=f()
nx=x()
class ZzRect(pygame.Rect):
    def __init__(self):
        super().__init__(225, 400, 50, 50)
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.x = 225
        self.rect.y = 400
        self.change_x = 0
    def go(self):
        self.rect.x += self.change_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 475:
            self.rect.x = 475
r = ZzRect()
class b(pygame.Rect):
    def __init__(self):
        super().__init__(225,400,10,10)
        self.image = biu
        self.rect = self.image.get_rect()
        self.rect.x = 225
        self.rect.y = 400
        self.change_y = 0
        self.fly=False
        self.out=False
    def go(self):
        self.rect.y+=self.change_y
        if self.rect.y < 10:
            self.out=True
        else:
            self.out=False
bi=b()
class wxr(pygame.Rect):
    def __init__(self,y):
        super().__init__(0,y,40,80)
        self.image=wxrim
        self.rect=self.image.get_rect()
        self.rect.x=0
        self.rect.y=y
        self.change_y=1
    def randomwz(self):
        self.ra=randoms[random.randint(0,4)]
        self.rect.x=self.ra
    def go(self):
        self.rect.y+=self.change_y
    def stop(self):
        self.randomwz()
        self.rect.y=-80
w1=wxr(-80)
w2=wxr(-160)
w3=wxr(-320)
running=True
fs=[2,2,2,2,3,3,4,5]
sy=0
zx=False
x=8
f=0
w1.randomwz()
w2.randomwz()
w3.randomwz()
while running:
    clock.tick(80)
    sy+=1
    text = font.render("life value:"+str(x),True,(225,0,0))
    text1 = font.render("score:"+ str(f),True,(225,255,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                r.change_x = -0.8
            elif e.key == pygame.K_RIGHT:
                r.change_x = 0.8
            if e.key == pygame.K_DOWN:
                r.change_x=0
            if e.key == pygame.K_SPACE:
                r.change_x=0
                ha+=1
                print("你作弊了")
                zd=max(w1.rect.y,w2.rect.y,w3.rect.y)
                if w1.rect.y == zd:
                    r.rect.x=w1.rect.x
                if w2.rect.y == zd:
                    r.rect.x=w2.rect.x
                if w3.rect.y == zd:
                    r.rect.x=w3.rect.x
            if e.key == pygame.K_UP:
                sound.play()
            if e.key == pygame.K_UP or bi.fly and not bi.out:
                zx=True
                bi.change_y=-3
                bi.fly=True
            else:
                zx=False
        if not zx:
            bi.change_y=0
            bi.rect.x=r.rect.x
            bi.rect.y=r.rect.y
    bi.go()
    if bi.out:
        bi.change_y=0
        bi.fly=False
        bi.rect.x=r.rect.x
        bi.rect.y=r.rect.y
    r.go()
    w1.go()
    w2.go()
    w3.go()
    if bi.rect.colliderect(w1.rect):
        w1.stop()
        f+=random.choice(fs)
        print(f)
    if bi.rect.colliderect(w2.rect):
        w2.stop()
        f+=random.choice(fs)
        print(f)
    if bi.rect.colliderect(w3.rect):
        w3.stop()
        f+=random.choice(fs)
        print(f)
    if 350 < w1.rect.y:
        w1.stop()
        x-=1
        print("生命："+str(x))
        ad.play()
    if 350 < w2.rect.y:
        w2.stop()
        x-=1
        print("生命："+str(x))
        ad.play()
    if w3.rect.y > 350:
        w3.stop()
        x-=1
        print("生命："+str(x))
        ad.play()
    root.fill((0, 220, 220))
    root.blit(r.image, r.rect)
    root.blit(bi.image,bi.rect)
    root.blit(w1.image,w1.rect)
    root.blit(w2.image,w2.rect)
    root.blit(w3.image,w3.rect)
    root.blit(text, (70, 500))
    root.blit(nx.image,nx.rect)
    root.blit(text1,(330,500))
    root.blit(nf.image,nf.rect)
    pygame.display.flip()
    if f >= 20:
        root.fill((0, 220, 220))
        text = font.render("life value:"+str(x),True,(225,0,0))
        text1 = font.render("score:"+ str(f),True,(225,225,0))
        text2=font.render("win",True,(0,0,0))
        root.blit(text1,(330,500))
        root.blit(text, (70, 500))
        root.blit(text2,(150,250))
        pygame.display.flip()
        running=False
        print("you are winner")
        sound1.stop()
        win.play()
        time.sleep(1)
    if x == 0:
        root.fill((0, 220, 220))
        text = font.render("life value:"+str(x),True,(225,0,0))
        text1 = font.render("score:"+ str(f),True,(225,225,0))
        text2=font.render("game over",True,(0,0,0))
        root.blit(text1,(330,500))
        root.blit(text, (70, 500))
        root.blit(text2,(150,250))
        pygame.display.flip()
        running=False
        print("game over")
        sound1.stop()
        over.play()
        for i in range(5):
            time.sleep(1)
if ha >= 5: 
    print( "恭喜你，获得作弊小能手称号")
sys.exit()
#217行，新高