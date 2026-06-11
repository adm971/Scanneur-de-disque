# Scanneur-de-disque
Un programme python qui utilise powershell pour scanner l'ensemble des dossiers présents sur le disque système et les trier en fonction de leur taille 

J'ai créé ce programme car je cherchais à comprendre pourquoi mon SSD principal était constamment presque saturé malgré avoir déplacé tous les logiciels, jeux, et 
dossiers volumineux sur mon deuxième SSD 
étant donné que l'explorateur de dossier de Windows ne me plait pas j'ai décidé de combiner Powershell et Python afin de découvrir ce qui pouvait occuper encore tant de place sur mon disque 

Prochaines fonctionnalités à venir : 

-Compatibilité Linux 

-Recherche plus approfondie(et donc plus longue) des sous-dossiers volumineux 

-Cliquer sur un chemin affiché par le programme pour l'ouvrir directement dans l'explorateur de fichier ou le terminal 

-Pouvoir supprimmer des chemins depuis le programme


# Installation

## 1. Prérequis
Installer Python 

Installer pip

## 2. Lancer le programme

git clone https://github.com/adm971/Scanneur-de-disque.git

cd Scanneur-de-disque 

pip install -r requirements.txt

python main.py
