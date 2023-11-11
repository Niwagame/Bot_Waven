import win32gui
import time
import keyboard

import script
import action
import locate_image

def main():
    
    game_window = win32gui.FindWindow(None, "Waven") # Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
    win32gui.SetForegroundWindow(game_window) # Activer la fenêtre du jeu
    game_window_coordinates = locate_image.get_game_window_coordinates("Waven")

    if action.move_mouse_to_image("Images/bullpnj.png"): # Appel de la fonction pour déplacer la souris sur l'image du PNJ 
        if action.move_mouse_to_image("Images/quete.png"): # Appel de la fonction pour déplacer la souris sur l'image de la quête
                
            action.click_coor(812, 846) #Clique sur jouer
            time.sleep(3) #Attend l'entrer dans le donjon
            action.click_coor(969, 430,right=True) # Clique sur la flèche
            time.sleep(1) #Attend l'entrer dans la salle
            action.click_coor(902, 478)# Clique sur le group de mob
            time.sleep(7) #Attend que le jeux charge
            action.deplacement(649, 582, 809, 506) #Place le personnage a la bonne position
            # T1
            if action.sort_6pa("Images/sort/6pa",(853, 475), (755, 534)): # Place le sort 6 PA si il est présent
                keyboard.press_and_release('space')  #Passe sont tour
            elif action.sort("Images/sort/4pa", 853, 475) : # Sinon place le sort 4 PA si il est présent
                action.sort("Images/sort/2pa", 755, 534) # Et on place le sort 2 PA
                keyboard.press_and_release('space')  #Passe sont tour
            else :
                action.sort("Images/sort/2pa", 853, 475) # Sinon place le sort 2 PA
                action.sort("Images/sort/2pa", 755, 534) # Place le sort 2 PA
                keyboard.press_and_release('space')  #Passe sont tour


            # T2
            if action.sort("Images/sort/fureur", 809, 505) : # Place le sort Fureur sur le personnage
                if locate_image.detection_images_count("Images/sort/2pa", (497, 813, 615, 117), game_window_coordinates) >= 2 : # On verifie si on a 2 sort 2 PA ou plus
                    action.deplacement(809, 505,803, 450) # On ce déplace pour taper le Cristalroc
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 802, 508) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(861, 483,805, 510) # On ce déplace sur le sort 2 PA
                    time.sleep(1)
                    action.deplacement(802, 505,758, 530) # On ce déplace sur le sort 2 PA
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 759, 536) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(759, 536,759, 536) # On ce déplace le sort 2 PA
                    time.sleep(1)
                    action.abandonner() # On quitte le combat
                    time.sleep(2)
                    action.exit_dj() # On quitte le DJ
                else :
                    action.sort("Images/sort/trappesort", 754, 535) # Place le sort trappe sur le piège derrère
                    action.deplacement(809, 505,803, 450) # On ce déplace pour taper le Cristalroc
                    time.sleep(1)
                    action.sort("Images/sort/trappe", 802, 508) # Place le sort trappe 
                    time.sleep(1)
                    action.deplacement(861, 483,805, 510) # On ce déplace sur le sort 2 PA
                    time.sleep(1)
                    action.deplacement(802, 505,758, 530) # On ce déplace sur le sort 2 PA
                    action.sort("Images/sort/2pa", 759, 536) # On place le sort 2 PA
                    action.deplacement(759, 536,759, 536) # On ce déplace le sort 2 PA
                    time.sleep(1)
                    action.abandonner() # On quitte le combat
                    time.sleep(2)
                    action.exit_dj() # On quitte le DJ
            elif locate_image.detection_images_count("Images/sort/2pa", (497, 826, 621, 99), game_window_coordinates) >= 3 :
                    action.deplacement(809, 505,803, 450) # On ce déplace pour taper le Cristalroc
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 819, 510) # On place le sort 2 PA
                    action.deplacement(861, 483,805, 510) # On ce déplace sur le sort 2 PA
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 855, 482) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(809, 505,853, 483) # On ce déplace sur le sort 2 PA.
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 811, 499) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(853, 483,811, 499) # On ce déplace le sort 2 PA
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 855, 482) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(809, 505,853, 483) # On ce déplace sur le sort 2 PA.
                    action.abandonner() # On quitte le combat
                    time.sleep(2)
                    action.exit_dj() # On quitte le DJ
            else :
                    action.sort("Images/sort/trappesort", 754, 535) # Place le sort trappe sur le piège derrère
                    action.deplacement(809, 505,803, 450) # On ce déplace pour taper le Cristalroc
                    time.sleep(1)
                    action.sort("Images/sort/trappe", 802, 508) # Place le sort trappe 
                    time.sleep(1)
                    action.deplacement(861, 483,805, 510) # On ce déplace sur le sort 2 PA
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 856, 477) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(799, 506,860, 488) # On ce déplace sur le sort 2 PA
                    time.sleep(1)
                    action.sort("Images/sort/2pa", 813, 506) # On place le sort 2 PA
                    time.sleep(1)
                    action.deplacement(867, 490,813, 506) # On ce déplace le sort 2 PA
                    time.sleep(1)
                    action.abandonner() # On quitte le combat
                    time.sleep(2)
                    action.exit_dj() # On quitte le DJ
    else:
         action.abandonner() # Si il trouve pas la bull le perso doit être toujours dans le DJ donc on quitte 



if __name__ == '__main__':
    main()