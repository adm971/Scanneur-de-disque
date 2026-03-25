# Scanneur-de-disque
Un programme python qui utilise powershell pour scanner l'ensemble des dossiers présents sur le disque système et les trier en fonction de leur taille 

J'ai créé ce programme car je cherchais à comprendre pourquoi mon SSD principal était constamment presque saturé malgré avoir déplacé tous les logiciels, jeux, et 
dossiers volumineux sur mon deuxième SSD 
étant donné que l'explorateur de dossier de Windows ne me plait pas j'ai décidé de combiner Powershell et Python afin de découvrir ce qui pouvait occuper encore tant de place sur mon disque 


# Installation

## 1. Cloner le projet

git clone https://github.com/adm971/fonctions.git


---

# Installation sur Windows

1. Installer Python depuis :
https://www.python.org/downloads/

2. Installer cx_Freeze :

python -m pip install cx_Freeze

3. Compiler le programme :

python setup.py build

4. Lancer le programme :

un dossier "build" sera créé avec un sous dossier "exe.win" dans le quel se trouve "main.exe"
Lancer main.exe
