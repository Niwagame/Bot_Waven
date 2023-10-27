import win32gui
import time

import action
import script
# Lvl 14 taures
# COmbat astrub

def main():
    
    game_window = win32gui.FindWindow(None, "Waven") # Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
    win32gui.SetForegroundWindow(game_window) # Activer la fenêtre du jeu

    if action.move_mouse_to_image("Images/bullpnj.png"): # Appel de la fonction pour déplacer la souris sur l'image du PNJ
        if action.move_mouse_to_image("Images/quete.png"): # Appel de la fonction pour déplacer la souris sur l'image de la quête
                action.click_coor(812, 846) #Clique sur jouer
                time.sleep(3) #Attend que le jeux charge
                action.click_coor(1138, 349) #Clique sur le sol pour ce déplacer et voir le pnj
                time.sleep(2) #Attend que le déplacement sois fini
                action.click_coor_right(1047, 244) # Intéragie avec le pnj
                script.hold_click(3000) # Reste cliquer 2sec pour passé l'annimation
                time.sleep(10) #Attend que le combat ce charge
                action.deplacement(591, 508, 762, 581) # Ce deplace sur le premère mare
                time.sleep(3)
                action.deplacement(755, 584, 964, 583) # Attack le 1er mob
                time.sleep(3)
                action.deplacement(894, 556, 1022, 504) # Attack le 2eme mob
                time.sleep(3)
                action.deplacement(971, 526, 960, 474) # Ce deplace sur le deuxieme mare
                time.sleep(2)
                action.deplacement(968, 481, 924, 404) # Ce deplace sur la troiseme mare
                time.sleep(3)
                action.deplacement(900, 397, 969, 418) # Attack le 3eme mob

if __name__ == '__main__':
    while True:
        main()