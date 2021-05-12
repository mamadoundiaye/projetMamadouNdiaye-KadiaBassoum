import numpy as np
class Polynome() :
    import numpy as np
    
    def __init__(self , coefs):
        if isinstance(coefs , (list,tuple)) == True :
            self.coefs = coefs
            
    def __repr__(self):
                pol = '' #initialisation par une chaine de caractere vide
                #boucle tres long pour gerer les contraintes d'affichage les zeros non affichés etc...
                for coef in range(len(self.coefs)) :
                    degre = (len(self.coefs)-1) - coef 
                    if self.coefs[coef] > 0:
                        if degre > 1  and degre != (len(self.coefs)-1):
                            pol +=  '+'+str(self.coefs[coef])+'x^'+str(degre)
                        elif degre == 1  :
                            if self.coefs[coef] != 1 :
                                if len(self.coefs) == 2 :
                                    pol += str(self.coefs[coef])+'x'
                                else :
                                    pol += '+'+str(self.coefs[coef])+'x'
                            else : 
                                if len(self.coefs) == 2 :
                                    pol += 'x'
                                else :
                                    pol += '+'+'x'
                        elif degre == 0 :
                            if len(self.coefs) == 1 :
                                pol += str(self.coefs[coef]) 
                            else :
                                pol += '+'+str(self.coefs[coef])
                        else : 
                            pol +=  str(self.coefs[coef])+'x^'+str(degre)
                    elif self.coefs[coef] < 0:
                        if degre > 1 :
                            if self.coefs[coef] != -1 :
                                pol +=  '-'+str(np.abs(self.coefs[coef]))+'x^'+str(degre)
                            else :
                                pol += '-'+'x^'+str(degre)
                        elif degre == 1 :
                            if self.coefs[coef] != -1 :
                                pol += '-'+str(np.abs(self.coefs[coef]))+'x'
                            else :
                                pol += '-'+'x'
                            
                        else :
                            pol += '-'+str(np.abs(self.coefs[coef]))
                    else :
                        pass
                    if len(pol) == 0 :
                        pol = '0'
               
                return pol
            
    def degre_pol(self):
        return len(self.coefs)
    
    def coef_plus_haut_degre(self):
        return self.coefs[0]
    
    def __pos__(self):
        return self
    
    def __neg__(self):
        self.coefs_neg = [-i for i in self.coefs]
        return Polynome(self.coefs_neg)
    
    
    def __add__(self, other):
        if isinstance(other, Polynome):
            if len(self.coefs) > len(other.coefs) :
                new_coefs = np.add(self.coefs[(len(self.coefs) - len(other.coefs) ): ], other.coefs)
                
                new_coefs = list(new_coefs)
                
                result = self.coefs[:(len(self.coefs) - len(other.coefs)  )]
                
                for i in new_coefs:
                    result.append(i)
                #on separe en deux cas parceque avec numpay on peut ajouter que des arrays de mm taille
                #on fait la reconversion en liste pour pouvoir mettre sous forme de polynome
                
            else :
                new_coefs = np.add(other.coefs[(len(other.coefs) - len(self.coefs) ): ], self.coefs)
                
                new_coefs = list(new_coefs)
                
                result = other.coefs[:(len(other.coefs) - len(self.coefs) )]
                for i in new_coefs:
                    result.append(i)       
            
            return Polynome(result)
        
    def __sub__(self, other):
        #une soustraction est aussi une addition
        if isinstance(other, Polynome):
            return self + -other
        
    def __mul__(self, other):
        #ici on se sert de la multiplication de deux arrays via numpay
        if isinstance(other, Polynome):
            mult = Polynome([0]) #recuperer la somme 
            j=1  #compteur pour decremter le degre du x
            for i in self.coefs :
                news = list(np.array(other.coefs)) + list(np.ones(len(self.coefs)-j)) #on ajoute des 1 pour gerer les exposant
                mult += ( Polynome( list(np.array(news).dot(np.array(i))) ) - Polynome( list( np.array(list(np.zeros(len(other.coefs)))+ list(np.ones(len(self.coefs)-j)) ).dot(np.array(i)) )  )    )    
                #les 1 sont retrancher et conservation des esposants
                j=j+1
            return mult
            
            
    def __truediv__(self, other):
        #diviser c'est multiplier par l'inverse
        if isinstance(other, Polynome):
            inverse_other = []
            for i in other.coefs :
                inverse_other.append(1/i)
            return self * Polynome(inverse_other)
        #diviser c'est multiplier par l'inverse
    
        
        
    
 
    
        
        
