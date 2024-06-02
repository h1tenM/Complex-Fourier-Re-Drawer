import pygame
import argparse as ap
from time import sleep
from cmath import *
from src.button import Button


TEXT_COL = ('white')

class Controller:
  
  def __init__(self):
    #setup pygame data
    self.screen = pygame.display.set_mode() #work on sizing and work on button layout
    self.WIDTH, self.HEIGHT = self.screen.get_size()
    pygame.display.set_caption("Fourier Draw")
    #menu buttons go there
    self.resume_button = Button((self.WIDTH/2 - 87.5), ((self.HEIGHT/3)/2 - 37.5), color=(105,105,105), text="Resume")
    self.options_button = Button((self.WIDTH/2 - 87.5), ((self.HEIGHT/3 + self.HEIGHT/3/2)-37.5), color=(105,105,105), text="Options")
    self.quit_button = Button(self.WIDTH/2 - 87.5, 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Quit")
    self.color_button = Button(self.WIDTH/2 - 87.5, (self.HEIGHT/3)/2 - 37.5, color=(105,105,105), text="Color")
    #self.equation_button = Button(self.WIDTH/2 - 87.5, (self.HEIGHT/3 + self.HEIGHT/3/2)-37.5, color=(105,105,105), text="Equation")

    self.back_button = Button(self.WIDTH/2 - 87.5, 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Back")
    #self.back_button2 = Button((self.WIDTH/2 - 87.5), 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Back")
    self.back_button2 = Button(self.WIDTH/2 - 87.5, 2*(self.HEIGHT/3 + self.HEIGHT/3/2)-175, color=(105,105,105), text="Back")

    #color buttons
    self.color = (255,0,0)
    self.red_button = Button((self.WIDTH/2 - 37.5 - 112.5), self.HEIGHT/3/2 - 37.5, width=75, height=75,  color=(255,0,0), text="R")
    self.blue_button = Button((self.WIDTH/2 - 37.5), self.HEIGHT/3/2 - 37.5, width=75, height=75,  color=(0,0,255), text="Bl")
    self.green_button = Button((self.WIDTH/2 - 37.5 + 112.5), self.HEIGHT/3/2 - 37.5, width=75, height=75,  color=(2,207,2), text="G")
    self.yellow_button = Button((self.WIDTH/2 - 37.5 - 112.5), self.HEIGHT/3/2 - 37.5 + 112.5, width=75, height=75,  color=(255,255,0), text="Y")
    self.orange_button = Button((self.WIDTH/2 - 37.5), self.HEIGHT/3/2 - 37.5 + 112.5, width=75, height=75,  color=(255,128,0), text="O")
    self.purple_button = Button((self.WIDTH/2 - 37.5 + 112.5), self.HEIGHT/3/2 - 37.5 + 112.5, width=75, height=75,  color=(127,0,255), text="Pu")
    self.pink_button = Button((self.WIDTH/2 - 37.5 - 112.5), self.HEIGHT/3/2 - 37.5 + 112.5 + 112.5, width=75, height=75,  color=(255,153,255), text="Pi")
    self.gold_button = Button((self.WIDTH/2 - 37.5), self.HEIGHT/3/2 - 37.5 + 112.5 + 112.5, width=75, height=75,  color=(219, 172, 52), text="Au")
    self.silver_button = Button((self.WIDTH/2 - 37.5 + 112.5), self.HEIGHT/3/2 - 37.5 + 112.5 + 112.5, width=75, height=75,  color=(192,192,192), text="Ag")

    self.menu_buttons = pygame.sprite.Group(self.resume_button, self.options_button, self.quit_button)
    
    self.options_buttons = pygame.sprite.Group(self.color_button, self.back_button)
    
    self.color_buttons = pygame.sprite.Group(self.back_button2, self.red_button, self.blue_button, self.green_button, self.yellow_button,
                                      self.orange_button, self.purple_button, self.pink_button, self.gold_button, self.silver_button)
    
    
    #gamestates
    #self.game_paused = False #ask if redudant
    #self.menu_state = 'Paused' #ask if redudant
    self.state = 'Gameloop'
    self.font =  pygame.font.SysFont('arialblack',30)
    '''
    description: This initializes the conroller, creates the screen and all buttons as well as sets the state
    arg description: no arguement
    return: intializes the controller
    '''

  def draw_text(self, text, font, text_col, x, y):
    img = font.render(text,True, text_col)
    self.screen.blit(img, (x,y))
    '''
    description: This function allows for text to be drawn on screen 
    arg description: This takes in the wanted text, the color of the text, and its x and y positions
    return: it returns the text onto the screen
    '''
    
  def mainloop(self):
    #select state loop
    while True:
      if self.state == 'Menu':
         self.menuloop()
    
      elif self.state == 'Gameloop':
         self.gameloop()

      elif self.state == 'Options':
        self.optionsloop()
    
      elif self.state == 'Color':
        self.colorloop()
    
      #elif self.state == 'Equation':
        #self.equationloop()
    '''
    description: This selects the different loops based on the state of the game depending on the button that is pressed.  
    arg description: N/A
    return: it returns the desired loop
    '''

    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
    while self.state == 'Menu':
      self.screen.fill((0,0,0))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
          for button in self.menu_buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.resume_button.rect.collidepoint(event.pos):
                self.state = "Gameloop"
          if self.quit_button.rect.collidepoint(pygame.mouse.get_pos()):
              pygame.quit()
          if self.options_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Options'
      # not update section

      # need to redraw buttons
      self.menu_buttons.draw(self.screen)
      self.draw_text("Press ESC to Exit", self.font, TEXT_COL, 20, 20)
      
      pygame.display.update()
    '''
    description: This is the menu loop for when the game is paused  
    arg description: N/A
    return: it returns the menu loop
    '''
        
  def optionsloop(self):
    while self.state == 'Options':
      self.screen.fill((0,0,0))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
          for button in self.options_buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.color_button.rect.collidepoint(event.pos):
                self.state = "Color"
          #if self.equation_button.rect.collidepoint(pygame.mouse.get_pos()):
              #self.state == 'Equation'
          if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Menu'
      # not update section

      # need to redraw buttons
      self.options_buttons.draw(self.screen)
      self.draw_text("Press ESC to Exit", self.font, TEXT_COL, 20, 20)
      
      pygame.display.update()
    '''
    description: This brings up the options that the program allows for if that is what button is clicked in the menu loop.  
    arg description: N/A
    return: it returns the options loop
    '''
  
  def colorloop(self):
    while self.state == 'Color':
      self.screen.fill((0,0,0))
      #check if game is paused
      for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
          for button in self.color_buttons:
              if button.rect.collidepoint(event.pos):
                  button.highlight()
                  self.screen.blit(button.image, button.rect.topleft)
              else:
                button.color_default()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.red_button.rect.collidepoint(event.pos): 
                self.color = (255,0,0)
                print('red')
          if self.green_button.rect.collidepoint(event.pos): 
                self.color = (0,255,0)
                print('green')
          if self.blue_button.rect.collidepoint(event.pos): 
                self.color = (0,0,255)
                print('blue')
          if self.yellow_button.rect.collidepoint(event.pos):
                self.color = (255,255,0)
                print('yellow')
          if self.orange_button.rect.collidepoint(event.pos): 
                self.color = (255,128,0)
                print('orange')
          if self.purple_button.rect.collidepoint(event.pos): 
                self.color = (127,0,255)
                print('purple')
          if self.pink_button.rect.collidepoint(event.pos): 
                self.color = (255,153,255)
                print('pink')
          if self.gold_button.rect.collidepoint(event.pos): 
                self.color = (219, 172, 52)
                print('gold')
          if self.silver_button.rect.collidepoint(event.pos): 
                self.color = (192,192,192)
                print('silver')
          
          if self.back_button2.rect.collidepoint(pygame.mouse.get_pos()):
              self.state = 'Options'
      # not update section

      # need to redraw buttons
      self.color_buttons.draw(self.screen)
      self.draw_text("Press ESC to Exit", self.font, TEXT_COL, 20, 20)
      self.draw_text("Choose your Color!", self.font, TEXT_COL, self.WIDTH/2 - 87.5, (self.HEIGHT/3 + self.HEIGHT/3/2)-37.5+30)
      
      pygame.display.update()
    '''
    description: This brings the user to the menu that allows for different colors to be selected for the drawing. 
    arg description: N/A
    return: it returns the selected color for the drawing 
    '''
       
           
  def gameloop(self):
    while self.state == 'Gameloop':
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                  self.state = "Menu"
                if event.key == pygame.K_ESCAPE:
                  pygame.quit()
              
            if event.type == pygame.QUIT:  
              run = False

        if self.state != 'Gameloop':
            break
        def draw_grid(text):
            self.screen.fill(pygame.Color(30, 30, 30))
            pygame.draw.line(self.screen, pygame.Color(120, 120, 120), (self.WIDTH//2, 0), (self.WIDTH//2, self.HEIGHT))
            for i in range(50, self.WIDTH//2, 50):
                pygame.draw.line(self.screen, pygame.Color(90, 90, 90), (self.WIDTH//2+i, 0), (self.WIDTH//2+i, self.HEIGHT))
                pygame.draw.line(self.screen, pygame.Color(90, 90, 90), (self.WIDTH//2-i, 0), (self.WIDTH//2-i, self.HEIGHT))
            pygame.draw.line(self.screen, pygame.Color(120, 120, 120), (0, self.HEIGHT//2), (self.WIDTH, self.HEIGHT//2))
            for i in range(50, self.HEIGHT//2, 50):
                pygame.draw.line(self.screen, pygame.Color(90, 90, 90), (0, self.HEIGHT//2+i), (self.WIDTH, self.HEIGHT//2+i))
                pygame.draw.line(self.screen, pygame.Color(90, 90, 90), (0, self.HEIGHT//2-i), (self.WIDTH, self.HEIGHT//2-i))

            if text == True:
                font = pygame.font.SysFont(pygame.font.get_default_font(), 30)
                start_text = font.render("press d to start/stop drawing, press r to restart, Space for Menu, ESC to leave", True, pygame.Color(220, 220, 220))
                self.screen.blit(start_text, ((self.WIDTH - start_text.get_width())//2, (self.HEIGHT - start_text.get_height())//2))
                pygame.display.update()
            '''
            Description: This what creates the grid pattern seen in some of the screens. Depending on the state of the arg, the instructions are show as well
            args: text: true or false desides if the instructions are shown or not
            return: returns text and the background of screen
            '''
            
        p = ap.ArgumentParser(description = "Replicate drawing using Fourier Transform")
        p.add_argument("-n", default = 10, type = int, help = "number of circles to use (default is 10)")
        p.add_argument("-m", "--mode", default = "increase", choices = ["loop", "increase"], help = "whether the number of circles should stay constant or increase after each loop (default is 'loop')")
        args = p.parse_args()
        
        def round(p):
            x, y = p
            return (int(x), int(y))
        '''
        Description: This takes in command line arguements so that different values are returned
        args: p: the parser for the command line
        return: returns integer values of the x and y
        '''

        def main():

            draw_grid(True)
            

            wait = True
            while wait:
                sleep(0.005)
                for e in pygame.event.get():
                    if e.type == pygame.KEYUP and e.key == pygame.K_d:
                        wait = False
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_SPACE:
                            self.state = "Menu"
                        if e.key == pygame.K_ESCAPE:
                            pygame.quit()
                if self.state != 'Gameloop':
                    wait = False
                    break

            print("recording track")

            track = [pygame.mouse.get_pos()]
            wait = True
            while wait:
                sleep(0.005)
                for e in pygame.event.get():
                    if e.type == pygame.KEYUP and e.key == pygame.K_d:
                        wait = False
                    if e.type == pygame.KEYDOWN and e.key == pygame.K_r:#djdnsfl;kdsf
                        main()
                    if e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_SPACE:
                            self.state = "Menu"
                        if e.key == pygame.K_ESCAPE:
                            pygame.quit()
                if self.state != 'Gameloop':
                    wait = False
                    break
                x0, y0 = track[-1]
                x1, y1 = pygame.mouse.get_pos()
                d = ((x1 - x0)**2 + (y1 - y0)**2)**0.5
                for i in range(2, int(d), 2):
                    track.append((x0 + (x1-x0)*i/d, y0 + (y1-y0)*i/d))
                draw_grid(False)
                self.draw_text("Press ESC to Exit, Press Space for Menu, R to Restart, D to Start", self.font, TEXT_COL, 20, 20)
                for p in track:
                    self.screen.set_at(round(p), pygame.Color(220, 220, 220))
                pygame.display.update()

            print("processing track")

            save_coordinates = open("src/coordinates.txt", 'w')
            #save_coordinates.write(f"Here are the Cartesian coordinates of your drawing \n")
            #save_coordinates.close()
            #save_coordinates = open("src/coordinates.txt", 'a')
            tl = len(track)
            for i in range(tl):
                x, y = track[i]
                track[i] = (x-self.WIDTH//2, y-self.HEIGHT//2)
                #print(x,y,x-self.WIDTH//2, y-self.HEIGHT//2,)
                save_coordinates.write(f"x: {x-self.WIDTH//2}, y: {y-self.HEIGHT//2}\n" )
            save_coordinates.close()


            ftrack = []
            n = args.n
            wait = True
            while wait:
                print("drawing witn n = %d"%n)
                if ftrack == []:
                    c = []
                    for i in range(n, -n-1, -1):
                        c.append(sum(exp(2*pi*1j*i*t/tl)*(track[t][0]+track[t][1]*1j) for t in range(tl))/tl)

                for t in range(tl):
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_r:#iujrifjf
                            main()
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_SPACE:
                                self.state = "Menu"
                            if e.key == pygame.K_ESCAPE:
                                pygame.quit()
                    if self.state != 'Gameloop':
                        wait = False
                        break
                    # sleep(0.005)
                    self.screen.fill(pygame.Color(30, 30, 30))
                    z = self.WIDTH//2 + self.HEIGHT//2*1j
                    # for i in range(2*n+1):
                    for i in sum(zip(range(n+1, 2*n+1), range(n-1, -1, -1)), (n,)):
                        old_z = z
                        z += exp(2*pi*1j*(i-n)*t/tl)*c[i] 
                        pygame.draw.line(self.screen, pygame.Color(120, 120, 120), (old_z.real, old_z.imag), (z.real, z.imag))
                        r = ((old_z.real - z.real)**2 + (old_z.imag - z.imag)**2)**0.5
                        if r > 1:
                            pygame.draw.circle(self.screen, pygame.Color(90, 90, 90), (int(old_z.real), int(old_z.imag)), int(r), 1)
                    if len(ftrack) < tl:
                        ftrack.append(z)

                    #z = sum(exp(2*pi*1j*(i-n)*t/tl)*c[i] for i in range(2*n+1))
                    for i in range(len(ftrack)):
                        color = self.color[:]
                        p = ftrack[i]
                        self.screen.set_at((int(p.real), int(p.imag)), color)
                    self.draw_text("Press ESC to Exit, Press Space for Menu, R to Restart", self.font, TEXT_COL, 20, 20)
                    pygame.display.update()

                if args.mode == "increase":
                    n += 2
                    ftrack = []

        main()
              
        #self.draw_text("Press ESC to Exit, Press Space for Menu", self.font, TEXT_COL, 20, 20)
        pygame.display.update()
        '''
        description: This is the game loop where the actual drawing takes place  
        arg description: N/A
        return: it returns the game loop
        '''