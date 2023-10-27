import pyautogui
import win32gui
import time
import os

import locate_image
import script

#game_window_coordinates = locate_image.get_game_window_coordinates("Waven") 

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

def deplacement(start_x, start_y, end_x, end_y):
    """Effectue un déplacement lent de la souris d'un point de départ à un point de fin."""

    # Durée du clic en secondes
    clic_duration = 2.0  # par exemple, 2 secondes

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

        script.hold_click(6000)
        # Déplace la souris à la nouvelle coordonnée
        pyautogui.moveTo(x + rect[0], y + rect[1])
    
        # Attendez le délai entre les étapes de déplacement
    time.sleep(step_delay)
    
    # Déplacez la souris à la position de fin
    pyautogui.moveTo(x=rect[0] + end_x, y=rect[1] + end_y,tween=pyautogui.easeInOutQuad)

    # Relâche le clic gauche
    pyautogui.mouseUp()

def attack_loop():
    # Define the game window coordinates and region for detection
    game_window_coordinates = locate_image.get_game_window_coordinates("Waven")   # Placeholder, replace with actual function to get game window coordinates
    detection_region = (376, 328, 800, 410)
    
    while True:  # Keep attacking as long as enemies are detected
        # Step 1: Get the position of the character
        char_image_path = "Images/perso.png"
        char_location = locate_image.detection_images_single(char_image_path, detection_region, game_window_coordinates)
        
        # If character is not detected, exit the function
        if char_location is None:
            print("Character not detected!")
            return
        
        # Extract the character's coordinates
        _, (char_x, char_y, _, _) = char_location
        
        # Step 2: Get the position of all detected enemies
        mob_image_paths = [os.path.join("Images/mob", f) for f in os.listdir("Images/mob")]
        enemies_locations = locate_image.detection_images(mob_image_paths, detection_region, game_window_coordinates)
        
        # If no enemies are detected, call abandon function and break the loop
        if enemies_locations is None:
            abandonner()
            break
        
        # Step 3: Find the closest enemy
        closest_enemy = None
        min_distance = float('inf')
        
        # Adjusting the unpacking of values here
        image_path, box = enemies_locations
        enemy_x, enemy_y, _, _ = box.left, box.top, box.width, box.height
        
        distance = ((char_x - enemy_x) ** 2 + (char_y - enemy_y) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_enemy = (enemy_x, enemy_y)
        
        # Step 4: Perform the attack (move to the enemy using deplacement)
        deplacement(char_x, char_y, closest_enemy[0], closest_enemy[1])


def click_coor(clic_x, clic_y):

        if (0 <= clic_x < rect[2] - rect[0]) and (0 <= clic_y < rect[3] - rect[1]):
            # Attend un court délai avant le clic
            time.sleep(0.5)  # ajustez la valeur du délai au besoin
                
            # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
            pyautogui.click(x=rect[0] + clic_x, y=rect[1] + clic_y,)
            
            script.simple_click()

def click_coor_right(clic_x, clic_y):

        if (0 <= clic_x < rect[2] - rect[0]) and (0 <= clic_y < rect[3] - rect[1]):
            # Attend un court délai avant le clic
            time.sleep(0.5)  # ajustez la valeur du délai au besoin
                
            # Déplace la souris à la coordonnée souhaitée et effectue un clic gauche
            pyautogui.click(x=rect[0] + clic_x, y=rect[1] + clic_y,)
            
            script.simple_click_right()

def abandonner():
    click_coor(32, 902)
    click_coor(177, 817)
    click_coor(745, 508)
