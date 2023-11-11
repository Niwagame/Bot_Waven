import win32gui
import time
import keyboard

import script
import action
import locate_image

nb_combat = 0
nb_combat_failed = 0
nb_combat_win = 0

#pyinstaller --onefile bot_waven.py --add-data "Images/*;Images" --add-data "Script/*;Script" --distpath ./output --hidden-import script

def suite():
    global nb_combat 
    global nb_combat_failed
    global nb_combat_win

    

    game_window_coordinates = locate_image.get_game_window_coordinates("Waven")



    keyboard.press_and_release('space')  #Passe sont tour
    time.sleep(13)
    if action.sort("Images/sort/fureur", 648, 582) : # Si le sort Fureur est présent alors il ce le met | Premier paterne !
        time.sleep(1)
        action.deplacement(648, 582,800, 504) # Ce déplacement sur le mob pour le taper
        time.sleep(3)
        action.deplacement(751, 521,810, 554) # Ce déplace sur la cases juste a coter pour déclancher le piège
        if locate_image.detection_images_count("Images/sort/2pa", (497, 813, 615, 117), game_window_coordinates) >= 2 :
            action.sort("Images/sort/2pa", 946, 483) # Place le piege 2 PA
            time.sleep(2)
            action.deplacement(815, 556,966, 476) # Ce deplace sur le piege a 2 PA
            if action.sort("Images/sort/2pa", 916, 451) : # Place le piege 2 PA
                time.sleep(1)
                action.deplacement(970, 482,912, 450) # Ce deplace sur le piege a 2 PA
                action.abandonner() # Le combat est fini on peut quitter le combat
                nb_combat += 1 
                nb_combat_win += 1
        else :
            action.sort("Images/sort/4pa", 791, 502)
            time.sleep(2)
            keyboard.press_and_release('space') #Passe son tour
            time.sleep(8)
            if locate_image.detection_mob("Images/mob.png", (810, 455, 100, 110), game_window_coordinates) : # Si le mob est a gauche
                action.sort("Images/sort/2pa", 862, 479)
                time.sleep(2)
                action.deplacement_2step(803, 555, 852, 533, 797, 501)
                time.sleep(2)
                action.deplacement(811, 503,870, 474)
                time.sleep(2)
                if action.sort("Images/sort/2pa", 802, 501) : # On place le sort 2PA
                    action.deplacement(859, 480,802, 501)
                    action.abandonner() # Le combat est fini on peut quitter le combat
                    nb_combat += 1 
                    nb_combat_win += 1
                else : # Si le sort 2 PA pas présent alors on place le sort 4PA 
                    action.sort("Images/sort/4pa", 802, 501)
                    action.deplacement(859, 480,802, 501)
                    action.abandonner() # Le combat est fini on peut quitter le combat
                    nb_combat += 1 
                    nb_combat_win += 1
            else:
                action.sort("Images/sort/2pa", 859, 531) # Place le sort 2 PA
                action.deplacement(813, 557,914, 506) # Tape le mob en face
                time.sleep(3)
                action.deplacement(866, 533,804, 503)
                if action.sort("Images/sort/2pa", 865, 536) :
                    time.sleep(3)
                    action.deplacement(804, 493,856, 537)
                    action.abandonner()
                    nb_combat += 1 
                    nb_combat_win += 1
                else :
                    action.sort("Images/sort/4pa", 865, 536)
                    time.sleep(3)
                    action.deplacement(804, 493,856, 537)
                    action.abandonner()
                    nb_combat += 1 
                    nb_combat_win += 1
    else: # Si le sort Fureur n'est pas présent | Deuxieme Paterne !
        action.deplacement(648, 582,861, 532)
        time.sleep(3)
        action.deplacement(813, 561,741, 527)
        time.sleep(2)
        action.sort("Images/sort/2pa", 807, 559)
        time.sleep(3)
        action.deplacement(756, 516,807, 559)
        time.sleep(3)
        action.sort("Images/sort/4pa", 791, 502)
        time.sleep(2)
        keyboard.press_and_release('space') #Passe son tour
        time.sleep(8)
        if locate_image.detection_mob("Images/mob.png", (810, 455, 100, 110), game_window_coordinates) : # Si le mob est a gauche
            action.sort("Images/sort/2pa", 862, 479)
            time.sleep(2)
            action.deplacement_2step(803, 555, 852, 533, 797, 501)
            time.sleep(2)
            action.deplacement(811, 503,870, 474)
            time.sleep(2)
            if action.sort("Images/sort/2pa", 802, 501) : # On place le sort 2PA
                action.deplacement(859, 480,802, 501)
                action.abandonner()
                nb_combat += 1 
                nb_combat_win += 1
            else : # Si le sort 2 PA pas présent alors on place le sort 4PA 
                action.sort("Images/sort/4pa", 802, 501)
                action.deplacement(859, 480,802, 501)
                action.abandonner()
                nb_combat += 1 
                nb_combat_win += 1
        else:
            action.sort("Images/sort/2pa", 859, 531) # Place le sort 2 PA
            action.deplacement(813, 557,914, 506) # Tape le mob en face
            time.sleep(3)
            action.deplacement(866, 533,804, 503)
            if action.sort("Images/sort/2pa", 865, 536) :
                time.sleep(3)
                action.deplacement(804, 493,856, 537)
                action.abandonner()
                nb_combat += 1 
                nb_combat_win += 1
            else :
                action.sort("Images/sort/4pa", 865, 536)
                time.sleep(3)
                action.deplacement(804, 493,856, 537)
                action.abandonner()
                nb_combat += 1 
                nb_combat_win += 1


def main():
    
    game_window = win32gui.FindWindow(None, "Waven") # Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
    win32gui.SetForegroundWindow(game_window) # Activer la fenêtre du jeu

    if action.move_mouse_to_image("Images/bullpnj.png"): # Appel de la fonction pour déplacer la souris sur l'image du PNJ et utiliser F6
        if action.move_mouse_to_image("Images/quete.png"): # Appel de la fonction pour déplacer la souris sur l'image de la quête et utiliser F6
                #CLique sur jouer
                action.click_coor(812, 846)
                #Attend que le jeux charge
                time.sleep(5)
                #Place le personnage a la bonne 
                action.deplacement(484, 503, 646, 586)

                #Place le sort a 6 PA
                if action.sort_6pa("Images/sort/6pa",(758, 533), (797, 560)):
                    time.sleep(2)
                    suite()
                else: #Si le sort 6 PA est pas présent
                    if action.sort_single("Images/sort/4pa/sort2-4pa-vert.png", 758, 533) : #On place le sort 4PA vert
                        action.sort("Images/sort/2pa", 797, 560)
                        time.sleep(2)
                        suite()
                    else: # Si le sort 4PA vert est pas présent alors on place 2 sort PA
                        action.sort("Images/sort/2pa", 758, 533)
                        action.sort("Images/sort/2pa", 797, 560)
                        time.sleep(2)
                        suite()
    else:
        keyboard.press_and_release('esc')


if __name__ == '__main__':
    while True:
        print(f"Nombre de combat : {nb_combat}")
        print(f"Nombre de combat réussi : {nb_combat_win}")
        print(f"Nombre de combat fail : {nb_combat_failed}")
        time.sleep(3)
        main()