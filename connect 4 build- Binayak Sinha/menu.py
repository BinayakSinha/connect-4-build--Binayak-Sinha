import pygame, sys
import subprocess
from menu_button_fun import Button

pygame.init()
ssj=1540
SCREEN = pygame.display.set_mode((ssj, 790))
pygame.display.set_caption("Menu")
size_bg=(ssj, 790)
size_button1=(550,100)
size_button2=(650,100)
size_button3=(350,100)
BG = pygame.image.load("Images/background.png")
BG= pygame.transform.scale(BG, size_bg)
metal= pygame.image.load("Images/metal.png")
metal1= pygame.transform.scale(metal, size_button1)
metal2= pygame.transform.scale(metal, size_button2)
metal3= pygame.transform.scale(metal, size_button3)
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Images/font.ttf", size)

def play():
    while True:

        subprocess.run(["python", "connectfourprogramwithAI_ver3.py"])
        sys.exit()

    
def options():
    while True:
        subprocess.run(["python", "connectfourprogramwithpygame_ver2.py"])
        sys.exit()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Connect 4", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(ssj/2, 150))

        PLAY_BUTTON = Button(metal1, pos=(ssj/2, 300), 
                            text_input="PLAY AI", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(metal2, pos=(ssj/2, 450), 
                            text_input="PLAY pvp", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(metal3, pos=(ssj/2, 600), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
