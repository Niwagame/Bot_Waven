import pyautogui
import win32gui
import cv2
import os

from ahk import AHK
import numpy as np



SEARCH_REGION = (398, 653, 585, 95)

# Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")


# Vérifie si la souris est à l'intérieur de la fenêtre du jeu
rect = win32gui.GetWindowRect(game_window)



def get_game_window_rect(window_name):
    game_window_handle = win32gui.FindWindow(None, window_name)
    if not game_window_handle:
        return None
    return win32gui.GetWindowRect(game_window_handle)

def capture_game_window_with_region(window_name, region=None):
    rect = get_game_window_rect(window_name)
    if not rect:
        return None
    x, y, x2, y2 = rect
    if region:
        x += region[0]
        y += region[1]
        x2 = x + region[2]
        y2 = y + region[3]
    return pyautogui.screenshot(region=(x, y, x2 - x, y2 - y))


def locate_image_on_screen(image_path, window_name, threshold=0.8, region=None):
    screenshot = capture_game_window_with_region(window_name, region)
    if screenshot is None:
        return None
    
    screenshot_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if template is None:  # Ajout de la gestion des erreurs ici
        print(f"Erreur lors du chargement de l'image: {image_path}")
        return None
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    #res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCORR_NORMED)
    loc = np.where(res >= threshold)
    
    rect = get_game_window_rect(window_name)
    
    for pt in zip(*loc[::-1]):
        # Ajoutez les coordonnées X et Y de la fenêtre pour obtenir les coordonnées absolues
        return pt[0] + rect[0], pt[1] + rect[1], w, h
    return None

def locate_images_in_directory(directory_path, window_name, threshold=0.8):
    # Liste tous les fichiers dans le dossier
    files = os.listdir(directory_path)
    for file in files:
        # Construisez le chemin complet vers le fichier
        image_path = os.path.join(directory_path, file)
        # Essayez de trouver le fichier sur l'écran
        location = locate_image_on_screen(image_path, window_name, threshold)
        if location is not None:
            # Si vous trouvez une correspondance, retournez les coordonnées et le chemin de l'image
            return location, image_path
    # Si aucune image n'est trouvée, retournez None
    return None, None
