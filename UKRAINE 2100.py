#Підключення модулів
import pygame
from random import *
import time




#Кольори
WHITE = (255,255,255)
YELLOW = (255,213,0)
BLACK = (0,0,0)



#Підключення сцени та ігрового циклу
pygame.init()
window = pygame.display.set_mode((1000,650))
window.fill((0,0,0))
clock = pygame.time.Clock()



#Класи
class Area():
    def __init__(self,x=0,y=0, width = 10, height = 10, color = None):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self,filename,x=0,y=0, width = 10, height = 10, color = None):
        super().__init__(x,y,width,height,color)
        self.image = pygame.image.load(filename)
    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.Font('freesansbold.ttf', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



#Лічильники
point = 0


score = Label(200,53,80,25,YELLOW)
score.set_text(str(point),28,WHITE)
score.draw(0,0)

timer = Label(875,53,50,25, YELLOW)
timer.set_text("0",28,WHITE)
timer.draw(0,0)



#Спрайти
start_button = Picture("pics/startbutton.png",350,240,290,75)
start_button_select = Picture("pics/startbuttonselect.png",350,240,290,75)
settings_button = Picture("pics/settingsbutton.png",350,365,290,75)
settings_button_select = Picture("pics/settingsbuttonselect.png",350,365,290,75)
info_zone = Picture("pics/info.png",0,0,1000,500)
quit_button = Picture("pics/quitbutton.png",350,490,290,75)
quit_button_select = Picture("pics/quitbuttonselect.png",350,490,290,75)
start_bg = Picture("pics/start.png",0,0,1000,650)
go_back_button = Picture("pics/gobackbutton.png",50,50,80,80)
go_back_button_select = Picture("pics/gobackbuttonselect.png",50,50,80,80)
go_button = Picture("pics/gobutton.png",460,300,80,80)
go_button_select = Picture("pics/gobuttonselect.png",460,300,80,80)
kherson_1 = Picture("pics/kherson-1.png",0,0,1000,650)
melitopol_2 = Picture("pics/melitopol-2.png",0,0,1000,650)
nizhyn_3 = Picture("pics/nizhyn-3.png",0,0,1000,650)
uzhhorod_4 = Picture("pics/uzhhorod-4.png",0,0,1000,650)
mars_5 = Picture("pics/mars-5.png", 0,0,1000,650)
kavun = Picture("pics/kavun-1.png", randint(100,900), randint(50,450), 50,50)
cherry = Picture("pics/cherry-2.png", randint(100,900), randint(50,450), 50,50)
cucumber = Picture("pics/cucumber-3.png", randint(100,900), randint(50,450), 50,50)
mushroom = Picture("pics/mushroom-4.png", randint(100,900), randint(50,450), 50,50)
mars_fruit = Picture("pics/marsfruit-5.png", randint(100,900), randint(50,450), 50,50)
next = Picture("pics/next.png", 320,350,325,75)
next_select = Picture("pics/nextselected.png",320,350,325,75)
result = Picture("pics/result.png", 320,350,350,75)
result_select = Picture("pics/resultselected.png",320,350,350,75)
final = Picture("pics/final.png", 0,0,1000,650)
mainmenu_button = Picture("pics/mainmenu.png",320,350,290,75)
mainmenu_button_select = Picture("pics/mainmenuselected.png",320,350,290,75)






#Надання початкових значень
wait = 10
screen = "menu"



#Ігровий цикл
while True:
    #Завершення гри при натисканні на хрестик
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 

    
    
    #Екран Меню
    if screen == "menu":
        #Малювання спрайтів
        start_bg.draw()
        start_button.draw()
        settings_button.draw()
        quit_button.draw()
        
        
        
        #Зміна кольору при наведенні мишкою
        x,y = pygame.mouse.get_pos()
        if start_button_select.rect.collidepoint(x,y):
            start_button_select.draw()
        if settings_button_select.rect.collidepoint(x,y):
            settings_button_select.draw()
        if quit_button_select.rect.collidepoint(x,y):
            quit_button_select.draw()
        if start_button.rect.collidepoint(x,y):
            start_button_select.draw()
        if settings_button.rect.collidepoint(x,y):
            settings_button_select.draw()
        if quit_button.rect.collidepoint(x,y):
            quit_button_select.draw()
        
        
        
        #Натискання на кнопки
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x,y = event.pos
                if start_button_select.rect.collidepoint(x,y) or start_button.rect.collidepoint(x,y):
                    screen = "level 1"
                    kherson_1.draw()
                    start_time = time.time()
                    cur_time = start_time
                if settings_button_select.rect.collidepoint(x,y) or settings_button.rect.collidepoint(x,y):
                    screen = "settings"
                if quit_button_select.rect.collidepoint(x,y) or quit_button.rect.collidepoint(x,y):
                    pygame.quit()
    
    
    
    
    #Екран Перший рівень
    if screen == "level 1":
        #Лічильник часу
        new_time = time.time()
        if int(new_time) - int(cur_time) == 1:
            timer.set_text(str(int(new_time - start_time)),28,WHITE)
            timer.draw(0,0)
            cur_time = new_time
            
        
        #Промалювання спрайтів лічильників
        timer.draw()
        score.draw()
        
        
        
        #Поява нового кавуну
        if wait == 0 or kavun.rect.collidepoint(x,y):
            wait = 120
            kherson_1.draw()
            kavun = Picture("pics/kavun-1.png", randint(100,900), randint(150,450), 50,50)
            kavun.draw()
        else:
            wait -= 1
            
            
        
        #Натискання на кавун
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x,y = event.pos
            if kavun.rect.collidepoint(x,y):
                point += 1
                score.set_text(str(point),28,WHITE)
                score.draw(0,0)
                
                
        
        #Закінчення Першого рівня
        if int(new_time - start_time) >= 16:
            kherson_1.draw()
            next.draw()
            score.draw()
            x,y = pygame.mouse.get_pos()
            if next.rect.collidepoint(x,y):
                next_select.draw()
            
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                    if next.rect.collidepoint(x,y) or next_select.rect.collidepoint(x,y):
                        start_time = time.time()
                        cur_time = start_time
                        new_time = time.time()
                        melitopol_2.draw()
                        screen = "level 2"
            
    #Екран Другий рівень
    if screen == "level 2":
        #Лічильник часу
        new_time = time.time()
        if int(new_time) - int(cur_time) == 1:
            timer.set_text(str(int(new_time - start_time)),28,WHITE)
            timer.draw(0,0)
            cur_time = new_time
            
        
        #Промалювання спрайтів лічильників
        timer.draw()
        score.draw()
        
        
        
        #Поява нової черешні
        if wait == 0 or cherry.rect.collidepoint(x,y):
            wait = 90
            melitopol_2.draw()
            cherry = Picture("pics/cherry-2.png", randint(100,900), randint(150,450), 50,50)
            cherry.draw()
        else:
            wait -= 1
            
            
        
        #Натискання на черешню
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x,y = event.pos
            if cherry.rect.collidepoint(x,y):
                point += 2
                score.set_text(str(point),28,WHITE)
                score.draw(0,0)
                
                
        
        #Закінчення Другого рівня
        if int(new_time - start_time) >= 16:
            melitopol_2.draw()
            next.draw()
            score.draw()
            x,y = pygame.mouse.get_pos()
            if next.rect.collidepoint(x,y):
                next_select.draw()
            
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                    if next.rect.collidepoint(x,y) or next_select.rect.collidepoint(x,y):
                        start_time = time.time()
                        cur_time = start_time
                        new_time = time.time()
                        nizhyn_3.draw()
                        screen = "level 3"
                        
    #Екран Третій рівень
    if screen == "level 3":
        #Лічильник часу
        new_time = time.time()
        if int(new_time) - int(cur_time) == 1:
            timer.set_text(str(int(new_time - start_time)),28,WHITE)
            timer.draw(0,0)
            cur_time = new_time
            
        
        #Промалювання спрайтів лічильників
        timer.draw()
        score.draw()
        
        
        
        #Поява нового огірка
        if wait == 0 or cucumber.rect.collidepoint(x,y):
            wait = 60
            nizhyn_3.draw()
            cucumber = Picture("pics/cucumber-3.png", randint(100,900), randint(150,450), 50,50)
            cucumber.draw()
        else:
            wait -= 1
            
            
        
        #Натискання на огірок
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x,y = event.pos
            if cucumber.rect.collidepoint(x,y):
                point += 5
                score.set_text(str(point),28,WHITE)
                score.draw(0,0)
                
                
        
        #Закінчення Третього рівня
        if int(new_time - start_time) >= 16:
            nizhyn_3.draw()
            next.draw()
            score.draw()
            x,y = pygame.mouse.get_pos()
            if next.rect.collidepoint(x,y):
                next_select.draw()
            
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                    if next.rect.collidepoint(x,y) or next_select.rect.collidepoint(x,y):
                        start_time = time.time()
                        cur_time = start_time
                        new_time = time.time()
                        uzhhorod_4.draw()
                        screen = "level 4"
    
    #Екран Четвертий рівень
    if screen == "level 4":
        #Лічильник часу
        new_time = time.time()
        if int(new_time) - int(cur_time) == 1:
            timer.set_text(str(int(new_time - start_time)),28,WHITE)
            timer.draw(0,0)
            cur_time = new_time
            
        
        #Промалювання спрайтів лічильників
        timer.draw()
        score.draw()
        
        
        
        #Поява нового гриба
        if wait == 0 or mushroom.rect.collidepoint(x,y):
            wait = 45
            uzhhorod_4.draw()
            mushroom = Picture("pics/mushroom-4.png", randint(100,900), randint(150,450), 50,50)
            mushroom.draw()
        else:
            wait -= 1
            
            
        
        #Натискання на гриб
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x,y = event.pos
            if mushroom.rect.collidepoint(x,y):
                point += 10
                score.set_text(str(point),28,WHITE)
                score.draw(0,0)
                
                
        
        #Закінчення Четвертого рівня
        if int(new_time - start_time) >= 16:
            uzhhorod_4.draw()
            next.draw()
            score.draw()
            x,y = pygame.mouse.get_pos()
            if next.rect.collidepoint(x,y):
                next_select.draw()
            
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                    if next.rect.collidepoint(x,y) or next_select.rect.collidepoint(x,y):
                        start_time = time.time()
                        cur_time = start_time
                        new_time = time.time()
                        mars_5.draw()
                        screen = "level 5"

    #Екран П'ятий(Бонус) рівень
    if screen == "level 5":
        #Лічильник часу
        new_time = time.time()
        if int(new_time) - int(cur_time) == 1:
            timer.set_text(str(int(new_time - start_time)),28,WHITE)
            timer.draw(0,0)
            cur_time = new_time
            
        
        #Промалювання спрайтів лічильників
        timer.draw()
        score.draw()
        
        
        
        #Поява нового фрукту
        if wait == 0 or mars_fruit.rect.collidepoint(x,y):
            wait = 30
            mars_5.draw()
            mars_fruit = Picture("pics/marsfruit-5.png", randint(100,900), randint(150,450), 50,50)
            mars_fruit.draw()
        else:
            wait -= 1
            
            
        
        #Натискання на фрукт
        if event.type == pygame.MOUSEBUTTONDOWN: 
            x,y = event.pos
            if mars_fruit.rect.collidepoint(x,y):
                point += 20
                score.set_text(str(point),28,WHITE)
                score.draw(0,0)
                
                
        
        #Закінчення П'ятого рівня
        if int(new_time - start_time) >= 16:
            mars_5.draw()
            result.draw()
            score.draw()
            x,y = pygame.mouse.get_pos()
            if result.rect.collidepoint(x,y):
                result_select.draw()
            
            for event in pygame.event.get(): 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                    if result.rect.collidepoint(x,y) or result_select.rect.collidepoint(x,y):
                        start_time = time.time()
                        cur_time = start_time
                        new_time = time.time()
                        final.draw()
                        screen = "final"

    #Фінальний екран
    if screen == "final":
        score = Label(445,95,80,25,YELLOW)
        score.set_text(str(point),28,WHITE)
        final.draw()
        score.draw()
        mainmenu_button.draw()
        x,y = pygame.mouse.get_pos()
        if mainmenu_button.rect.collidepoint(x,y):
            mainmenu_button_select.draw()
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                    x,y = event.pos
                    if mainmenu_button.rect.collidepoint(x,y) or mainmenu_button_select.rect.collidepoint(x,y):
                        score = Label(200,53,80,25,YELLOW)
                        point = 0
                        score.set_text(str(point),28,WHITE)
                        score.draw(0,0)
                        screen = "menu"

    
    #Екран Налаштування
    if screen == "settings":
        text1 = Label(300,200,0,0,YELLOW)
        text1.set_text("WELCOME TO UKRAINE 2100",27,WHITE)
        text2 = Label(300,250,0,0,YELLOW)
        text2.set_text("Ваше завдання - зібрати максимальну кількість",16,WHITE)
        text3 = Label(300,270,0,0,YELLOW)
        text3.set_text(" їжі в 5-ти різних локаціях для відправлення",16,WHITE)
        text4 = Label(300,290,0,0,YELLOW)
        text4.set_text("поселенням на інших планетах.",16,WHITE)
        text5 = Label(300,340,0,0,YELLOW)
        text5.set_text("1 Lv. Херсон = 1 point/кавун",16,WHITE)
        text6 = Label(300,360,0,0,YELLOW)
        text6.set_text("2 Lv. Мелітополь = 2 points/черешня",16,WHITE)
        text7 = Label(300,380,0,0,YELLOW)
        text7.set_text("3 Lv. Ніжин = 5 points/огірок",16,WHITE)
        text8 = Label(300,400,0,0,YELLOW)
        text8.set_text("4 Lv. Ужгород = 10 points/печериця",16,WHITE)
        text9 = Label(300,420,0,0,YELLOW)
        text9.set_text("5 Lv. Марсіанська обл. = 20 points/марсарин",16,WHITE)
        

        
        #Промалювання спрайтів
        info_zone.draw()
        go_back_button.draw()
        text1.draw()
        text2.draw()
        text3.draw()
        text4.draw()
        text5.draw()
        text6.draw()
        text7.draw()
        text8.draw()
        text9.draw()
        
        
        #Зміна кольору при наведенні мишкою
        x,y = pygame.mouse.get_pos()
        if go_back_button.rect.collidepoint(x,y):
            go_back_button_select.draw()
        
        
        
        #Натискання на кнопку повернення у Меню
        for event in pygame.event.get(): 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                x,y = event.pos
                if go_back_button_select.rect.collidepoint(x,y) or go_back_button_select.rect.collidepoint(x,y):
                    screen = "menu"
    
    
    #Завершення ігрового циклу
    pygame.display.update()
    clock.tick(60)