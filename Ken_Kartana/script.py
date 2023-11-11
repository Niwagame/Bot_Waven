from ahk import AHK
import configparser

# Chargez les variables depuis le fichier config.ini
config = configparser.ConfigParser()
config.read('config.ini')
EXECUTABLE_PATH = config['DEFAULT']['EXECUTABLE_PATH']

def hold_click(duration_ms):
    ahk = AHK(executable_path=EXECUTABLE_PATH)
    
    with open("Script/drag.ahk", "r") as file:
        script = file.read().replace('%1%', str(duration_ms))
    
    ahk.run_script(script, blocking=False)

def simple_click(right=False):
    ahk = AHK(executable_path=EXECUTABLE_PATH)
    
    # Choix du script en fonction de la valeur de `right`
    script_file = "Script/simple_click_right.ahk" if right else "Script/simple_click.ahk"
    
    with open(script_file, "r") as file:
        script = file.read()
    
    ahk.run_script(script, blocking=False)
