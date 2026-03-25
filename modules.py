import PySimpleGUI4 as sg 
import pandas as pd 
import os, csv, subprocess


path = "dossiers.csv"
path2 = "sousdoss.csv"

# Exécuter le script powershell
def launch_script() :
    print("EXECUTION DU SCRIPT POWERSHELL")
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", "script.ps1"
    ])
    print("FINI")
    finished = True 
    if finished :
        print("la variable finished est vérifiée et retournée")
        return finished



# Lire le CSV qui contient les résultats du scan
def read_analysis(path):
    if os.path.exists(path):
        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                print(f"Chemin: {row['Path']} | Taille(Go): {row['SizeGB']}")
    else:
        print(f"Le fichier {path} n'existe pas")



# Convertir les CSV en DataFrame pour afficher dans PySimpleGUI
def to_dataframe(p, txt) :
    df = pd.read_csv(p)
    df = df.sort_values(by="SizeGB", ascending=False)
    data = df.values.tolist()
    headings = list(df.columns)


    layout = [
        [sg.Text(txt)],
        [sg.Table(
            values=data,
            headings=headings,
            auto_size_columns=True,
            display_row_numbers=False,
            justification='left',
            num_rows=20,
            key='-TABLE-',
            enable_events=True
        )],
        
        [sg.Button("Quitter")]
    ]
    return layout

txt1 = "classement des dossiers les plus volumineux trouvés parmis le système"
txt2 = "classement des sous-dossiers les plus volumineux trouvés parmis les 3 dossiers les plus volumineux du système"

def run():
    if os.path.exists(path):
        window = sg.Window("Analyse des dossiers", to_dataframe(path, txt1) + to_dataframe(path2, txt2), resizable=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Quitter":
                break
        window.close()
    else : 
        print("résultats introuvables \néxécution du script")
        launch_script()
        print("éxécution récursive de la fonction run()")
        run()
