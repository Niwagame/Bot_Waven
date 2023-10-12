import pyautogui
import win32gui
import time
import os

from ahk import AHK


import locate_image
import script

SEARCH_REGION = (398, 653, 585, 95)
# Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")


# Vérifie si la souris est à l'intérieur de la fenêtre du jeu
rect = win32gui.GetWindowRect(game_window)

# Fonction pour déplacer la souris sur une image et effectuer un clic avec la touche F6
def move_mouse_to_image(image_path):
    # Tente de localiser l'image sur l'écran
    location = pyautogui.locateOnScreen(image_path, confidence=0.8, minSearchTime=2)

    if location is not None:
        # Récupère les coordonnées du centre de l'image
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image
        pyautogui.click(center_x, center_y, clicks=3)

        time.sleep(2)

        script.simple_click()
        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False


def sort(directory_path, clic_x, clic_y):
    # Tente de localiser une des images sur l'écran
    location, image_path = locate_image.locate_images_in_directory(directory_path, "Waven")

    #location, image_path = locate_images_in_directory(directory_path, "Waven")

    # Obtient les coordonnées de la fenêtre du jeu
    rect = locate_image.get_game_window_rect("Waven")
    if not rect:
        print("Fenêtre de jeu non trouvée.")
        return False

    if location is not None:
        # Récupère les coordonnées du centre de l'image
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image
        pyautogui.moveTo(center_x, center_y,)
        time.sleep(2)
        script.simple_click()
        time.sleep(1)
        script.simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=rect[0] + clic_x, y=rect[1] + clic_y,)
        time.sleep(1)
        script.simple_click()

        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False

def sort_boost(image_path, clic_x, clic_y):
    # Tente de localiser l'image sur l'écran
    location = locate_image.locate_image_on_screen(image_path, "Waven")
    
    # Obtient les coordonnées de la fenêtre du jeu
    rect = locate_image.get_game_window_rect("Waven")
    if not rect:
        print("Fenêtre de jeu non trouvée.")
        return False

    if location is not None:
        # Récupère les coordonnées du centre de l'image
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image
        pyautogui.moveTo(center_x, center_y,)
        time.sleep(2)
        script.simple_click()
        time.sleep(1)
        script.simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=rect[0] + clic_x, y=rect[1] + clic_y,)
        time.sleep(1)
        script.simple_click()

        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False

def sort_6pa(directory_path, click1_coords, click2_coords):
    # Tente de localiser l'image sur l'écran
    location, image_path = locate_image.locate_images_in_directory(directory_path, "Waven")
    #location = pyautogui.locateOnScreen(image_path, confidence=0.8, minSearchTime=2)
    
    # Obtient les coordonnées de la fenêtre du jeu
    rect = locate_image.get_game_window_rect("Waven")
    if not rect:
        print("Fenêtre de jeu non trouvée.")
        return False

    if location is not None:
        # Récupère les coordonnées du centre de l'image
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image et effectue des clics
        pyautogui.moveTo(center_x, center_y,)
        time.sleep(2)
        script.simple_click()  # simule un clic simple
        time.sleep(1)
        script.simple_click()  # simule un autre clic simple

        # Déplace la souris à la première position spécifiée et effectue un clic
        pyautogui.moveTo(x=rect[0] + click1_coords[0], y=rect[1] + click1_coords[1],)
        time.sleep(1)

        # Déplace la souris à la seconde position spécifiée et effectue un clic
        pyautogui.moveTo(x=rect[0] + click2_coords[0], y=rect[1] + click2_coords[1],)
        script.simple_click()
        time.sleep(1)

        return True
    else:
        print(f"Images dans {directory_path} non trouvées.")
        return False

def deplacement(start_x, start_y, end_x, end_y):
    """Effectue un déplacement lent de la souris d'un point de départ à un point de fin."""

    # Durée du clic en secondes
    clic_duration = 5.0  # par exemple, 2 secondes

    # Nombre d'étapes de déplacement
    num_steps = 15 # Augmentez ce nombre pour un déplacement plus lent

    # Calcule le délai entre chaque étape de déplacement
    step_delay = clic_duration / num_steps
    
    # Déplace la souris à la position de départ
    pyautogui.moveTo(x=rect[0] + start_x, y=rect[1] + start_y,)

    # Effectue le déplacement lent vers la position de fin
    for step in range(num_steps):
        # Calcule les nouvelles coordonnées intermédiaires
        x = int(start_x + (end_x - start_x) * (step / num_steps))
        y = int(start_y + (end_y - start_y) * (step / num_steps))

        script.hold_click(5000)
        # Déplace la souris à la nouvelle coordonnée
        pyautogui.moveTo(x + rect[0], y + rect[1])
    
        # Attendez le délai entre les étapes de déplacement
    time.sleep(step_delay)
    
    # Déplacez la souris à la position de fin
    pyautogui.moveTo(x=rect[0] + end_x, y=rect[1] + end_y,tween=pyautogui.easeInOutQuad)

    # Relâche le clic gauche
    pyautogui.mouseUp()

def click_coor(clic_x, clic_y):

        if (0 <= clic_x < rect[2] - rect[0]) and (0 <= clic_y < rect[3] - rect[1]):
            # Attend un court délai avant le clic
            time.sleep(0.5)  # ajustez la valeur du délai au besoin
                
            # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
            pyautogui.click(x=rect[0] + clic_x, y=rect[1] + clic_y,)
            
            script.simple_click()


def abandonner():
    click_coor(31,729)
    click_coor(150,650)
    click_coor(615,415)