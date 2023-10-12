import pyautogui
import win32gui
import time
import keyboard
import action



def main():
    # Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
    game_window = win32gui.FindWindow(None, "Waven")

    # Activer la fenêtre du jeu
    win32gui.SetForegroundWindow(game_window)

    # Vérifie si la souris est à l'intérieur de la fenêtre du jeu
    rect = win32gui.GetWindowRect(game_window)

    # Appel de la fonction pour déplacer la souris sur l'image du PNJ et utiliser F6
    if action.move_mouse_to_image("Images/bullpnj.png"):
        # Appel de la fonction pour déplacer la souris sur l'image de la quête et utiliser F6
        if action.move_mouse_to_image("Images/quete.png"):
                #CLique sur jouer
                action.click_coor(646,682)

                time.sleep(5)
                action.deplacement(397, 407, 526, 475)
                #Place le sort a 6 PA
                action.sort_6pa("Images\sort6pa.png",(605, 431), (648, 451))

                #Passe sont tour
                keyboard.press_and_release('space')
                time.sleep(15)

                # Si le sort Fureur est présent alors il ce le met | Premier paterne !
                if action.sort("Images/boost.png",526,475) :
                    time.sleep(2)
                    # Ce déplacement sur le mob pour le taper
                    action.deplacement(532, 471,645, 406)
                    time.sleep(3)
                    # Ce déplace sur la cases juste a coter pour déclancher le piège
                    action.deplacement(616, 420,658, 453)
                    time.sleep(1)
                    # Place le piege 2 PA
                    action.sort("Images\sort2pa.png", 772,387)
                    time.sleep(1)
                    # Ce deplace sur le piege a 2 PA
                    action.deplacement(649, 455,772, 388)
                    time.sleep(1)
                    # Place le piege 2 PA
                    action.sort("Images\sort2pa.png", 738,373)
                    time.sleep(1)
                    # Ce deplace sur le piege a 2 PA
                    action.deplacement(772, 388,738,373)
                    # Le combat est fini on peut quitter le combat
                    action.abandonner()
                else: # Si le sort Fureur n'est pas présent | Deuxieme Paterne !
                    action.abandonner()


    # Condition dans le premier paterne si une fisure est présente avant de placer le sort 
    # Condition au T2 si un mob est devant le personnage



if __name__ == '__main__':
    while True:
         main()