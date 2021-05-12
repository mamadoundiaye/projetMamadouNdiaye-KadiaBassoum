"""un environnement virtuel peut etre decrit comme un repertoire d'installation
isolés ,  et cela nous permet de gerer les dependances et de pouvoir gerer et travailler dans differentes
version , python , dans notre exemple

on a plusieurs facons d'en creer pour python


VIRTUALENV

1: on l'install avec la commande
pip install virtualenv
2: apres l'installation reussie ,  on cree un environnement avec la commande suivante 

virtualenv --python=/usr/bin/python2.7 my-env

ici la path vers la version de python a utiliser est specifié
et le nom de l'environnement virtuell aussi

3:activation , avant de pouvoir utiliser notre environnement virtuel , on l'active avec la commande suivante

source my-env/bin/activate

3 desactive :
desactivate
4 pour supprimer on efface le dossier


CONDA 

1 :
conda create --name my-env python = vesion_de_python


2: 
conda info --envs #afficher les environnements virtuels
source activate my-env #activer un env virtuel

3:
source desactivate #pour la desactivation

4 
conda remove --name my-env #pour supprimer 

les autres questions , voir images


"""