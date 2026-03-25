
from cx_Freeze import setup, Executable
import sys

# inclure le script et le csv
includefiles = ["script.ps1"]

# Options 
build_exe_options = {
    "packages": ["os", "subprocess", "pandas", "PySimpleGUI4"],
    "include_files": includefiles
}

# Détecter Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI" 

setup(
    name="Scanneur de disque",
    version="1.0",
    description="Scan l'ensemble du disque dur et trie les dossiers volumineux",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)

# python setup.py build