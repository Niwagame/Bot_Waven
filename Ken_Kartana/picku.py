from typing import Tuple
import pyautogui
import win32gui
import time
import numpy as np
from ahk import AHK


# Clic gauche souris
def click_left():
    ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkeyA32.exe')
    with open("ScriptAHK/mouseclickleft.ahk", "r") as file:
        script = file.read()
    ahk.run_script(script, blocking=False)

# Clic droit souris
def click_right():
    ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkeyA32.exe')
    with open("ScriptAHK/mouseclickright.ahk", "r") as file:
        script = file.read()
    ahk.run_script(script, blocking=False)


def get_game_window_coordinates(window_title: str) -> Tuple[int, int, int, int]:
    # Obtient le handle de la fenêtre
    hwnd = win32gui.FindWindow(None, window_title)
    if hwnd:
        return win32gui.GetWindowRect(hwnd)
    else:
        return None, None, None, None

def detection_images(image_path, region: Tuple[int, int, int, int], game_window_coordinates, click_type = 'left'):
    # Convertit les coordonnées de la région relative à la fenêtre en coordonnées absolues
    absolute_region = (
        game_window_coordinates[0] + region[0],
        game_window_coordinates[1] + region[1],
        region[2],
        region[3]
    )

    location = pyautogui.locateOnScreen(image_path, step=5, region=absolute_region, confidence=0.8, minSearchTime=2)

    if location is not None:
         # Récupère les coordonnées du centre de l'image
        x, y, width, height = location
        center_x = x + width // 2
        center_y = y + height // 2

        # Déplace la souris sur le centre de l'image
        pyautogui.click(center_x, center_y, clicks=1)
        time.sleep(1)
        
        # Clic gauche ou droit en fonction de click_type
        if click_type == 'left':
            click_left()
        elif click_type == 'right':
            click_right()
    else:
        print(f"Image {image_path} non trouvée.")

def show_region(region: Tuple[int, int, int, int], game_window_coordinates):
    absolute_region = (
        game_window_coordinates[0] + region[0],
        game_window_coordinates[1] + region[1],
        region[2],
        region[3]
    )
    screenshot = pyautogui.screenshot(region=absolute_region)
    screenshot.show()

window_title = "Waven"
game_window_coordinates = get_game_window_coordinates(window_title)

if None not in game_window_coordinates:
    # Active la fenêtre au premier plan
    win32gui.SetForegroundWindow(win32gui.FindWindow(None, window_title))

    # Ressources avant première salle
    image_pnj_path = "Images/positions/PNJvamp.png"
    image_quete_path = "Images/positions/quetevampyre.png"
    image_jouer_path = "Images/positions/jouerbutton.png"
    image_fleche_path = "Images/positions/tinyarrow1.png"
    image_mob_path = "Images/mobs/MS1Vampyre1.png"

    # Détection de l'action puis affichage de la zone (remplacer l'affichage par la gestion du clic)
    detection_images(image_pnj_path, region=(0, 0, 1600, 900), game_window_coordinates=game_window_coordinates, click_type = 'left') # trouvée
    #show_region((0, 0, 1600, 900), game_window_coordinates=game_window_coordinates) # bonne range (prend la barre blanche)

    detection_images(image_quete_path, region=(0, 0, 1600, 900), game_window_coordinates=game_window_coordinates, click_type = 'left') # trouvée
    #show_region((890, 240, 150, 150), game_window_coordinates=game_window_coordinates) # bonne range
    
    detection_images(image_jouer_path, region=(680, 750, 250, 130), game_window_coordinates=game_window_coordinates, click_type = 'left') # trouvée
    #show_region((680, 750, 250, 130), game_window_coordinates=game_window_coordinates) # bonne range
    
    detection_images(image_fleche_path, region=(920, 380, 100, 100), game_window_coordinates=game_window_coordinates, click_type = 'right')# trouvée
    #show_region((920, 380, 100, 100), game_window_coordinates=game_window_coordinates) # bonne range
    
    detection_images(image_mob_path, region=(820, 340, 200, 200), game_window_coordinates=game_window_coordinates, click_type = 'left') # trouvée
    #show_region((820, 340, 200, 200), game_window_coordinates=game_window_coordinates) # bonne range

else:
    print("Fenêtre de jeu non trouvée.")
