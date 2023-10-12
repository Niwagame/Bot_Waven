import pyautogui
import win32gui
import time
from ahk import AHK
import cv2
import numpy as np

#Zone délimitée : Debut (460, 660) - Largeur: 438, Hauteur: 75

# Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")


# Vérifie si la souris est à l'intérieur de la fenêtre du jeu
rect = win32gui.GetWindowRect(game_window)

def get_game_window_rect(window_name):
    game_window_handle = win32gui.FindWindow(None, window_name)
    if not game_window_handle:
        return None
    return win32gui.GetWindowRect(game_window_handle)

def capture_game_window(window_name):
    rect = get_game_window_rect("Waven")
    if not rect:
        return None
    x, y, x2, y2 = rect
    return pyautogui.screenshot(region=(x, y, x2 - x, y2 - y))

def locate_image_on_screen(image_path, window_name, threshold=0.8):
    screenshot = capture_game_window(window_name)
    if screenshot is None:
        return None
    
    screenshot_np = np.array(screenshot)
    screen_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

    template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
    rect = get_game_window_rect(window_name)
    
    for pt in zip(*loc[::-1]):
        # Ajoutez les coordonnées X et Y de la fenêtre pour obtenir les coordonnées absolues
        return pt[0] + rect[0], pt[1] + rect[1], w, h
    return None



def hold_click(duration_ms):
    #ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\v1.1.37.01\\AutoHotkeyA32.exe')
    ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkeyA32.exe')
    
    with open("Script/drag.ahk", "r") as file:
        script = file.read().replace('%1%', str(duration_ms))
    
    ahk.run_script(script, blocking=False)

def simple_click():
    #ahk = AHK(executable_path='C:\\Program Files\\AutoHotkey\\v1.1.37.01\\AutoHotkeyA32.exe')
    ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkeyA32.exe')
    
    with open("Script/simple_click.ahk", "r") as file:
        script = file.read()
    
    ahk.run_script(script, blocking=False)

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

        simple_click()
        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False

def sort(image_path, clic_x, clic_y):
    # Tente de localiser l'image sur l'écran
    location = locate_image_on_screen(image_path, "Waven")
    
    # Obtient les coordonnées de la fenêtre du jeu
    rect = get_game_window_rect("Waven")
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
        simple_click()
        time.sleep(1)
        simple_click()

        # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
        pyautogui.moveTo(x=rect[0] + clic_x, y=rect[1] + clic_y,)
        time.sleep(1)
        simple_click()

        return True
    else:
        print(f"Image {image_path} non trouvée.")
        return False


def sort_6pa(image_path, click1_coords, click2_coords):
    # Tente de localiser l'image sur l'écran
    location = locate_image_on_screen(image_path,"Waven")
    #location = pyautogui.locateOnScreen(image_path, confidence=0.8, minSearchTime=2)
    
    # Obtient les coordonnées de la fenêtre du jeu
    rect = get_game_window_rect("Waven")
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
        simple_click()  # simule un clic simple
        time.sleep(1)
        simple_click()  # simule un autre clic simple

        # Déplace la souris à la première position spécifiée et effectue un clic
        pyautogui.moveTo(x=rect[0] + click1_coords[0], y=rect[1] + click1_coords[1],)
        time.sleep(1)

        # Déplace la souris à la seconde position spécifiée et effectue un clic
        pyautogui.moveTo(x=rect[0] + click2_coords[0], y=rect[1] + click2_coords[1],)
        simple_click()
        time.sleep(1)

        return True
    else:
        print(f"Image {image_path} non trouvée.")
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

        hold_click(5000)
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
            
            simple_click()

def abandonner():
    click_coor(31,729)
    click_coor(150,650)
    click_coor(615,415)

