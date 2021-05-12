import os.path
import glob


def count_nb_lines_mod(the_path) :
    import os.path
    import glob
    with open(the_path) as f :
        text = f.read()
        nbre_lignes = 0
        new_text = text.split("\n")
        for i in new_text: 
            if len(i) != 0 and (i.startswith("#") == False ):
                nbre_lignes += 1                                  
        return nbre_lignes



def count_nb_lines_mod(the_path) :
    with open(the_path) as f :
        text = f.read()
        nbre_lignes = 0
        new_text = text.split("\n")
        for i in new_text: 
            if len(i) != 0 and (i.startswith("#") == False ):
                nbre_lignes += 1                                  
        return nbre_lignes



import os.path
import glob
def get_modules(the_path) :
    os.chdir(the_path)
    fichier_py = glob.glob(r"*.py*")
    return fichier_py
    


def get_packages(the_path) :
    os.chdir(the_path)
    fichier_all = glob.glob(r"**")
    sous_dossiers = []
    for i in fichier_all :
        if '.' not in i :
            sous_dossiers.append(i)
    return sous_dossiers
    


def get_all_modules(the_path) :
    all_modules = [get_modules(the_path)]
    parcours = get_packages(the_path)
    for mods in parcours :
        all_modules.append(get_modules(mods))
    return all_modules
    


def count_nb_lines_paquet(the_path) :
    esp = '\ '#utile pour faire un append au path
    all_modules = [get_modules(the_path)] #recupere les modules du repertoire actuel
    parcours = get_packages(the_path) #recupere les sous repertoires
    comp1 = 0 #compteur nombre de lignes dans la racine du repertoire
    comp2 = 0 #compteur nombre de lignes dans les sous repertoire
    
    #premiere boucle for pour les lignes de codes dans les modules des sous repertoires
    for mods in parcours :
        if len(get_all_modules(the_path+esp[0]+mods)) != 0  :
            for  i in get_all_modules(the_path+esp[0]+mods) :
                comp1 += count_nb_lines_mod(the_path+esp[0]+mods+esp[0]+i[0]) 
                
    #premiere boucle for pour les lignes de codes dans les modules du repertoire actuel
    for mod in all_modules :
        for fichiers_py in mod :
            comp2 += count_nb_lines_mod(the_path+esp[0]+fichiers_py)
        
    return  comp1 + comp2 #nombre total de lignes 








