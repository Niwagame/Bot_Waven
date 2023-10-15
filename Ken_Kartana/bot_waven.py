import win32gui
import time
import keyboard
import script

import action

nb_combat = 0
nb_combat_failed = 0
nb_combat_win = 0

#Images dans sort//6pa non trouvées.

def main():

    global nb_combat 
    global nb_combat_failed
    global nb_combat_win

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
                action.click_coor(812, 846)

                time.sleep(5)
                action.deplacement(484, 503, 646, 586)
                #Place le sort a 6 PA
                if action.sort_6pa("Images/sort/6pa",(758, 533), (797, 560)):
                    #Passe sont tour
                    keyboard.press_and_release('space')
                    time.sleep(15)

                    # Si le sort Fureur est présent alors il ce le met | Premier paterne !
                    if action.sort("Images/sort/fureur", 648, 582) :
                        time.sleep(2)
                        # Ce déplacement sur le mob pour le taper
                        action.deplacement(648, 582,800, 504)
                        time.sleep(3)
                        # Ce déplace sur la cases juste a coter pour déclancher le piège
                        action.deplacement(751, 521,810, 554)
                        time.sleep(1)
                        # Place le piege 2 PA
                        if action.sort("Images/sort/2pa", 946, 483) :
                            time.sleep(1)
                            # Ce deplace sur le piege a 2 PA
                            action.deplacement(815, 556,966, 476)
                            time.sleep(1)
                            # Place le piege 2 PA
                            if action.sort("Images/sort/2pa", 916, 451) :
                                time.sleep(1)
                                # Ce deplace sur le piege a 2 PA
                                action.deplacement(970, 482,912, 450)
                                # Le combat est fini on peut quitter le combat
                                action.abandonner()
                                nb_combat += 1 
                                nb_combat_win += 1
                            else :
                                action.abandonner()
                                nb_combat_failed += 1
                                nb_combat += 1  # Incrémentez la variable
                        else :
                            action.abandonner()
                            nb_combat_failed += 1
                            nb_combat += 1  # Incrémentez la variable
                    else: # Si le sort Fureur n'est pas présent | Deuxieme Paterne !
                        action.abandonner()
                        nb_combat_failed += 1
                        nb_combat += 1  # Incrémentez la variable
                else:
                    action.abandonner()
                    nb_combat_failed += 1
    # Condition dans le premier paterne si une fisure est présente avant de placer le sort 
    # Condition au T2 si un mob est devant le personnage



if __name__ == '__main__':
    while True:
        print(f"Nombre de combat : {nb_combat}")
        print(f"Nombre de combat réussi : {nb_combat_win}")
        print(f"Nombre de combat fail : {nb_combat_failed}")
        time.sleep(3)
        main()