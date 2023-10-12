import win32gui
import pyautogui

# Obtient le handle de la fenêtre du jeu (remplacez "NomDuJeu" par le nom de la fenêtre du jeu)
game_window = win32gui.FindWindow(None, "Waven")

while True:
    # Obtient la position actuelle de la souris à l'écran
    x, y = pyautogui.position()
    
    # Convertit les coordonnées en coordonnées relatives à la fenêtre du jeu
    rect = win32gui.GetWindowRect(game_window)
    x_rel = x - rect[0]
    y_rel = y - rect[1]
    
    # Vérifie si la souris est à l'intérieur de la fenêtre du jeu
    if (0 <= x_rel < rect[2] - rect[0]) and (0 <= y_rel < rect[3] - rect[1]):
        # Affiche la position relative dans la fenêtre du jeu en temps réel
        print(f"Position (x, y) dans la fenêtre du jeu : ({x_rel}, {y_rel})")
