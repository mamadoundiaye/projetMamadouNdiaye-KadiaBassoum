# fonction pour creer une base de donnees
def create_connection(db_name):
    import sqlite3
    from sqlite3 import Error

    """ fonction pour creer la base de donnees
    :param db_name: le nom de la base de donnees
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)

    return conn


# fonction pour creer la table DIC
def create_table_db():
    conn = create_connection(r"dic-database.db")
    table_dic = """ CREATE TABLE IF NOT EXISTS DIC1 (
                                        id_ept integer ,
                                        nom text ,
                                        prenom text ,
                                        departement text,
                                        niveau text ,
                                        telephone text
                                    ); """
    try:
        c = conn.cursor()
        c.execute(table_dic)
    except Error as e:
        print(e)



# fonction pour peupler la table DIC dans la base de donnees dic_database
def save_db(id_ele, nom_ele, prenom_el, departement_el, niveau_el, telephone_el):
    conn = create_connection(r"dic-database.db")
    donnees_ele = """ INSERT  INTO  DIC1(
                                        id_ept ,
                                        nom ,
                                        prenom ,
                                        departement ,
                                        niveau ,
                                        telephone
                                    )VALUES(
                                    ?,
                                    ? ,
                                    ? ,
                                    ? ,
                                    ? ,
                                    ? ) ; """
    c = conn.cursor()
    c.execute(donnees_ele , (id_ele, nom_ele, prenom_el, departement_el, niveau_el, telephone_el))
    conn.commit()
    return c.lastrowid


# fonction pour supprimer un enregistrement
def delete_db(id_ele):
    conn = create_connection(r"dic-database.db")
    donnees_ele = """ DELETE FROM DIC1 WHERE id_ept = ? ; """

    c = conn.cursor()
    c.execute(donnees_ele, (id_ele, ))
    conn.commit()
    


# qui permet de recupérer (sous forme d’un dictionnaire)
#dans la table DIC quelques informations d’un élève-ingénieur en DIC
def get_db(id_ele , *positions_id_a_recup):
    #ici on precise en plus de l'id de l'eleve la position des informations dans la table
    conn = create_connection(r"dic-database.db")
    for i in positions_id_a_recup  :
        if  i not in range(5):
               raise ValueError("la donnee n'est pas un attribut")
    c = conn.cursor()
    c.execute("""select * from DIC1 where id_ept = ?""" , id_ele)
    lignes = c.fetchone()
    
    dict_eleves = {key:value for (key,value) in (enumerate(lignes))}
    infos_requises = [ ]
    for i in positions_id_a_recup :
        infos_requises.append(dict_eleves[int(i)])
    infos_requises = {key:value for (key,value) in (enumerate(infos_requises))}
    
    
    return infos_requises



def get_all_db():
    conn = create_connection(r"dic-database.db")
  

    c = conn.cursor()
    c.execute("SELECT * FROM DIC1")
    
    lignes = c.fetchall()
    dict_eleves = {key:value for (key,value) in (enumerate(lignes))}
    
    return dict_eleves


#create_table_db()


#save_db(2, 'ndiaye', 'omar', 'git', 'DIC1', '785009876')


#save_db(1, 'ndiaye', 'Mamadou', 'git', 'DIC1', '785235415')


#delete_db(2)


#save_db(4, 'sene', 'mbaye', 'git', 'DIC1', '778909876')


#modifier_db('DIOP' , 'DIARRA' , 'GIT' , 'DIC1' , '779765432' , 1)


#get_all_db()


#get_db('1' , 0,1 , 2,3 )

#ci dessus les requetes deja executés dans la base de donnees



